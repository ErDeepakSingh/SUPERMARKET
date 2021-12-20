
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from . import models


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    subcategory = serializers.CharField(source='subcategory.name')
    class Meta:
        model = models.Item
        fields = ['name','category','subcategory','amount']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"Fail": "blablal"}, status=status.HTTP_400_BAD_REQUEST)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
        return Response({"Success": "msb blablabla"}, status=status.HTTP_201_CREATED, headers=headers)

class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ['name','category','subcategory','amount']