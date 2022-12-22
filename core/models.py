import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)   
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password, **extra_fields):
        '''
        Create and return a `User` with superuser (admin) permisissions.
        '''
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, password, is_superuser=True)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True,blank=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    def __str__(self):
        return str(self.email)



class Wallet(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=10, blank=True, editable=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True) 
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account_no}"


 
class TransactionHistory(models.Model):
    CREDIT = 'credit'
    DEBIT = 'debit'
    FUND_WALLET =  'fund_wallet'
    TRANSACTION_TYPE = ((CREDIT, 'Credit'),(DEBIT, 'Debit'),(FUND_WALLET, 'Fund Wallet'),)
    reference_number = models.UUIDField(default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='trans_sender')
    trans_type = models.CharField(max_length=20,choices=TRANSACTION_TYPE)
    amount  = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)
    time = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='trans_recipient')
    details = models.CharField(max_length=255)

    def __str__(self):
        return str(self.reference_number)

