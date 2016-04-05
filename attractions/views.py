from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from attractions.serializers import AttractionsSerializer, AggregateAttractionSerialize
from django.core.cache import cache
import pdb
from datetime import datetime
from attractions.attractions_dao import AttractionsDao
from attractions.client_disney import ClientDisney
from app.utils import parse_date


@api_view(['GET'])
def get_attractions(request):
    """
    List all attractions
    
    ---
    nickname: Attractions
    responseMessages:
        - code: 200
          message: List Attractions
    """        
             
    value = cache.get('attractions')
    if not value:
          value = AttractionsDao.find_attractions()
          cache.set('attractions', value)      
    
    serializer = AttractionsSerializer(data = value, many=True)

    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_attractions_aggregate(request):
    """
    Get average wait time of attractions
    ---
    nickname: AttractionsAggregate
    parameters:
        - name: startdate
          type: string
          in: query
          format: date-time
        - name: enddate
          format: date-time
          in: query
          type: string
        - name: attractions
          in: query
          type: array           
    """        
    attractionsParam = request.GET.get('attractions')
    if ',' in attractionsParam:
        myListAttractions = attractionsParam.split(',')
    else:
        myListAttractions = request.GET.getlist('attractions')
    start_date = parse_date(request.GET.get('startdate'))
    end_date = parse_date(request.GET.get('enddate'))
    docs = AttractionsDao.find_aggregate_attractions_between_date(myListAttractions,start_date, end_date)
    serializer = AggregateAttractionSerialize(data = docs, many=True)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    else: 
        return Response(status=status.HTTP_400_BAD_REQUEST)

