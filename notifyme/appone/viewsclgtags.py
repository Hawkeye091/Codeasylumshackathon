from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView

from .serializers import ClgtagsSerializer

from .models import Clgtagsdb

# Create your views here.
class get_delete_update_clgtags(RetrieveUpdateDestroyAPIView):
	serializer_class=ClgtagsSerializer

	def get_queryset(self,pk):
		try:
			clgtags=Clgtagsdb.objects.get(pk=pk)
		except Clgtagsdb.DoesNotExist:
			content={
				'status':'Not Found'
			}	
			return Response(content,status=status.HTTP_404_NOT_FOUND)
		return clgtags	

	def get(self,request,pk):
		clgtags=self.get_queryset(pk)
		serializer=ClgtagsSerializer(clgtags)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def put(self,request,pk):
		clgtags=self.get_queryset(pk)
		serializer=ClgtagsSerializer(clgtags,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)		

	def delete(self,request,pk):
		clgtags=self.get_queryset(pk)
		clgtags.delete()
		content={
		'status':'Item Deleted'
		}
		return Response(content,status=status.HTTP_204_NO_CONTENT)


class get_post_clgtags(ListCreateAPIView):
	serializer_class = ClgtagsSerializer
	def get(self,request):
		clgtags = Clgtagsdb.objects.all()
		serializer = ClgtagsSerializer(clgtags, many=True)
		return Response(serializer.data)
	def post(self,request):
		serializer = ClgtagsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
