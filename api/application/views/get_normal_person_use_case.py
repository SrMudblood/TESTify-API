import json
import random
import string
from django.http import HttpResponse
from django.views import View
from datetime import datetime
from dateutil.relativedelta import relativedelta

from ...domain.models.person import Person
from ...domain.repositories.for_connector_db_port import For_connector_db_adapter

# Create your views here.

class NormalPerson(View):
    
    def post(self, request, db: For_connector_db_adapter):
        person = Person(request)
        if person.postal_code == None:
            person.postal_code = "".join([str(random.randint(0,9)) for _ in range(5)])
        if person.gender == None:
            person.gender = random.choice(["Male", "Female"])
        if person.education_level == None:
            person.education_level = random.choice(["Preschool", "Elementary School", "High School", "University"])
        if person.date_of_birth == None:
            start_date = datetime.now() - relativedelta(years=100)
            end_date =  datetime.now() - relativedelta(years=12)
            date = start_date + (end_date - start_date) * random.random()
            person.date_of_birth = date.strftime("%Y-%m-%d")
            person.age = (datetime.now() - relativedelta(years=date.year, months=date.month, days=date.day)).year
        else:
            date = datetime.strptime(person.date_of_birth, "%Y %m %d")
            person.age = (datetime.now() - relativedelta(years=date.year, months=date.month, days=date.day)).year
        if person.marital_status == None:
            person.marital_status = "single" if person.age <18 else random.choice(['single', 'married', 'widowed', 'divorced', 'common law'])
        if person.drivers_license_number == None:
            person.drivers_license_number = "".join([str(random.randint(0,9)) for _ in range(7)])
        if person.social_security_number == None:
            person.social_security_number = "".join([str(random.randint(0,9)) for _ in range(3)])+"-"+"".join([str(random.randint(0,9)) for _ in range(2)])+"-"+"".join([str(random.randint(0,9)) for _ in range(4)])
        if person.passport_number == None:
            person.passport_number = "".join(random.choice(string.ascii_letters).upper() for _ in range(2))+"".join([str(random.randint(0,9)) for _ in range(7)])
        return HttpResponse(json.dumps(db().create_normal_person_from_database(person, "US")))