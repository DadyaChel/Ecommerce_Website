from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from shop import views
from accounts import views as acc_views

acc_router = routers.DefaultRouter()
acc_router.register('account', acc_views.ProfileViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', auth_views.obtain_auth_token),

    path('api/accounts/register/', include(acc_router.urls)),
    # path('api/account/register/sender/', include(acc_router.urls)), #dool=True
    # path('api/account/register/buyer/', include(acc_router.urls)),  #boll=False

    path('category/', views.CategoryCreateListView.as_view()),
    # path('api/shop/category/', views.CategoryCreateListView.as_view()),

    path('category/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    # path('api/shop/category/<int:id>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),

    path('item/', views.ItemCreateListView.as_view()),
    # path('api/shop/category/<int:id>/item/', views.ItemCreateListView.as_view()),

    path('item/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view()),
    # path('api/shop/category/<int:id>/item/<int:pk>/', views.ItemCreateListView.as_view()),

    path('order/', views.OrderCreateListView.as_view()),
    # path('api/shop/category/<int:id>/item/<int:pk>/order/ ', views.OrderCreateListView.as_view()),

    path('order/<int:pk>/', views.OrderRetrieveUpdateDestroyAPIView.as_view()),
    # path('api/shop/category/<id>/item/<pk>/order/<order_id>/', views.OrderRetrieveUpdateDestroyAPIView.as_view()),
]
