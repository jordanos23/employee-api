from django.urls import path

from .views import EmployeeDetail, EmployeeList

urlpatterns = [
    path('', EmployeeList.as_view(), name="list-create"),
    path('<int:pk>', EmployeeDetail.as_view(), name="get-update-delete"),
]
