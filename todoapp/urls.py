from django.urls import path
from .views import tasklist
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', tasklist, name='tasks'),
    path('gettask', views.get_tasks),
    path('createtask', views.create_task),
    path('updatetask/<str:task_title>', views.update_task),
    path('deletetask/<str:task_title>', views.delete_task),
    path('gettask/<str:task_category>', views.filter_tasks),
]


urlpatterns = format_suffix_patterns(urlpatterns)
