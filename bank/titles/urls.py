from django.urls import path
from titles.views import TitleViewSet, TitleQuantityViewSet

urlpatterns = [
    path(
        "",
        TitleViewSet.as_view(
            {"post": "create", "get": "list", "delete": "destroy", "put": "update"}
        ),
    ),
    path("quantity/", TitleQuantityViewSet.as_view({"get": "list"})),
]
