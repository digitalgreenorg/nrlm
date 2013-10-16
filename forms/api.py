
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from forms.models import State,Project, Progress, Target,  HrDetails, FinancialAssistance #,HrUnit, Category,

class StateResource(ModelResource):
    class Meta:
        queryset=State.objects.all()
        resource_name = 'State'
        always_return_data = True
        authorization= Authorization()
        
class ProjectResource(ModelResource):
    class Meta:
        queryset=Project.objects.all()
        resource_name = 'Project'
        always_return_data = True
        authorization= Authorization()

class BaseResource(ModelResource):
    
    def full_hydrate(self, bundle):
        bundle = super(BaseResource, self).full_hydrate(bundle)
        bundle.obj.user_modified_id = bundle.request.user.id
        return bundle
    
    def obj_create(self, bundle, **kwargs):
        """
        A ORM-specific implementation of ``obj_create``.
        """
        bundle.obj = self._meta.object_class()

        for key, value in kwargs.items():
            setattr(bundle.obj, key, value)

        self.authorized_create_detail(self.get_object_list(bundle.request), bundle)
        bundle = self.full_hydrate(bundle)
        bundle.obj.user_created_id = bundle.request.user.id
        return self.save(bundle)

def dict_to_foreign_uri(bundle, field_name, resource_name=None):
    if field_name == 'State':
        field_name = 'state_id'
    if field_name == 'Project':
        field_name = 'project_name'
    field_dict = bundle.data.get(field_name)
    print field_dict, field_name
    if field_dict:
        bundle.data[field_name] = "/api/v1/%s/%s/"%(resource_name if resource_name else field_name, 
                                                    str(field_dict))
    else:
        bundle.data[field_name] = None
    print bundle.data[field_name]
    return bundle

class ProgressResource(BaseResource):
    state=fields.ForeignKey(StateResource,'state',full=True)
    project=fields.ForeignKey(ProjectResource,'project',full=True)
    class Meta:
        queryset=Progress.objects.all()
        resource_name = 'Progress'
        authorization= Authorization()
        always_return_data = True
    #hydrate_state = partial(dict_to_foreign_uri, field_name = 'State', resource_name='State')
    #hydrate_project = partial(dict_to_foreign_uri, field_name = 'Project', resource_name = 'Project')

class TargetResource(BaseResource):
    state=fields.ForeignKey(StateResource,'state',full=True)
    project=fields.ForeignKey(ProjectResource,'project',full=True)
    class Meta:
        queryset=Target.objects.all()
        resource_name = 'Target'
        authorization= Authorization()
        always_return_data = True

"""class HrUnitResource(ModelResource):
    class Meta:
        queryset=HrUnit.objects.all()
        resource_name = 'HrUnit'
        authorization= Authorization()
        always_return_data = True"""

class HrDetailsResource(BaseResource):
    state=fields.ForeignKey(StateResource,'state',full=True)
    project=fields.ForeignKey(ProjectResource,'project',full=True)
    #hrunit=fields.ForeignKey(HrUnitResource,'hrunit',full=True)
    class Meta:
        queryset=HrDetails.objects.all()
        resource_name = 'HrDetails'
        authorization= Authorization()
        always_return_data = True
        
"""class CategoryResource(ModelResource):
    class Meta:
        queryset=Category.objects.all()
        resource_name = 'Category'
        always_return_data = True"""

class FinancialAssistanceResource(BaseResource):
    state=fields.ForeignKey(StateResource,'state',full=True)
    project=fields.ForeignKey(ProjectResource,'project',full=True)
    class Meta:
        queryset=FinancialAssistance.objects.all()
        resource_name = 'FinancialAssistance'
        authorization= Authorization()
        always_return_data = True