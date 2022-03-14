from random import choices
from tkinter.ttk import Style
from django import forms

from .models import IOTDevice, JSONSchema

import jsonschema

DRAFT7_DATATYPES = (
    ("string", "String"), # python str
    ("number", "Number"), # python int/float
    # ("object", "Dict"), # Python dictionary
    # ("array", "Array"), #python list 
    ("boolean", "Boolean"), # python bool
    ("null", "Null") # python 
)

DATATPES_TO_FIELDS_MAP = {
    'string' : forms.CharField,
    'number' : forms.FloatField,
    'boolean' : forms.BooleanField,
}


schema_draft7_template = """
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "type" : "object",
    "title" : "Dynamic Parameter Schema",
    "description" : "This schema is used as a template for  making dynamic parameters",
    "required" : [],
    "properties" : {
    }

}"""
class JSONSchemaCreatorForm(forms.Form):
    data_type = forms.ChoiceField(
        choices=DRAFT7_DATATYPES,
        widget=forms.Select(
            attrs={
                'class' : 'form-control form-control-sm'
            }
        ))
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control form-control-sm',
                'onchange' : "setValueForCheckbox(event)"    
                }
            )
        )
    is_required = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class' : 'form-check-input form-check-sm',
                'style' : 'max-width : 32px',
            }
        )
    )
    # validators = forms.JSONField()

class IOTDeviceFormWithDynamicParams(forms.ModelForm):
    # name = forms.CharField(required='name')
    name = forms.CharField(required=True, label="Device Name", widget=forms.TextInput(
        attrs={
            'class' : 'form-control form-control-sm'
        }
    ))
    class Meta:
        model = IOTDevice
        fields = ('name', )
    def _generate_dynamicfields(self, schema):
        if 'properties' in schema:
            properties = schema.get('properties')
            for prop in properties:
                data_type = properties[prop].get('type')
                custom_field = DATATPES_TO_FIELDS_MAP.get(data_type)
                self.fields[prop] = custom_field()



