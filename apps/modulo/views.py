from rest_framework.viewsets import ModelViewSet
from .serializers import ModuloSerializer


class ModuloViewSet(ModelViewSet):
    serializer_class = ModuloSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.serializer_class.Meta.model.objects.all()
        
        return self.serializer_class.Meta.model.objects.filter(id=pk).first()