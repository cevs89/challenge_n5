import json

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.api.serializers import InfractionSerializer
from apps.api.service import InfractionService
from apps.api.validators import InfractionValidator


class InfractionViewSet(viewsets.ViewSet):
    """
    Esta clase solo representa el acceso, la peticion del API.
    permission_classes: Valida que este en token correcto
    serializer_class: Obj para utilizar dentro de la clase
    service_infraction: Obj para utilizar dentro de la clase
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = InfractionSerializer
    service_infraction = InfractionService()

    def create(self, request) -> Response:
        # Validate json body is correct
        try:
            json.dumps(request.data)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)

        # Validate data body is correct
        try:
            _validation_data = InfractionValidator.parse_obj(request.data)
        except Exception as e:
            return Response(json.loads(e.json()), status=status.HTTP_404_NOT_FOUND)

        # Service save logical service
        try:
            _data_save = self.service_infraction.save(_validation_data, request.user)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)

        # Serializar object return
        serializer = self.serializer_class(_data_save)
        return Response(serializer.data, status=status.HTTP_200_OK)
