import json
from nss_handler import status
from models import Agency

class AgencyView():

    def get(self, handler, pk):
        if pk != 0:
            return handler.response("", status.HTTP_200_SUCCESS.value)
        else:
            agency_model = Agency()
            agencies = agency_model.get_all()
            serialized_agencies = json.dumps(agencies)

            return handler.response(serialized_agencies, status.HTTP_200_SUCCESS.value)

