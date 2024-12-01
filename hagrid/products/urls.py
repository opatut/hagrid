from django.contrib import admin
from django.urls import include, path

from .views import (
    ProductsConfigOverviewView,
    VariationConfigView,
    VariationAvailabilityConfigView,
    VariationAvailabilityEventListView,
    variation_count_overview_view,
    variation_count_view,
    VariationCountSuccessView,
)

urlpatterns = [
    path("", ProductsConfigOverviewView.as_view(), name="products_config_overview"),
    path(
        "availability/",
        VariationAvailabilityConfigView.as_view(),
        name="variation_availability_config",
    ),
    path(
        "availability/<int:product_id>/",
        VariationAvailabilityConfigView.as_view(),
        name="variation_availability_config",
    ),
    path("variations/", VariationConfigView.as_view(), name="variation_config"),
    path(
        "variations/<int:product_id>/",
        VariationConfigView.as_view(),
        name="variation_config",
    ),
    path(
        "history/",
        VariationAvailabilityEventListView.as_view(),
        name="variationavailabilityeventlist",
    ),
    path(
        "count/", variation_count_overview_view, name="variation_count_overview"
    ),
    path(
        "count/success",
        VariationCountSuccessView.as_view(),
        name="variation_count_success",
    ),
    path("count/<slug:code>/", variation_count_view, name="variationcount"),
    path("count/<slug:code>/<int:variation_id>", variation_count_view, name="variationcount"),
]
