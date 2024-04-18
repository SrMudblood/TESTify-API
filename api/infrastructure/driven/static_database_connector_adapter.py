import random
import string

from ...domain.repositories.for_connector_db_port import For_connector_db_adapter
from ...domain.models.person import Person
from ...source.countries.countries import Country

class Static_database_connector_adapter(For_connector_db_adapter):
    def create_normal_person_from_database(self, data: Person, country_code: string) -> dict:
        from ...source.professions.profession import Profession
        from ...source.languages.language import Language

        if country_code == "US":
            from ...source.US.person_names.US_first_name_F import US_first_name_F as first_name_f
            from ...source.US.person_names.US_first_name_M import US_first_name_M as first_name_m
            from ...source.US.person_names.US_last_name import US_last_name as last_name
        else:
            from ...source.US.person_names.US_first_name_F import US_first_name_F as first_name_f
            from ...source.US.person_names.US_first_name_M import US_first_name_M as first_name_m
            from ...source.US.person_names.US_last_name import US_last_name as last_name

        country, dialing_code, state_province, city = Country().getRandomCountryData
        
        if data.first_name == None:
            data.first_name = first_name_m().getRandomName if data.gender == "Male" else first_name_f().getRandomName
        if data.last_name == None:
            data.last_name = last_name().getRandomLastName
        data.full_name = data.first_name + " " + data.last_name
        if data.occupation == None:
            data.occupation = Profession().getRandomProfession
        if len(data.languages) == 0:
            data.languages = Language().getRandomLanguages(3)
        if data.employer == None:
            data.employer = (first_name_m().getRandomName if random.randint(0,1) == 1 else first_name_f().getRandomName)+" "+last_name().getRandomLastName
        if data.country == None:
            data.country = country
        if data.state_province == None:
            data.state_province = state_province
        if data.city == None:
            data.city = city
        if data.phone_number == None:
            data.phone_number = '+' + str(dialing_code) + ''.join([str(random.randint(0, 9)) for _ in range(10)])
        if data.email_address == None:
            data.email_address = str(data.first_name).lower()+str(data.last_name).lower()+str(data.age)+"@gmail.com"

        return data.getPersonData