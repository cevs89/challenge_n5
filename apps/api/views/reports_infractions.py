import json

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.serializers import InfractionSerializer
from apps.api.service import ReportsInfractionService
from apps.api.validators import ReportsInfractionValidator


class ReportsInfractionViewSet(APIView):
    permission_classes = (AllowAny,)
    service_reports = ReportsInfractionService()
    serializer_class = InfractionSerializer

    def get(self, request, *args, **kwargs) -> Response:
        # Validate json body is correct
        try:
            _validation_data = ReportsInfractionValidator.parse_obj(kwargs)
        except Exception as e:
            return Response(json.loads(e.json()), status=status.HTTP_404_NOT_FOUND)

        # Service save logical service
        try:
            _data_save = self.service_reports.find(_validation_data)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)

        # Serializar object return
        serializer = self.serializer_class(_data_save, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
