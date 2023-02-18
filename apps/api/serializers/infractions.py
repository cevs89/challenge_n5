from datetime import datetime

import serpy


class InfractionSerializer(serpy.Serializer):
    """
    Serializador para un modelo, especificamente para el modelo: Infractions

    Field(): Devuelve el valor plano que recibe.
    MethodField(): Devuelve el valor de la relacion, se accede mediante una funcion.
    se debe definir como: get_NOMBRE_DEL_CAMPO

    De esta manera se accede al valor de la relacion entre el modelo principal.


    Tambien se puede parsear data plana, hacer filtro o cualquier otra funcionalidad
    necesario dento de cada funcion
    """

    patent = serpy.MethodField()
    brand = serpy.MethodField()
    color = serpy.MethodField()
    vehicle_type = serpy.MethodField()
    person = serpy.MethodField()
    timestamp = serpy.MethodField()
    comment = serpy.Field()

    def get_patent(self, obj):
        if obj.vehicle is not None:
            return obj.vehicle.patent

    def get_brand(self, obj):
        if obj.vehicle is not None:
            return obj.vehicle.brand

    def get_color(self, obj):
        if obj.vehicle is not None:
            return obj.vehicle.color

    def get_vehicle_type(self, obj):
        if obj.vehicle is not None:
            return obj.vehicle.get_vehicle_type_display()

    def get_person(self, obj):
        if obj.vehicle is not None:
            return obj.vehicle.person.email_person

    def get_timestamp(self, obj):
        if obj.timestamp is not None:
            return datetime.strftime(obj.timestamp, "%Y-%m-%d %H:%M")
