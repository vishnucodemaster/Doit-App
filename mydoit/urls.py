from django.urls import path
from mydoit.views import home,add_doit,delete_doit,edit_doit



urlpatterns = [
    path('', home, name='home'),
    path('add_doit/', add_doit, name='add_doit'),
    path('delete_doit/<int:doit_id>', delete_doit, name='delete_doit'),
    path('edit_doit/<int:doit_id>', edit_doit, name='edit_doit'),
]