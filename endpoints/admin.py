from django.contrib import admin
from endpoints.models import Project, EndPointGroup, Method, EndPoint


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(EndPointGroup)
class EndPointGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    readonly_fields = ['method_name']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(EndPoint)
class EndPointAdmin(admin.ModelAdmin):
    pass
