
from django.contrib import admin
from forms.models import State,Project, Progress, Target, HrUnits, HrDetails, Category, FinancialAssistance

admin.site.register(State)
admin.site.register(Project)
admin.site.register(Progress)
admin.site.register(Target)
admin.site.register(HrUnits)
admin.site.register(HrDetails)
admin.site.register(Category)
admin.site.register(FinancialAssistance)