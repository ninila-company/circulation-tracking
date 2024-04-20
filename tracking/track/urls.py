from django.urls import path
from . import views


app_name = 'track'

urlpatterns = [
    # представления заказа
    path("", views.order_list, name="order_list"),
    # path("ajax/example/", views.ajax_example_view, name="ajax_example"),
]
