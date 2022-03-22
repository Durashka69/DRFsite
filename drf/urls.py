from django.contrib import admin
from django.urls import path, include

from women.views import *
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet, basename='women')
# # print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    # path('api/v1/', include(router.urls)), #http://127.0.0.1:8000/api/v1/women/
    # path('api/v1/womenlist', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>', WomenViewSet.as_view({'put': 'update'})),
    # path('api/v1/womendetail/<int:pk>', WomenAPIDetailView.as_view())
]
