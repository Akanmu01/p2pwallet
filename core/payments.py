from rave_python import Rave, RaveExceptions, Misc
from decimal import Decimal
from p2pwallet.settings import FLW_PUB_KEY, FLW_SEC_KEY

rave = Rave(FLW_PUB_KEY, FLW_SEC_KEY, usingEnv = False)

def flutter_wave(amount, email):
    # Payload with pin
    payload = {
    "cardno": "5531886652142950", 
    "cvv": "564",
    "expirymonth": "09", 
    "expiryyear": "32", 
    "amount": str(amount), 
    "email": email, 
    "phone_number": "08100000000",
    "first_name": "test",
    "last_name": "test",
    "IP": "355426087298442",
    }

    try:
        res = rave.Card.charge(payload)

        if res["suggestedAuth"]:
            arg = Misc.getTypeOfArgsRequired(res["suggestedAuth"])

            if arg == "pin":
                Misc.updatePayload(res["suggestedAuth"], payload, pin=3310)
            if arg == "address":
                Misc.updatePayload(res["suggestedAuth"], payload, address= {"billingzip": "07205", "billingcity": "Hillside", "billingaddress": "470 Mundet PI", "billingstate": "NJ", "billingcountry": "US"})
            
            res = rave.Card.charge(payload)

        if res["validationRequired"]:
            rave.Card.validate(res["flwRef"], "12345")

        res = rave.Card.verify(res["txRef"])
        return {
            'status' : 'success',
            'success' : res
        }

    except RaveExceptions.CardChargeError as e:
        return {
            'status' : 'error',
            'error' : e.err
        }
    except RaveExceptions.TransactionValidationError as e:
        return {
            'status' : 'error',
            'error' : e.err
        }    
    except RaveExceptions.TransactionVerificationError as e:
        return {
            'status' : 'error',
            'error' : e.err
        }

