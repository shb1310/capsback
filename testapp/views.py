from django.shortcuts import render

# Create your views here.

from .serializers import AnsimSerializer, PublicPSerializer

from django.db.models import Q

from django.template.context_processors import csrf
from django.views.generic import ListView, TemplateView

from testapp.models import AnsimDataset as ans
from testapp.models import PublicPDataset as pp

from testapp.cftest import ClassTest as ct

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

import testapp.datainsert as di
import csv
		
class DataInsertView(APIView):
	def get(self,request):
		di.ansiminsert('testapp/ansim_20210903.csv')
		
class PDIView(APIView):
	def get(self,request):
		di.ppinsert('testapp/publicP_20210924.csv')
	
	
class TestView(APIView):	
	def get(self, request):
		queryset = ans.objects.filter(wardname__contains='은평구')			
		serializer = AnsimSerializer(queryset, many=True)
		return Response(serializer.data)
		
	
class AnsimView(APIView):
	
	def get(self, request):
		buff = ans.objects
		
		options = request.GET.get('options')		
		print(request)
		print('op:',options)
		
		if (options != None):			
			for i in options:
				if (i == 'g'):	#gps
					print("GPS")
					rlat = float(request.GET.get('lat'))
					rlon = float(request.GET.get('lon'))
					range = float(request.GET.get('range'))
					buff = buff.filter(lat__gt=rlat-range).\
									filter(lat__lt=rlat+range).\
									filter(lon__gt=rlon-range).\
									filter(lon__lt=rlon+range)
				
				elif (i == 's'):	#statename
					contents = request.GET.get('statename')
					buff = buff.filter(statename__contains=contents)	
				
				elif (i == 'w'):	#wardname
					contents = request.GET.get('wardname')
					buff = buff.filter(wardname__contains=contents)
				
				elif (i == 'p'):	#workplacename
					contents = request.GET.get('workplacename')
					buff = buff.filter(workplacename__contains=contents)
					
				elif (i == 'a'):	#address1
					contents = request.GET.get('address1')
					buff = buff.filter(address1__contains=contents)
				
				elif (i == 'A'):	#address2
					contents = request.GET.get('address2')
					buff = buff.filter(address2__contains=contents)

				elif (i == 'c'):	#category
					contents = request.GET.get('category')
					buff = buff.filter(category__contains=contents)
					
				elif (i == 'd'):	#categorydetail	
					print('categorydetail')	
					contents = request.GET.get('categorydetail')	
					buff = buff.filter(categorydetail=contents)
					
				print(i)
				
			buff = buff.filter(isansim='Y')

				
		else:
			buff = None
			
		queryset = buff				
		serializer = AnsimSerializer(queryset, many=True)
		return Response(serializer.data)


class PublicPView(APIView):
	def get(self, request):
		buff = pp.objects
		
		options = request.GET.get('options')		
		print(request)
		print('op:',options)
		
		if (options != None):			
			for i in options:
				if (i == 'g'):	#gps
					print("GPS")
					rlat = float(request.GET.get('lat'))
					rlon = float(request.GET.get('lon'))
					range = float(request.GET.get('range'))
					buff = buff.filter(lat__gt=rlat-range).\
									filter(lat__lt=rlat+range).\
									filter(lon__gt=rlon-range).\
									filter(lon__lt=rlon+range)
		
		else:
			buff = None			
			
		queryset = buff				
		serializer = PublicPSerializer(queryset, many=True)
		return Response(serializer.data)
		
class PtestView(APIView):
	def get(self, request):
		buff = pp.objects
		range = 0.05
		rlat = 37.48903538
		rlon = 126.720057
		buff = buff.filter(lat__gt=rlat-range).\
					filter(lat__lt=rlat+range).\
					filter(lon__gt=rlon-range).\
					filter(lon__lt=rlon+range)
			
			
		queryset = buff				
		serializer = PublicPSerializer(queryset, many=True)
		return Response(serializer.data)
	
	