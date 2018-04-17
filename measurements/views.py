from django.http import JsonResponse
<<<<<<< HEAD
from rest_framework.views import APIView

from measurements.models import Measurement
from measurements.serializers import MeasurementSerializer


def filter_measurements(request, serializer_class, personal=True):
    measurements = Measurement.objects.all()

    if personal:
        measurements = Measurement.objects.filter(activity__participation__user=request.user.id)

    project = request.GET.get('project', None)
    if (project is not None) and (int(project) >= 0):
        measurements = measurements.filter(activity__participation__project_id=project)

    user = request.GET.get('user', None)
    if (user is not None) and (int(user) >= 0):
        measurements = measurements.filter(activity__participation__user_id=user)

    group = request.GET.get('group', None)
    if (group is not None) and (int(group) >= 0):
        measurements = measurements.filter(activity__entity__group_id=group)

    serializer = serializer_class(measurements, many=True)
    resp = {'measurements': serializer.data}
    return JsonResponse(resp)
=======
from measurements.models import Measurement
from measurements.serializers import MeasurementSerializer

from rest_framework.views import APIView
>>>>>>> b08e6a3e8b2c2dd9bc6e05534b8e9593d0bb7dab


class MeasurementsList(APIView):
    """
<<<<<<< HEAD
    List filtered measurements
    """

    def get(self, request, format=None):
        return filter_measurements(request, MeasurementSerializer)
=======
    List all measurements
    """

    def get(self, request, format=None):
        measurements = Measurement.objects.filter(activity__participation__user=request.user.id)
        serializer = MeasurementSerializer(measurements, many=True)
        resp = {'measurements': (serializer.data)}
        return JsonResponse(resp)
>>>>>>> b08e6a3e8b2c2dd9bc6e05534b8e9593d0bb7dab
