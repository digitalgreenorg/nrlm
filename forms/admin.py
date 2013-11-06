from django.contrib import admin
from forms.models import CocoUser, FinancialAssistance, HrDetails, Progress, ProgressTill13, Project, ServerLog, State, Target

class ProgressAdmin(admin.ModelAdmin):
    list_filter = ['year','month','project','state']
    search_fields = ['state__state_name','project__project_name','month','year']

class TargetAdmin(admin.ModelAdmin):
    list_filter = ['year','project','state']
    search_fields = ['state__state_name','project__project_name','year']

class HrDetailsAdmin(admin.ModelAdmin):
    list_filter = ['year','month','project','state']
    search_fields = ['state__state_name','project__project_name','month','year']

class ProgressTill13Admin(admin.ModelAdmin):
    list_filter = ['month','project','state']
    search_fields = ['state__state_name','project__project_name','month']

class FinancialAssistanceAdmin(admin.ModelAdmin):
    list_filter = ['year','month','project','state']
    search_fields = ['state__state_name','project__project_name','month','year']

admin.site.register(State)
admin.site.register(Project)
admin.site.register(Progress,ProgressAdmin)
admin.site.register(Target,TargetAdmin)
admin.site.register(HrDetails,HrDetailsAdmin)
admin.site.register(ProgressTill13,ProgressTill13Admin)
admin.site.register(ServerLog)
admin.site.register(FinancialAssistance,FinancialAssistanceAdmin)
admin.site.register(CocoUser)