from rest_framework.routers import DefaultRouter

from tables.api.views import TableApiViewSet

router_table = DefaultRouter()

router_table.register(
    prefix='mesas', basename='mesas', viewset=TableApiViewSet
)