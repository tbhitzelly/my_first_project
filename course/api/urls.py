from django.urls import path, include
from course.api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('branches', views.BranchViewSet)
router.register('groups', views.GroupViewSet)
router.register('students', views.StudentViewSet)
router.register('course', views.CourseViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/branches/', views.BranchListView.as_view(), name='branches'),
    # path('v1/branches/<int:pk>/', views.BranchDetailView.as_view(), name='branch_detail'),
    # path('v1/groups/', views.GroupListView.as_view(), name='groups'),
    # path('v1/groups/<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),
    # path('v1/students/', views.StudentListView.as_view(), name='students'),
    # path('v1/students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
]