from rest_framework.generics import ListCreateAPIView
from mydemo.serializer import UserSerializer, StudentSerializer
from mydemo.models import User, Student

class UserListCreateAPIView(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class StudentListCreateAPIView(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer