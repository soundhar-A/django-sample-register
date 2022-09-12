from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Register
from .serializers import RegisterSerializer
# Create your views here.

class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer
    def get(self,request):
        register = Register.objects.all().values()
        return Response({"Message":"Register","Register":register})

    def post(self,request):
        print('Request data is :',request.data)
        serializer_obj = RegisterSerializer(data=request.data)
        if(serializer_obj.is_valid()):
            Register.objects.create(first_name=serializer_obj.data.get('first_name'),
                                    last_name=serializer_obj.data.get('last_name'),
                                    email = serializer_obj.data.get('email'),
                                    password = serializer_obj.data.get('password'),
                                    confirm_password = serializer_obj.data.get('confirm_password')
                                    )
            register = Register.objects.all().filter(first_name=request.data['first_name']).values()
            return Response({
                "Message":"News register Added","Register":register
            })