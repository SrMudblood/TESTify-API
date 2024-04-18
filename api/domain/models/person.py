class Person:
    def __init__(self, data: dict) -> None:
        self._body = {
                "first_name": data['first_name'],
                "last_name": data['last_name'],
                "full_name": data['full_name'],
                "date_of_birth": data['date_of_birth'],
                "age": data['age'],
                "gender": data['gender'],
                "marital_status": data['marital_status'],
                "social_security_number": data['social_security_number'],
                "passport_number": data['passport_number'],
                "drivers_license_number": data['drivers_license_number'],
                #"address": fake.address().replace("\n", ", "),
                "city": data['city'],
                "state_province": data['state_province'],
                "postal_code": data['postal_code'],
                "country": data['country'],
                "phone_number": data['phone_number'],
                "email_address": data['email_address'],
                "occupation": data['occupation'],
                "employer": data['employer'],
                "education_level": data['education_level'],
                "languages": data['languages'],
            }

    @property 
    def getPersonData(self):
        return self._body
    
    def _get_first_name(self):
        return self._body['first_name']

    def _set_first_name(self, value):
        self._body['first_name'] = value

    def _get_last_name(self):
        return self._body['last_name']

    def _set_last_name(self, value):
        self._body['last_name'] = value

    def _get_full_name(self):
        return self._body['full_name']

    def _set_full_name(self, value):
        self._body['full_name'] = value

    def _get_date_of_birth(self):
        return self._body['date_of_birth']

    def _set_date_of_birth(self, value):
        self._body['date_of_birth'] = value

    def _get_age(self):
        return self._body['age']

    def _set_age(self, value):
        self._body['age'] = value

    def _get_gender(self):
        return self._body['gender']

    def _set_gender(self, value):
        self._body['gender'] = value

    def _get_marital_status(self):
        return self._body['marital_status']

    def _set_marital_status(self, value):
        self._body['marital_status'] = value

    def _get_social_security_number(self):
        return self._body['social_security_number']

    def _set_social_security_number(self, value):
        self._body['social_security_number'] = value

    def _get_passport_number(self):
        return self._body['passport_number']

    def _set_passport_number(self, value):
        self._body['passport_number'] = value

    def _get_drivers_license_number(self):
        return self._body['drivers_license_number']

    def _set_drivers_license_number(self, value):
        self._body['drivers_license_number'] = value

    def _get_city(self):
        return self._body['city']

    def _set_city(self, value):
        self._body['city'] = value

    def _get_state_province(self):
        return self._body['state_province']

    def _set_state_province(self, value):
        self._body['state_province'] = value

    def _get_postal_code(self):
        return self._body['postal_code']

    def _set_postal_code(self, value):
        self._body['postal_code'] = value

    def _get_country(self):
        return self._body['country']

    def _set_country(self, value):
        self._body['country'] = value

    def _get_phone_number(self):
        return self._body['phone_number']

    def _set_phone_number(self, value):
        self._body['phone_number'] = value

    def _get_email_address(self):
        return self._body['email_address']

    def _set_email_address(self, value):
        self._body['email_address'] = value

    def _get_occupation(self):
        return self._body['occupation']

    def _set_occupation(self, value):
        self._body['occupation'] = value

    def _get_employer(self):
        return self._body['employer']

    def _set_employer(self, value):
        self._body['employer'] = value

    def _get_education_level(self):
        return self._body['education_level']

    def _set_education_level(self, value):
        self._body['education_level'] = value

    def _get_languages(self):
        return self._body['languages']

    def _set_languages(self, value):
        self._body['languages'] = value

    first_name = property(_get_first_name, _set_first_name)
    last_name = property(_get_last_name, _set_last_name)
    full_name = property(_get_full_name, _set_full_name)
    date_of_birth = property(_get_date_of_birth, _set_date_of_birth)
    age = property(_get_age, _set_age)
    gender = property(_get_gender, _set_gender)
    marital_status = property(_get_marital_status, _set_marital_status)
    social_security_number = property(_get_social_security_number, _set_social_security_number)
    passport_number = property(_get_passport_number, _set_passport_number)
    drivers_license_number = property(_get_drivers_license_number, _set_drivers_license_number)
    city = property(_get_city, _set_city)
    state_province = property(_get_state_province, _set_state_province)
    postal_code = property(_get_postal_code, _set_postal_code)
    country = property(_get_country, _set_country)
    phone_number = property(_get_phone_number, _set_phone_number)
    email_address = property(_get_email_address, _set_email_address)
    occupation = property(_get_occupation, _set_occupation)
    employer = property(_get_employer, _set_employer)
    education_level = property(_get_education_level, _set_education_level)
    languages = property(_get_languages, _set_languages)