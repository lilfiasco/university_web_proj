# Python
from typing import Any

# Django
from django.shortcuts import render, redirect
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import (
    HttpRequest,
    HttpResponse,
    QueryDict,
    JsonResponse,
)
from django.views.generic import (
    View,
    ListView,
)
from rest_framework.generics import ListAPIView
from django.core.files.uploadedfile import InMemoryUploadedFile

# Local
from .models import (
    Furniture,
    Rooms,
    Basket,
    Favs
)
from abstracts.mixins import HttpResponseMixin
from abstracts import utils
from .forms import (
    FurnitureForm,
    BasketForm
)
from .serializers import FurnitureSerializer

from django.views.decorators.csrf import csrf_exempt


class MainView(HttpResponseMixin, View):
    """Main view."""

    queryset: QuerySet = Furniture.objects.all()

    def get(self, request: HttpRequest, *args, **kwargs):

        u: QuerySet
        try:
            u = Furniture.objects.filter(
                title=Furniture.objects.get(title='Диван').id
            )
        except:
            u = {}

        return self.get_http_response(
            request=request,
            template_name='main/home_page.html',
            context={
                'u': u,
                'ctx_user': request.user
            }
        )
    

class RoomView(View):
    def get(self, request):
        rooms = Rooms.objects.all()
        fur = Furniture.objects.all()
        print(len(fur))
        
        return render(request, 'main/room.html', {"rooms_list": rooms, "furs": fur})
    

class RoomDetailView(View):
    def get(self, request, pk):
        room = Rooms.objects.get(id=pk)
        furnitures = room.furniture_set.all()

        print(type(furnitures))

        return render(request, 'main/production.html', {"room": room, 'furniture_list': furnitures})


class FurnitureDetailView(View):
    def get(self, request, slug):
        print("FFFFFFFF:", slug)
        furniture = Furniture.objects.get(url=slug)

        return render(request, 'main/production.html', {"furniture": furniture})


class FurnituresListView(ListAPIView):
    serializer_class = FurnitureSerializer
    
    def get_queryset(self):
        print("AAAAAAAAAAAAAAAAAAAAAAA work pls")
        queryset = Furniture.objects.filter(room=Rooms.objects.get(pk=self.kwargs.get('pk'))).all()
        print(list(queryset))
        
        return queryset

def favs(request):
    items = Favs.objects.filter(user=request.user).all()
    # form = BasketForm()
    return render(request, 'main/favs.html', context={'items': items})

def basket(request):
    items = Basket.objects.filter(user=request.user).all()
    # form = BasketForm()
    return render(request, 'main/cart.html', context={'items': items})


@csrf_exempt
def add_to_basket(request, id):
    furniture =  Furniture.objects.get(id=id)
    print(furniture)
    basket = Basket.objects.filter(user=request.user, furniture=furniture)
    price = request.POST.get("price")
    print(basket)

    if not basket.exists():
        Basket.objects.create(user = request.user, furniture=furniture, price=price, quantity_buying=1)
    else:
        basket=basket.first()
        basket.quantity_buying += 1
        basket.save()

    return render(request, 'main/add.html')

def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return redirect("cart")


def add_favs(request, id):
    success = False
    furniture =  Furniture.objects.get(id=id)
    favorite = Furniture.objects.filter(user=request.user, furniture=furniture)
    print("DDDDD: ", favorite)

    if not favorite.exists():
        Favs.objects.create(user = request.user, furniture=furniture)
        success = True
    else:
        favorite = favorite.first()
        favorite.save()
        success = True

    return JsonResponse({'success': success})

def favs_remove(request, id):
    favorite = Favs.objects.get(id=id)
    favorite.delete()
    return redirect("favorite")



def order_book(request):
    return render(request, 'main/purchase.html')
