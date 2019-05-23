# Setup code to load django framework
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoModeling.settings'
django.setup()

# Step 1: Import models to work with
from BasicModeling.models import Employee, Address, PhoneNumber

# Step 2: Create a new address for the employee and save it to the database
e1_address = Address(street_number=123, street_name="Burnel St", city="WINNIPEG", province="MANITOBA", postal_code="R3G2B3")
e1_address.save()

# Step 3: Create a set of phone numbers for the employee and save them to the database
e1_home_phone = PhoneNumber(phone_number=2045551212, phone_type="HOME")
e1_home_phone.save()

e1_mobile_phone = PhoneNumber(phone_number=2045557171, phone_type="MOBILE")
e1_mobile_phone.save()

e1_work_phone = PhoneNumber(phone_number=2045559999, phone_type="WORK")
e1_work_phone.save()

# Step 4: Create an employee with an address but no phone numbers associated with it and save to the database
# Notice: Before we can associate the ManyToMany relationships we need the record to exist in both the Employee table
#         as well as the PhoneNumber table hence why we save this record before creating the associations
e1 = Employee(first_name='John', last_name='Doe', age=37, gender='M', hair_color='BROWN', eye_color='HAZEL', social_insurance_number=123456789)
e1.address = e1_address
e1.save()

# Step 5: Associate one or more phone numbers to this employee
# Notice: We don't have to save our changes as this is done automatically
e1.phone_numbers.add(e1_home_phone)
e1.phone_numbers.add(e1_mobile_phone, e1_work_phone)