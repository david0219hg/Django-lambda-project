from rest_framework.viewsets import ModelViewSet
from titles.serializer import TitleSerializer
from rest_framework.response import Response
from rest_framework import status

class TitleViewSet(ModelViewSet):
    serializer_class = TitleSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)