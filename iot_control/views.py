from django.http import HttpResponse
from django.shortcuts import render
from .services import IOTService as service

# Create your views here.
def iot(request) -> HttpResponse:
    if request.method == "POST":
        if "create_program" in request.POST:
            service.create_empty_program(request.POST.get("program_name"))

    return render(
        request=request,
        template_name="iot_control/iot.html",
        context={
            "results": service.get_programs
        }
    )


def modify_program(request, program_id: str) -> HttpResponse:
    if request.method == 'POST':
        service.create_message(
            id=request.POST.get("device_name"),
            msg=request.POST.get("message_type"),
            data=request.POST.get("message_text"),
            program_id=program_id
        )
    result = service.get_programs()[program_id]
    return render(
        request=request,
        template_name="iot_control/create_program.html",
        context={
            "results": result,
            "name": program_id
        }
    )


def run_program(request) -> HttpResponse:
    prg_type = ""
    if request.method == "POST":
        prg_type = request.POST.get("program_type")
    if prg_type:
        result = service.run_program(prg_type)
    else:
        result = ["No program selected"]
    return render(
        request=request,
        template_name="iot_control/run_program.html",
        context={
            "results": service.get_programs(),
            "running": result
        }
    )
