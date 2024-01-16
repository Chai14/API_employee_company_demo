from rest_framework import serializers
from api.models import Company,Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__" #means i want to include all fields of company
class EmployeeSerializer(serializers.HyperlinkedModelSerializer): #model serializer taking because we are using models
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"
