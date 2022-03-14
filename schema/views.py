from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import json

from pyodbc import connect
from .forms import IOTDeviceFormWithDynamicParams, JSONSchemaCreatorForm, schema_draft7_template
from .models import IOTDevice, JSONSchema
# Create your views here.
def schema_creator(request):
    if request.method == "GET":
        form = IOTDeviceFormWithDynamicParams(prefix="iotdev")
        return render(request, "schema/schema_creator.html", context={"form" : form})
    else:
        form = IOTDeviceFormWithDynamicParams(request.POST, prefix="iotdev")

        if form.is_valid():

            iot_device = form.save(commit=False)

            names = request.POST.getlist('name')
            types = request.POST.getlist('data_type')
            is_requireds = request.POST.getlist('is_required')
            json_schema = json.loads(schema_draft7_template)

            for name, data_type in zip(names, types):
                json_schema['properties'].update(
                    {
                        name : {
                            'type' : data_type
                            }
                    }
                )
                if name in is_requireds:
                    json_schema['required'].append(name)
                    # is_requireds.remove(name)
            json_schema_str=  json.dumps(json_schema, indent=4)

            iot_device.dynamic_schema = json_schema
            iot_device.save()

            return redirect("schema:preview", pk=iot_device.pk)
            # return HttpResponse(
            #     content=json_schema_str,
            #     content_type="text/json"
            # )

def iot_device_preview(request, pk):
    if request.method == "GET":
        instance = IOTDevice.objects.get(pk=pk)
        form = IOTDeviceFormWithDynamicParams(instance=instance)
        form._generate_dynamicfields(instance.dynamic_schema)
        
        context = {
            'form' : form,
            'iotdevice': instance,
        }

        return render(request,'schema/iotdynamic_input.html', context)

def preview_schema(request, pk):
    if request.method == "GET":
        instance = IOTDevice.objects.get(pk=pk)
        schema = json.dumps(instance.dynamic_schema, indent=4)

        return HttpResponse(
            content=schema,
            content_type="application/json",
        )