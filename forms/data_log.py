from datetime import datetime
from django.core import serializers
from django.db.models import get_model
from django.forms.models import model_to_dict
from django.http import HttpResponse
from models import User

class TimestampException(Exception):
    pass

class UserDoesNotExist(Exception):
    pass


def save_log(sender, **kwargs ):
    instance = kwargs["instance"]
    action  = kwargs["created"]
    sender = sender.__name__    # get the name of the table which sent the request
    model_dict = model_to_dict(instance)
    previous_time_stamp = get_latest_timestamp()
    try:
        user = User.objects.get(id = instance.user_modified_id) if instance.user_modified_id else User.objects.get(id = instance.user_created_id)
    except Exception, ex:
        user = None
    try:
        instance.get_state()
    except Exception as e:
        print type(e), e
    ServerLog = get_model('forms','ServerLog')
    log = ServerLog(state = instance.get_state(), user = user, action = action, entry_table = sender, 
                    model_id = instance.id)
    log.save()
    ###Raise an exception if timestamp of latest entry is less than the previously saved data timestamp
    if previous_time_stamp.replace(tzinfo=None) > log.timestamp:
        raise TimestampException('timestamp error: Latest entry data time created is less than previous data timecreated')
#    
def delete_log(sender, **kwargs ):
    instance = kwargs["instance"]
    sender = sender.__name__    # get the name of the table which sent the request
    user = None
    if instance.user_created_id:
        if instance.user_modified_id:
            user = User.objects.get(id = instance.user_modified_id) 
        else:
            user = User.objects.get(id = instance.user_created_id)
    try:
        ServerLog = get_model('forms','ServerLog')
        log = ServerLog(state = instance.get_state(), user = user, action = -1, entry_table = sender, model_id = instance.id)
        log.save()
    except Exception as ex:
        pass

def send_updated_log(request):
    timestamp = request.GET.get('timestamp', None)
    if timestamp:
        CocoUser = get_model('forms','CocoUser')
        CocoUserStates = get_model('forms','CocoUser_states')
        ServerLog = get_model('forms','ServerLog')
        try:
            coco_user = CocoUser.objects.get(user_id=request.user.id)
        except Exception as e:
            raise UserDoesNotExist('User with id: '+str(request.user.id) + 'does not exist')
        states = CocoUserStates.objects.filter(cocouser_id = coco_user.id).values_list('state_id', flat = True)
        rows = ServerLog.objects.filter(timestamp__gte = timestamp, state__in = states)
        if rows:
            data = serializers.serialize('json', rows, fields=('action','entry_table','model_id', 'timestamp'))
            return HttpResponse(data, mimetype="application/json")
    return HttpResponse("0")

def get_latest_timestamp():
    from models import ServerLog
    try:
        timestamp = ServerLog.objects.latest('id')
        return timestamp.timestamp
    except ServerLog.DoesNotExist:
        return datetime.utcnow()
