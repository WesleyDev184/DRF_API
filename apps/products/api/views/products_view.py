from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializer import ProductSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

class ProductListApiView(GeneralListApiView):
    serializer_class = ProductSerializer

class ProductCreateApiView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'menssage': 'Produto criado'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        