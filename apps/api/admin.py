from django.contrib import admin

from apps.api.models import Infractions, PersonCitizen, PersonOfficer, Vehicle


@admin.register(Infractions)
class InfractionsAdmin(admin.ModelAdmin):
    list_display = (
        "vehicle",
        "officer_allowed",
        "comment",
        "is_active",
        "created_at",
        "modified_at",
    )
    search_fields = (
        "vehicle__patent",
        "vehicle__person__name_person",
        "vehicle__person__email_person",
    )
    ordering = ("vehicle",)
    list_filter = ("vehicle__patent",)


@admin.register(PersonCitizen)
class PersonCitizenAdmin(admin.ModelAdmin):
    list_display = (
        "name_person",
        "email_person",
        "is_active",
        "created_at",
        "modified_at",
    )
    search_fields = ("name_person", "email_person")
    list_filter = ("is_active",)


@admin.register(PersonOfficer)
class PersonOfficerAdmin(admin.ModelAdmin):
    list_display = (
        "name_officer",
        "personal_id",
        "token_officer",
        "is_active",
        "created_at",
        "modified_at",
    )
    search_fields = ("name_officer", "personal_id")
    list_filter = ("is_active",)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "patent",
        "person",
        "brand",
        "color",
        "vehicle_type",
        "created_at",
        "modified_at",
    )
    search_fields = ("patent", "brand", "color", "vehicle_type")
    ordering = ("vehicle_type",)
    list_filter = ("vehicle_type",)
