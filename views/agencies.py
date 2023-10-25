"""Agency view module"""
import json
from nss_handler import status
from models import Agency

class AgencyView():
    """Agency view class"""
    def get(self, handler, pk):
        """Method for handling GET requests for /agencies

        Args:
            handler (object): HTTP request handle to send response
            pk (int): Primary key of request resource

        Returns:
            None
        """
        agency_model = Agency()

        if pk != 0:
            serialized_agency = json.dumps(agency_model.get_single(pk))
            return handler.response(serialized_agency, status.HTTP_200_SUCCESS)

        serialized_agencies = json.dumps(agency_model.get_all())
        handler.response(serialized_agencies, status.HTTP_200_SUCCESS)

