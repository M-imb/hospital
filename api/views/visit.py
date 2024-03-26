
from rest_framework import mixins, status
from rest_framework.response import Response

from api.mixins import HospitalGenericViewSet
from api.models import Visit
from api.serializers.patient import PatientListSerializer, PatientDetailedSerializer, PatientCreateOrUpdateSerializer
from api.serializers.visit import VisitCreateSerializer, VisitRatingSerializer


class VisitView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    lookup_field = 'id'

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_visit', ]
        elif self.action == 'create':
            self.action_permissions = ['add_visit', ]
        # elif self.action == 'update':
        #     self.action_permissions = ['change_visit', ]
        # elif self.action == 'destroy':
        #     self.action_permissions = ['delete_visit', ]
        else:
            self.action_permissions = []

    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        if self.action == 'retrieve':
            return PatientDetailedSerializer
        if self.action == 'create':
            return VisitCreateSerializer
        if self.action == 'update':
            return PatientCreateOrUpdateSerializer
        if self.action == 'set_rating':
            return VisitRatingSerializer

    def get_queryset(self):
        return Visit.objects.all()

    def set_rating(self, request, id):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)
