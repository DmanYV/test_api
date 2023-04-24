from voluptuous import PREVENT_EXTRA, Schema


booking = Schema(
    {
        "firstname": str,
        "lastname": str,
        "totalprice": int,
        "depositpaid": bool,
        "bookingdates" : {
                            "checkin" : str,
                            "checkout" : str
    },
    "additionalneeds" : str
    },
        extra=PREVENT_EXTRA,
        required=True
)