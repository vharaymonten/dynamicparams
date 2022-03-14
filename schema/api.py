from django.http import JsonResponse
from rest_framework.views import APIView
from .serialiazers import CheckInSerializers

class IOTDeviceCheckInAPI(APIView):
    # Do not do authentication
    authentication_classes = []

    def post(self, request):
        checkin = CheckInSerializers(data=request.data, instance=None)
        checkin.is_valid(raise_exception=True)

        return JsonResponse(checkin.data)
