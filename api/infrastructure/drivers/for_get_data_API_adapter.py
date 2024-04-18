import json
from django.http import JsonResponse

from ..driven.static_database_connector_adapter import Static_database_connector_adapter as db
from ...application.views.get_normal_person_use_case import NormalPerson

class For_get_data_API_adapter():

    def __init__(self) -> None:
        self._db = db

    def get_normal_person(self, request):
        if request.method == "GET":
            return JsonResponse({'error': 'GET method not allowed in this view'}, status=405)
        elif request.method == "POST":
            return NormalPerson().post(json.loads(request.body.decode('utf-8')), self._db)