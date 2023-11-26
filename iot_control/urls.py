from django.urls import path
from . import views

app_name = "iot_control"

urlpatterns = [
    path("iot", views.iot, name="iot"),
    path("iot/run", views.run_program, name="run_program"),
    path("iot/<str:program_id>", views.modify_program, name="modify_program"),
]
