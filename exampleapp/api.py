from tastypie.resources import ModelResource
from exampleapp.models import Persons , State
from tastypie.authorization import Authorization
from tastypie import fields

class StateResource(ModelResource):
    class Meta:
        queryset=State.objects.all()
        resource_name = 'State'
        authorization= Authorization()
        always_return_data = True
        
class PersonResource(ModelResource):
    state = fields.ForeignKey(StateResource,'state')
    class Meta:
        queryset=Persons.objects.all()
        resource_name = 'Persons'
        authorization= Authorization()
        always_return_data = True