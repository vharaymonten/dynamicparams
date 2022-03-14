from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import DeviceCheckIn, IOTDevice
import jsonschema
class CheckInSerializers(serializers.ModelSerializer):
    iotdevice_name = serializers.CharField()
    
    class Meta:
        model = DeviceCheckIn
        exclude = ('iot_device', )
    
    def validate_dynamic_parameters(self, data):
        iotdevice_name = self.initial_data['iotdevice_name']
        try:
            iot_device = IOTDevice.objects.get(name=iotdevice_name)

        except IOTDevice.DoesNotExist:
            raise ValidationError(
                detail="IOT Device Name Does Exist", 
                code=400)
        schema = iot_device.dynamic_schema
        parameters = data

            # if no exception raised then the validation is succsesed
        validated = True
        try:
            jsonschema.validate(
            instance=parameters,
            schema=schema
            )
        except jsonschema.ValidationError:
            raise ValidationError(
                detail="Dynamic Parameters does not meet the Schmea requiremetns",
                code=400,
            )
            
        
    # def validate(self, rs):
    #     return super().validate(attrs)