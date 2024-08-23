from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage
from .models import MenWear
from .serializers import MenWearSerializers
from rest_framework.views import APIView

class ClothListView(APIView):
    '''for sending linst of tee shirts to the '''
    def get(self,request):
        perpage = request.query_params.get('perpage',default = 8)
        page = request.query_params.get('page',default = 1)
        items = MenWear.objects.all()
        paginator =  Paginator(items,per_page=perpage)
        try:
            items =paginator.page(number=page)
        except EmptyPage:
            items = []
        serialized_item = MenWearSerializers(items,many = True)
        return Response(serialized_item.data)
    def post(self,request):
        return Response({
            "status" : "403",
            "operation":"not allowed"
        },status=status.HTTP_403_FORBIDDEN)
    def delete(self,request):
        return Response({
            "status" : "403",
            "operation":"not allowed"
        },status=status.HTTP_403_FORBIDDEN)
    def put(self,request):
        return Response({
            "status" : "403",
            "operation":"not allowed"
        },status=status.HTTP_403_FORBIDDEN)
    
class ProductView(APIView):
    def get(self,request,id='',fit=''):
        if not id or not fit:
            return Response({"code":404,
                             "status":"notfound"
                             },status=status.HTTP_404_NOT_FOUND
                             )
        
        item = MenWear.objects.get(id=id)
        serialized_data = MenWearSerializers(item)
        return Response(serialized_data.data)
    def post(self,request,id='',fit=''):
        return Response({
            "status" : "403",
            "operation":"not allowed"
        },status=status.HTTP_403_FORBIDDEN)
    def delete(self,request,id='',fit=''):
        return Response({
            "status" : "403",
            "operation":"not allowed"
        },status=status.HTTP_403_FORBIDDEN)
    def put(self,request,id='',fit=''):
        return Response({
            "status" : "403",
            "operation":"not allowed"
        },status=status.HTTP_403_FORBIDDEN)