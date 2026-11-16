from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from employeeApp.serializers import EmployeeSerializer,TaskSerializer
from employeeApp.models import EmpolyeeModel,TaskModel
from rest_framework import authentication,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView


# Create your views here.
class EmployeeCreateListView(CreateAPIView,ListAPIView):
    serializer_class=EmployeeSerializer
    queryset=EmpolyeeModel.objects.all()
    
class EmployeeRetrieveUpdateDeleteView(RetrieveAPIView,ListAPIView,DestroyAPIView):
    serializer_class=EmployeeSerializer
    queryset=EmpolyeeModel.objects.all()

    
class CreateListTask(CreateAPIView,ListAPIView):
    serializer_class=TaskSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        return serializer.save()
    
    def get_queryset(self):
        return TaskModel.objects.filter(owner=self.request.empolyee)
    filter_backends=[
        DjangoFilterBackend,
        Searchfilter
    ]
    filterset_fields=["status"]
    
class RetrieveUpdateDeleteview(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=TaskSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset=TaskModel.objects.all()   
    lookup_url_kwarg="id"
