from rest_framework import status
from rest_framework.response import Response

from api.mixins import HospitalGenericViewSet
from api.models import Doctor, Patient
from api.service import get_upcoming_visits_count


class AnalyticsView(
    HospitalGenericViewSet
):
    def get_action_permissions(self):
        if self.action == 'get_analytics':
            self.action_permissions = []

    def get_analytics(self, request):
        response = {
            'patient_count': Doctor.objects.all().count(),
            'doctor_count': Patient.objects.all().count(),
            'visit_count': get_upcoming_visits_count()
        }
        return Response(status=status.HTTP_200_OK, data=response)