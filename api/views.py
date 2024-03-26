# from api.models import Doctor, Patient
# from api.serializers import DoctorListSerializer, DoctorRetrieveSerializer, DoctorCreateSerializer, \
#     DoctorUpdateSerializer, PatientListSerializer
# from rest_framework import mixins, viewsets
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from api.permissions import DoctorAccessPermission
#
#
# class DoctorView(
#     viewsets.GenericViewSet,
#     mixins.ListModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     mixins.DestroyModelMixin,
#     ):
#
#     lookup_field = 'id'
#
#     # permission_classes = [IsAuthenticated, ]
#     permission_classes = [IsAuthenticated, DoctorAccessPermission]
#
#     def get_action_permissions(self):
#         if self.action in ('list', 'retrieve'):
#             self.get_action_permissions = ['view_doctor',]
#         elif self.action == 'list_patient':
#             self.get_action_permissions = ['view_patient', ]
#
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return DoctorListSerializer
#         if self.action == 'retrieve':
#             return DoctorRetrieveSerializer
#         if self.action == 'create':
#             return DoctorCreateSerializer
#         if self.action == 'update':
#             return DoctorUpdateSerializer
#         if self.action == 'list_patient':
#             return PatientListSerializer
#
#
#     def get_queryset(self):
#         if self.action == 'list_patient':
#             return Patient.objects.all()
#         return Doctor.objects.all()
#
#     def list_patient(self, request, id):
#         queryset = self.get.queryset().filter(visits__doctor_id=id).all()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(data=serializer.data)
#
#

