from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from women.serializers import *
from .models import *


class WomenAPIView(APIView):
    def get(self, request):
        queryset = Women.objects.all()
        return Response({'posts': WomenSerlializer(queryset, many=True).data})

    def post(self, request):
        serializer = WomenSerlializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_post = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': WomenSerlializer(new_post).data})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
