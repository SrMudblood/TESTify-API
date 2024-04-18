from abc import ABC, abstractmethod
import string

from ...domain.models.person import Person

class For_connector_db_adapter(ABC):

    @abstractmethod
    def create_normal_person_from_database(self, data: Person, country_code: string) -> dict:
        pass