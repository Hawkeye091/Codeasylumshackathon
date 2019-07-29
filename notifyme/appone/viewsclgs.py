from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView

from .serializers import ClgsSerializer

from .models import Clgsdb

# Create your views here.
class get_delete_update_clgs(RetrieveUpdateDestroyAPIView):
	serializer_class=ClgsSerializer

	def get_queryset(self,pk):
		try:
			clgs=Clgsdb.objects.get(pk=pk)
		except Clgsdb.DoesNotExist:
			content={
				'status':'Not Found'
			}	
			return Response(content,status=status.HTTP_404_NOT_FOUND)
		return clgs	

	def get(self,request,pk):
		clgs=self.get_queryset(pk)
		serializer=ClgsSerializer(clgs)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def put(self,request,pk):
		clgs=self.get_queryset(pk)
		serializer=ClgsSerializer(clgs,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)		

	def delete(self,request,pk):
		clgs=self.get_queryset(pk)
		clgs.delete()
		content={
		'status':'Item Deleted'
		}
		return Response(content,status=status.HTTP_204_NO_CONTENT)


class get_post_clgs(ListCreateAPIView):
	serializer_class = ClgsSerializer
	def get(self,request):
		clgs = Clgsdb.objects.all()
		serializer = ClgsSerializer(clgs, many=True)
		return Response(serializer.data)
	def post(self,request):
		serializer = ClgsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
