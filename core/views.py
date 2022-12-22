from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes



class SignUpView(APIView):
    '''
    -  Users signup with their email and specified password 
    and get assigned a wallet address on successful signup.
    '''
    serializer_class = SignUpSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    '''
    - Users sign in with the credentials used to sign up.
    - Returns the user's email and a token which is used in authenticating the user for all other endpoints.
    '''
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class P2PTransferView(APIView):
    '''
    - Users can carry out in app <b>P2P</b> transfers by supplying the email of another user, amount and detail.
    - A Transaction History object is created on succesful transfer.
    '''
    serializer_class = P2PTransferSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        if serializer.data['status'] == 'error':
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED) 


class GetTransactionHistoryView(ListAPIView):
    '''
    - Returns a list of all transactions carried out by a user
    '''
    serializer_class = TransactionHistorySerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        user = Wallet.objects.get(owner=self.request.user)

        history = TransactionHistory.objects.filter((Q(sender=user) & (Q(trans_type=TransactionHistory.DEBIT) |
                Q(trans_type=TransactionHistory.FUND_WALLET)))  | (Q(recipient=user) & Q(trans_type=TransactionHistory.CREDIT)))
        return history.order_by('-time')


class FundWalletView(APIView):
    '''
    - Users can fund their wallet after successful sign up and authentication. 
    - Amount is capped at NGN3000.00 per transaction.
    - A Transaction History object is created on succesful wallet funding.
    '''
    serializer_class = FundWalletSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        if serializer.data['status'] == 'error':
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ProfileView(APIView):

#     serializer_class = ProfileSerializer
#     permission_classes = (IsAuthenticated,)

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         if serializer.data['status'] == 'error':
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @csrf_exempt
# def profileview(request):

#     # if request.method == 'GET':
#     #     profiles = Profile.objects.all()
#     #     serializer = ProfileSerializer(profiles, many=True)
#     #     return JsonResponse(serializer.data, safe=False)

#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ProfileSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @api_view(['POST'])
# @csrf_exempt
# # @csrf_protect
# @permission_classes([IsAuthenticated])
# def profileview(request):
#   # parser_classes = (MultiPartParser, FormParser)
#   if request.method == 'POST':
#     serializer = ProfileSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def profileview(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def getprofile(request):
  if request.method == 'GET':
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


def wallet(request):
    if request.method == 'GET':
        wallet = Wallet.objects.all()
        serializer = WalletSerializer(wallet, many=True)
        return Response(serializer.data)