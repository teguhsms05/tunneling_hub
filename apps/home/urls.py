




from django.urls import path, re_path
from . import views

app_name = 'home'

urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    path('register-cpanel/', views.register_cpanel, name='register_cpanel'),
    path('delete-cpanel/<int:task_id>', views.delete_cpanel, name='delete_cpanel'),
    path('update-cpanel/<int:task_id>', views.update_cpanel, name='update_cpanel'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
