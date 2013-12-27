from django.conf.urls import patterns, include, url
from forms.api import StateResource, ProjectResource, ProgressResource, TargetResource, HrDetailsResource, FinancialAssistanceResource, ProgressTill13Resource #,HrUnitResource, CategoryResource,  
from forms.views import excel_download, export_to_excel, login, logout, debug, coco_v2, reset_database_check, record_full_download_time
from tastypie.api import Api
from forms.data_log import send_updated_log
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#person_resource=PersonResource()
v1_api = Api(api_name='v1')
v1_api.register(ProjectResource())
v1_api.register(StateResource())
v1_api.register(ProgressResource())
v1_api.register(TargetResource())
#v1_api.register(HrUnitResource())
v1_api.register(HrDetailsResource())
v1_api.register(ProgressTill13Resource())
v1_api.register(FinancialAssistanceResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Nrlm.views.home', name='home'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
    (r'^coco/login/', login),
    (r'^coco/logout/', logout),
    (r'^coco/reset_database_check/', reset_database_check),
    (r'^coco/record_full_download_time/', record_full_download_time),
    (r'^forms/debug/', debug),
#    (r'^get_log/', send_updated_log),
    (r'^forms/$', coco_v2),
    url(r'^forms/faq/$', direct_to_template, {'template': 'faq.html'}, name="faq"),
    (r'^get_log/?$', send_updated_log),
    (r'^export/$', export_to_excel),
    (r'^download_excel/$', excel_download),
)
