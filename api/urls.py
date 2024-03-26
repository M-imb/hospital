from django.urls import path
from api.views import DoctorView, PatientView, VisitView, AnalyticsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# from rest_framework.authtoken import views
# from .views import ItemListCreateView, DoctorView

urlpatterns = [
    # path('item/', ItemListCreateView.as_view()),
    # path('item/<int:pk>/', ItemListCreateView.as_view({'get': 'get_item_by_id'})),
    # path('item/create/', ItemListCreateView.as_view({'post': 'create_item'})),
    path('doctor/', DoctorView.as_view({'get': 'list', 'post': 'create'})),
    path('doctor/<int:id>/', DoctorView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('doctor/<int:id>/patient/', DoctorView.as_view({'get': 'list_patient'})),
    path('visit/', VisitView.as_view({'post': 'create'})),
    path('visit/<int:id>/rating', VisitView.as_view({'put': 'set_rating'})),
    path('analytics/', AnalyticsView.as_view({'get': 'get_analytics'})),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]