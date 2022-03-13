from django.db import models
import uuid
# Create your models here.


    

class JSONSchema(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    schema = models.JSONField(blank=False)

class IOTDevice(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255, blank=False)
    dynamic_schema = models.ForeignKey(JSONSchema, on_delete=models.SET_NULL, null=True)

class DeviceCheckIn(models.Model):
    iot_device = models.ForeignKey(IOTDevice, on_delete=models.SET_NULL, null=True)
    val_1 = models.IntegerField()
    val_2 = models.IntegerField()
    val_3 = models.IntegerField()
    val_4 = models.IntegerField()
    dynamic_params = models.JSONField()