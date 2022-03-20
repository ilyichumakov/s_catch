from django.urls import path

from endpoints.views import project_list, group_list, endpoint_list, endpoint_detail

urlpatterns = [
    path('', project_list, name='project_list'),
    path('project_groups/<slug:project_name>/', group_list, name='project_group_list'),
    path('project_groups/<slug:project_name>/endpoints/<slug:group_name>/', endpoint_list, name='endpoint_list'),
    path('endpoint/<int:endpoint_id>/', endpoint_detail, name='endpoint_detail'),
]
