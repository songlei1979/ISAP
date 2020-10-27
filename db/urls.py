from rest_framework import routers
from .api import ServiceLevelViewSet, DivisionViewSet, DIVAndLOCViewSet, LocationViewSet, BuildingViewSet, DeskViewSet, EmpAndDeskViewSet, EmployeeViewSet, EquipmentViewSet, EquipmentTypeViewSet

router = routers.DefaultRouter()
router.register('api/service_level', ServiceLevelViewSet,'Service Levels')
router.register('api/divisions', DivisionViewSet,'Divisions')
router.register('api/divisionAndLocations', DIVAndLOCViewSet,'Division and Location')
router.register('api/locations', LocationViewSet,'Location')
router.register('api/buildings', BuildingViewSet,'Buildings')
router.register('api/desks', DeskViewSet,'Desks')
router.register('api/employeeAndDesk', EmpAndDeskViewSet,'Employee and Desk')
router.register('api/employees', EmployeeViewSet,'Employees')
router.register('api/equipment', EquipmentViewSet,'Equipments')
router.register('api/equipmentTypes', EquipmentTypeViewSet,'Equipment Types')


urlpatterns = router.urls