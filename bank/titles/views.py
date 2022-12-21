from rest_framework.viewsets import ModelViewSet, ViewSet
from titles.models import Title
from titles.serializer import TitleSerializer
from rest_framework.response import Response
from rest_framework import status
import json

class TitleViewSet(ModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
        
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        
        filter_by_date = self.request.GET.get('creation_date')
        filter_by_title_id = self.request.GET.get('title_id')

        if filter_by_title_id:
            fee_paid = request.data['fee_paid']
            Title.objects.filter(title_id=filter_by_title_id).update(fee_paid=fee_paid)
        elif filter_by_date:
            new_date = request.data['creation_date']
            Title.objects.filter(creation_date=filter_by_date).update(creation_date=new_date)

        return Response(status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        filter_by_title_id = self.request.GET.get('title_id')
        Title.objects.filter(title_id=filter_by_title_id).delete()
        self.queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TitleQuantityViewSet(ViewSet):
    
    def list(self, request, *args, **kwargs):
        return Response(json.dumps({'quantity': Title.objects.all().count()}), status=status.HTTP_200_OK)
 
