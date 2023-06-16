from django.urls import path
from fuel.views import fuel_list, FuelListView, FuelDetailsView,\
    FuelCreateView, FuelUpdateView, FuelDeleteView


urlpatterns = [
    path("", FuelListView.as_view(), name="fuel-list"),
    path("<int:pk>/", FuelDetailsView.as_view(), name="fuel-details"),
    path("update/<int:pk>/", FuelUpdateView.as_view(), name="fuel-update"),
    path("delete/<int:pk>/", FuelDeleteView.as_view(), name="fuel-delete"),
    path("create/", FuelCreateView.as_view(), name="fuel-create"),
]
