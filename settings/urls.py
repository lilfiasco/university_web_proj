from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from main.views import (
    MainView,
    RoomView,
    RoomDetailView,
    FurnitureDetailView,
    FurnituresListView,

    favs,
    add_favs,
    favs_remove,

    basket, 
    add_to_basket,
    basket_remove,
    order_book
)

from auths.views import(
    LoginView,
    LogoutView,
    RegistrationView,
    ProfileView,
    EditView,
    ChangePassowrdView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),

    path('', MainView.as_view()),
    path('auths/', LoginView.as_view()),
    path('auths/log-out', LogoutView.as_view()),
    path('auths/registration', RegistrationView.as_view()),
    path('auths/profile', ProfileView.as_view()),
    path('auths/edit', EditView.as_view()),
    path('auths/change-password', ChangePassowrdView.as_view()),


    path('room/', RoomView.as_view(), name='room'),
    path('<int:pk>/', RoomDetailView.as_view()),
    path('production/<slug:slug>/', FurnitureDetailView.as_view()),
    path('get_furniture_by_room_id/<int:pk>', FurnituresListView.as_view(), name='get_furniture_by_room_id'),

    path('favs/', favs, name='favs'),
    path('favs/add/<int:id>', add_favs, name='add_favs' ),
    path('favs/remove/<int:id>', favs_remove, name='favs_remove'),

    path('cart/', basket, name='cart'),
    path('cart/add/<int:id>', add_to_basket, name='cart_add' ),
    path('cart/remove/<int:id>', basket_remove, name='cart_remove'),
    path('buy/', order_book, name='purchase')

    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)