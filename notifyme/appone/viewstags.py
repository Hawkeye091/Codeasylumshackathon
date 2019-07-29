from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView

from .serializers import TagsSerializer

from .models import Tagsdb

# Create your views here.
class get_delete_update_tags(RetrieveUpdateDestroyAPIView):
	serializer_class=TagsSerializer

	def get_queryset(self,pk):
		try:
			tags=Tagsdb.objects.get(pk=pk)
		except Tagsdb.DoesNotExist:
			content={
				'status':'Not Found'
			}	
			return Response(content,status=status.HTTP_404_NOT_FOUND)
		return tags	

	def get(self,request,pk):
		tags=self.get_queryset(pk)
		serializer=TagsSerializer(tags)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def put(self,request,pk):
		tags=self.get_queryset(pk)
		serializer=TagsSerializer(tags,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)		

	def delete(self,request,pk):
		tags=self.get_queryset(pk)
		tags.delete()
		content={
		'status':'Item Deleted'
		}
		return Response(content,status=status.HTTP_204_NO_CONTENT)


class get_post_tags(ListCreateAPIView):
	serializer_class = TagsSerializer
	def get(self,request):
		tags = Tagsdb.objects.all()
		serializer = TagsSerializer(tags, many=True)
		return Response(serializer.data)
	def post(self,request):
		serializer = TagsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
