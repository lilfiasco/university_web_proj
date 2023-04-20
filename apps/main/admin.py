from typing import Optional

from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from .models import (
    Furniture,
    Company,
    Rooms,
)


class FurnitureAdmin(admin.ModelAdmin):
    """FurnitureAdmin."""

    model = Furniture

    search_fields = (
        'title'
    )
    readonly_fields = ()
    list_filter = (
        'price',
    )
    list_display = (
        'title',
        'room_belonging',
        'price',
        'company'
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
            'price',
            'company'
        )


class CompanyAdmin(admin.ModelAdmin):
    """CompanyAdmin."""

    model = Company
    readonly_fields = ()
    list_display = (
        'title'
    )

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Company] = None
    ) -> tuple[str, ...]:
        """Get readonly fields."""

        if not obj:
            return self.readonly_fields

        return self.readonly_fields + (
            'title'
        )
    

class RoomsAdmin(admin.ModelAdmin):
    """RoomsAdmin."""

    model = Rooms
    readonly_fields = ()
    list_display = (
        'title'
    )

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
admin.site.register(Company, CompanyAdmin)
admin.site.register(Rooms, RoomsAdmin)
