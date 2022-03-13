from django.shortcuts import render

from .forms import JSONSchemaCreatorForm
# Create your views here.
def schema_creator(request):
    if request.method == "GET":
        form = JSONSchemaCreatorForm()
        return render(request, "schema_creator.html", {"form" : form})
    
