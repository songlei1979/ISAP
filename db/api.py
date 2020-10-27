from db.models import ServiceLevel, Division, DIVAndLOC, Building, Desk, EmpAndDesk, Employee, Equipment, EquipmentType, Location
from rest_framework import viewsets, permissions
from .serializers import ServiceLevelSerializer, DivisionSerializer, DIVAndLOCSerializer, BuildingSerializer, DeskSerializer, EmpAndDeskSerializer, EmployeeSerializer, EquipmentSerializer, EquipmentTypeSerializer, LocationSerializer


class ServiceLevelViewSet(viewsets.ModelViewSet):
    queryset = ServiceLevel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ServiceLevelSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LocationSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DivisionSerializer

class DIVAndLOCViewSet(viewsets.ModelViewSet):
    queryset = DIVAndLOC.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DIVAndLOCSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BuildingSerializer

class DeskViewSet(viewsets.ModelViewSet):
    queryset = Desk.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DeskSerializer

class EmpAndDeskViewSet(viewsets.ModelViewSet):
    queryset = EmpAndDesk.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmpAndDeskSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeeSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EquipmentSerializer

class EquipmentTypeViewSet(viewsets.ModelViewSet):
    queryset = EquipmentType.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EquipmentTypeSerializer