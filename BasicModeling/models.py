from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Address(models.Model):
    # Constants
    PROVINCES = [
        ("ONTARIO", "Ontario"),
        ("QUEBEC", "Quebec"),
        ("NOVA SCOTIA", "Nova Scotia"),
        ("NEW BRUNSWICK", "New Brunswick"),
        ("MANITOBA", "Manitoba"),
        ("BRITISH COLUMBIA", "British Columbia"),
        ("PRINCE EDWARD ISLAND", "Prince Edward Island"),
        ("SASKATCHEWAN", "Saskatchewan"),
        ("ALBERTA", "Alberta"),
        ("NEWFOUNDLAND", "Newfoundland"),
        ("NORTHWEST TERRITORIES", "Northwest Territories"),
        ("YUKON", "Yukon"),
        ("NUNAVUT", "Nunavut"),
    ]

    # Model fields
    address_id = models.AutoField(primary_key=True)
    street_number = models.IntegerField(validators=[MinValueValidator(1)])
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(choices=PROVINCES, max_length=100)
    postal_code = models.CharField(max_length=7)

    # Overridden model methods
    def save(self, *args, **kwargs):
        # Ensure a full clean is performed before 
        # allowing a database save. This ensures that
        # our fields are fully validated. This doesn't happen
        # in the default model        
        self.full_clean()

        # If we reach here no errors were found and we can
        # save our model to the database
        super().save(*args, **kwargs)


class PhoneNumber(models.Model):
    # Constants
    PHONE_TYPES = [
        ("HOME", "Home"),
        ("MOBILE", "Mobile"),
        ("WORK", "Work"),
        ("OTHER", "Other"),
    ]

    # Model fields    
    phone_number_id = models.AutoField(primary_key=True)
    phone_number = models.BigIntegerField(validators=[MinValueValidator(1_000_000_000),
                                                      MaxValueValidator(9_999_999_999)])
    phone_type = models.CharField(choices=PHONE_TYPES, max_length=10)
    
    # Overridden model methods
    def save(self, *args, **kwargs):
        # Ensure a full clean is performed before 
        # allowing a database save. This ensures that
        # our fields are fully validated. This doesn't happen
        # in the default model        
        self.full_clean()

        # If we reach here no errors were found and we can
        # save our model to the database
        super().save(*args, **kwargs)


class Employee(models.Model):
    # Constants
    GENDERS = [
        ("M", "Male"),
        ("F", "Female"),
        ("U", "Unidentified/Other"),
    ]
    HAIR_COLORS = [
        ("BLONDE", "Blonde"),
        ("BRUNETTE", "Bruneete"),
        ("BROWN", "Brown"),
        ("BLACK", "Black"),
        ("GRAY", "Gray"),
        ("RED", "Red"),
        ("PURPLE", "Purple"),
        ("BLUE", "Blue"),
        ("GREEN", "Green"),
    ]
    EYE_COLOR = [
        ("GREEN", "Green"),
        ("BLUE", "Blue"),
        ("HAZEL", "Hazel"),
        ("BROWN", "Brown"),
    ]
    
    # Model fields 
    employee_id = models.AutoField(primary_key=True)    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(120)])
    gender = models.CharField(choices=GENDERS, max_length=1)
    hair_color = models.CharField(choices=HAIR_COLORS, max_length=20)
    eye_color = models.CharField(choices=EYE_COLOR, max_length=20)
    social_insurance_number = models.IntegerField(validators=[MinValueValidator(100_000_000),
                                                              MaxValueValidator(999_999_999)])
    # Note: In this setup, if the Address is deleted from the database we will also CASCADE delete all
    #       the employees who also have this address. We could also change this to instead set this address
    #       reference to NULL or DO_NOTHING instead. 
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    # Note: When creating a ManyToMany relationship you only need to define it in one model. The model you 
    #       select should be the model you are more likely to edit or the model that has ownership of the other
    #       model (e.g. An employee has a phone number not a phone number has an employee)
    phone_numbers = models.ManyToManyField(PhoneNumber)

    # Overridden model methods
    def save(self, *args, **kwargs):
        # Ensure a full clean is performed before 
        # allowing a database save. This ensures that
        # our fields are fully validated. This doesn't happen
        # in the default model        
        self.full_clean()

        # If we reach here no errors were found and we can
        # save our model to the database
        super().save(*args, **kwargs)    