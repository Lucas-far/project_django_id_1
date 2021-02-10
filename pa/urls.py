

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('signup', sign_up, name='signup'),
    path('signin', sign_in, name='signin'),
    path('signout', sign_out, name='signout'),
    path('mytasks', TasksListView.as_view(), name='mytasks'),
    path('createtask', NewTaskCreateView.as_view(), name='createtask'),
    path('editar/<int:pk>', AlterTaskUpdateView.as_view(), name='updatetask'),
    path('deletar/<int:pk>', EraseTaskDeleteView.as_view(), name='deletetask'),
]
