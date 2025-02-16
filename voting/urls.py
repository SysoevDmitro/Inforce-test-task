from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (RestaurantViewSet,
                    MenuViewSet,
                    VoteViewSet,
                    CurrentDayMenuView,
                    CurrentDayResultsView)

router = DefaultRouter()
router.register(r"restaurants", RestaurantViewSet)
router.register(r"menus", MenuViewSet, basename="menus")
router.register(r"votes", VoteViewSet)
router.register(r"today", CurrentDayMenuView, basename="menus-today")

urlpatterns = [
    path("", include(router.urls)),
    path("menus/today/results/", CurrentDayResultsView.as_view(), name="current-day-results"),
]

app_name = "voting"
