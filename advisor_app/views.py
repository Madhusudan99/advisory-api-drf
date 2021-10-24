import re
from rest_framework import serializers, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, AdvisorSerializer, RegisterSerializer, BookingSerializer
from .models import Advisor, Booking

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

import json

@api_view(['GET', 'POST'])
# @permission_classes([permissions.IsAuthenticated])
def advisor_list(request):
    if request.method == 'GET':
        advisors = Advisor.objects.all()
        serializer = AdvisorSerializer(advisors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdvisorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def book_advisor(request, user_id, advisor_id):
    # print(user_id)
    # print(advisor_id)
    # print(request.data['booking_time'])
    book_obj = {
        'user': user_id,
        'booking_time': request.data['booking_time'],
        'advisor': advisor_id
    }
    serializer = BookingSerializer(data=book_obj)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_booked_calls(request, user_id):
    # print(user_id)
    bookings = Booking.objects.filter(user=user_id)
    arr = []
    for i in bookings:
        result = {}
        result['Advisor Name'] = i.advisor.advisor_name
        result['Advisor Profile Pic'] = i.advisor.advisor_photo_url
        result['Advisor Id'] = i.advisor.id
        result['Booking time'] = i.booking_time
        result['Booking id'] = i.id
        # arr.append(json.dumps(result, default=str))
        arr.append(result)
    return Response(arr, status=status.HTTP_200_OK)    

@api_view(['GET'])
def get_list_of_advisors(request, user_id):
    advisors = Advisor.objects.values()
    return Response(advisors, status=status.HTTP_200_OK)
    

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer