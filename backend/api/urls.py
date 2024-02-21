from django.urls import path

from .views import CurrencyListView, CurrencyDetailView

app_name = "api"

urlpatterns = [
    path("currencies/", CurrencyListView.as_view(), name="currency_list"),
    path("currency/<int:pk>/", CurrencyDetailView.as_view(), name="currency_detail"),
]
