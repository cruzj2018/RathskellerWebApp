from django.urls import path
from . import views
app_name = "order"

urlpatterns = [
    path("my-order/", views.order_list, name="order-list"),
]