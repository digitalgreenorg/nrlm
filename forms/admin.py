
from django.contrib import admin
from forms.models import State,Project, Progress, Target, HrDetails, FinancialAssistance, CocoUser, ServerLog, ProgressTill13 #HrUnit, Category,

admin.site.register(State)
admin.site.register(Project)
admin.site.register(Progress)
admin.site.register(Target)
#admin.site.register(HrUnit)
admin.site.register(HrDetails)
admin.site.register(ProgressTill13)
admin.site.register(ServerLog)
admin.site.register(FinancialAssistance)
admin.site.register(CocoUser)