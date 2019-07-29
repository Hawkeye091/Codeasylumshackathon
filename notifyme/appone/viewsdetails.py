from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView


from .serializers import DetailsSerializer

from .models import Detailsdb

# Create your views here.
class get_delete_update_details(RetrieveUpdateDestroyAPIView):
	serializer_class=DetailsSerializer

	def get_queryset(self,pk):
		try:
			details=Detailsdb.objects.get(pk=pk)
		except Detailsdb.DoesNotExist:
			content={
				'status':'Not Found'
			}	
			return Response(content,status=status.HTTP_404_NOT_FOUND)
		return details	

	def get(self,request,pk):
		details=self.get_queryset(pk)
		serializer=DetailsSerializer(details)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def put(self,request,pk):
		details=self.get_queryset(pk)
		serializer=DetailsSerializer(details,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)		

	def delete(self,request,pk):
		details=self.get_queryset(pk)
		details.delete()
		content={
		'status':'Item Deleted'
		}
		return Response(content,status=status.HTTP_204_NO_CONTENT)


class get_post_details(ListCreateAPIView):
	serializer_class = DetailsSerializer
	def get(self,request):
		details = Detailsdb.objects.all()
		serializer = DetailsSerializer(details, many=True)
		return Response(serializer.data)
	def post(self,request):
		serializer = DetailsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
