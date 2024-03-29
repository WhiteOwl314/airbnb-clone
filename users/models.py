from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGAUGE_ENGLISH = "en"
    LANGAUGE_KOREAN = "kr"

    LANGAUGE_CHOICES = ((LANGAUGE_ENGLISH, "English"), (LANGAUGE_KOREAN, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )

    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    langauge = models.CharField(choices=LANGAUGE_CHOICES, max_length=2, blank=True)

    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)

    superhost = models.BooleanField(default=False)
