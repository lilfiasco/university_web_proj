from typing import Optional

from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from .models import (
    Furniture,
    Rooms,
)


class FurnitureAdmin(admin.ModelAdmin):
    """FurnitureAdmin."""

    model = Furniture

    readonly_fields = ()
    list_filter = (
        'price',
    )
    list_display = (
        'title',
        'room_belonging',
        'price'
    )
    ordering = ('-id',)

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Furniture] = None
    ) -> tuple[str, ...]:
        """Get readonly fields."""

        if not obj:
            return self.readonly_fields

        return self.readonly_fields + (
            'title',
            'room_belonging',
            'price'
        )
    

class RoomsAdmin(admin.ModelAdmin):
    """RoomsAdmin."""

    model = Rooms
    readonly_fields = ()
    list_display = [
        'title'
    ]

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Rooms] = None
    ) -> tuple[str, ...]:
        """Get readonly fields."""

        if not obj:
            return self.readonly_fields

        return self.readonly_fields + (
            'title'
        )
    
admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(Rooms, RoomsAdmin)
