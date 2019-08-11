from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ShopifyOrder
from .serializers import ShopifyOrderSerializer

class ShopifyView(APIView):

    def get(self, request, format=None):
        sorder = ShopifyOrder.objects.all()
        serializer = ShopifyOrderSerializer(sorder, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShopifyOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)