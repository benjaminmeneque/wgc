from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Attendance(models.Model):
    COMPANY_CHOICES = [
        ("wesupport incorporated", "WeSupport Incorporated "),
        (
            "tranzend solutions and trading corporation",
            "Tranzend Solutions and Trading Corporation",
        ),
        ("JR", "Junior"),
        ("SR", "Senior"),
        ("GR", "Graduate"),
    ]
    full_name = models.CharField(max_length=255)
    company = models.CharField(choices=COMPANY_CHOICES, max_length=100)
    contact_number = PhoneNumberField(region="PH")
    coupon = models.CharField(max_length=255)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["create_timestamp"]

    def __str__(self):
        return self.full_name
