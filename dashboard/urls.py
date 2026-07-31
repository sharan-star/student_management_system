from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
   path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
   path('login/',views.login,name='login'),
   path('register/',views.register,name='register'),
   path('add_student/',views.add_student,name='add_student'),
   path('view_student/',views.view_students,name='view_students'),
   path('update_student/<int:input_id>',views.update_student,name='update_student'),
    path('delete_student/<int:input_id>',views.delete_student,name='delete_student'),
    path('Drives/',views.drives,name='drives')
]
