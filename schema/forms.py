from random import choices
from django import forms

from .models import JSONSchema

import jsonschema

DRAFT7_DATATYPES = (
    ("string", "string"), # python str
    ("number", "number"), # python int/float
    ("object", "dict"), # Python dictionary
    ("array", "list"), #python list 
    ("boolean", "boolean"), # python bool
    ("null", "null") # python 
)
class JSONSchemaCreatorForm(forms.Form):
    data_type = forms.CharField(choices=DRAFT7_DATATYPES)
    name = forms.CharField(max_length=255)

