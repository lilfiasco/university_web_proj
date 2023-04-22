from django import forms 

from .models import Furniture, Basket


class FurnitureForm(forms.ModelForm):
    """Furniture form."""

    class Meta:
        model = Furniture
        fields = (
            'title',
            'room',
            'price'
        )


class BasketForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Basket, self).__init__(*args, **kwargs)
        self.fields['furniture'].required = False
        self.fields['user'].required = False
        self.fields['quantity_buying'].required = False
        self.fields['price'].required = False

    class Meta:
        model = Basket
        fields = "__all__"