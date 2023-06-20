from django.urls import path

from .views import OrderCreateView, CanceledTemplateView, SuccessTemplateView

app_name = "orders"

urlpatterns = [
    path("", OrderCreateView.as_view(), name="order_create"),
    path("order-success/", SuccessTemplateView.as_view(), name="order_success"),
    path("order-canceled/", CanceledTemplateView.as_view(), name="order_canceled"),
]