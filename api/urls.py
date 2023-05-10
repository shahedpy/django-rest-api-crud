from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import StudentList, StudentDetail, ApiOverview


urlpatterns = [
    path('', ApiOverview.as_view() ,name = 'api-overview'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('students/', StudentList.as_view(), name='students-list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
]