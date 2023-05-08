from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import StudentList, StudentDetail, ApiOverview


urlpatterns = [
    path('students/', StudentList.as_view(), name='task-list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='task-detail'),
    path('', ApiOverview.as_view() ,name = 'api-overview'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]