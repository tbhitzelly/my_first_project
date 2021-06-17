from django.urls import path
from course import views
urlpatterns = [
    path('', views.my_main_page, name='my_main_page'),
    path('branches/', views.branches_list, name='branches_list'),
    path('branches/<int:branch_id>/', views.branch_detail, name='branch_detail'),
    path('branches/create/', views.branch_create, name='branch_create'),
    path('branches/<int:branch_id>/edit/', views.branch_edit, name='branch_edit'),
    path('branches/<int:branch_id>/delete/', views.branch_delete, name='branch_delete'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('groups/create/',views.group_create, name='group_create'),
    path('groups/<int:group_id>/edit/', views.group_edit, name='group_edit'),
    path('group/<int:group_id>/delete/', views.group_delete, name='group_delete'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:student_id>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:student_id>/delete/', views.student_delete, name='student_delete'),
]