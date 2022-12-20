from django.urls import path
from titles.views import TitleViewSet

urlpatterns = [
    path('register/', TitleViewSet.as_view({'post': 'create'})),
]