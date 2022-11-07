from django.contrib import admin
from .models import Room, Amenity

# Register your models here.
@admin.register(Room)
class Room(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "owner",
        "total_amenities",
        "created_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_filter = (
        "country",
        "city",
        "amenities",
        "created_at",
        "updated_at",
    )

    def total_amenities(self, room):
        return room.amenities.count()

    pass


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
