from django.conf.urls import patterns, include, url
from forms.api import StateResource, ProjectResource, ProgressResource, TargetResource, HrUnitResource, HrDetailsResource, CategoryResource, FinancialAssistanceResource
from forms.views import login, logout, debug, coco_v2
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#person_resource=PersonResource()
v1_api = Api(api_name='v1')
v1_api.register(ProjectResource())
v1_api.register(StateResource())
v1_api.register(ProgressResource())
v1_api.register(TargetResource())
v1_api.register(HrUnitResource())
v1_api.register(HrDetailsResource())
v1_api.register(CategoryResource())
v1_api.register(FinancialAssistanceResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Nrlm.views.home', name='home'),
    # url(r'^Nrlm/', include('Nrlm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
    (r'^coco/login/', login),
    (r'^coco/logout/', logout),
    (r'^forms/debug/', debug),
#    (r'^get_log/', send_updated_log),
    (r'^forms/$', coco_v2),
)
