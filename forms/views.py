# Create your views here.
from django.contrib import auth, messages
from django.core import urlresolvers
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from models import CocoUser, FullDownloadStats
from excel_views import get_project_excel_sheet, MonthYear
from openpyxl.writer.excel import save_virtual_workbook

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
        else:
            return HttpResponse("0")
    else:
        return HttpResponse("0")
    return HttpResponse("1")

def logout(request):
    auth.logout(request)    
    return HttpResponse("1")

def coco_v2(request):
    return render(request,'dashboard.html')

def html_decorator(func):
    """
    This decorator wraps the output in html.
    (From http://stackoverflow.com/a/14647943)
    """
 
    def _decorated(*args, **kwargs):
        response = func(*args, **kwargs)
 
        wrapped = ("<html><body>",
                   response.content,
                   "</body></html>")
 
        return HttpResponse(wrapped)
 
    return _decorated
 
@html_decorator
def debug(request):
    """
    Debug endpoint that uses the html_decorator,
    """
    path = request.META.get("PATH_INFO")
    api_url = path.replace("debug/", "")
 
    view = urlresolvers.resolve(api_url)
 
    accept = request.META.get("HTTP_ACCEPT")
    accept += ",application/json"
    request.META["HTTP_ACCEPT"] = accept
 
    res = view.func(request, **view.kwargs)
    return HttpResponse(res._container)

def reset_database_check(request):
    if not(request.user):
        return HttpResponse("0")
    cocouser = CocoUser.objects.get(user = request.user)    
    if not(cocouser and cocouser.time_modified):
        return HttpResponse("0")
    lastdownloadtime = request.GET["lastdownloadtimestamp"]
    lastdownloadtimestamp = datetime.strptime(lastdownloadtime, '%Y-%m-%dT%H:%M:%S.%f')
    
    if lastdownloadtimestamp<=cocouser.time_modified.replace(tzinfo=None):
        return HttpResponse("1")
    return HttpResponse("0")   

def record_full_download_time(request):
    if not(request.user and request.POST["start_time"] and request.POST["end_time"]):
        return HttpResponse("0")
    stat = FullDownloadStats(user = request.user, start_time = request.POST["start_time"], end_time = request.POST["end_time"])
    stat.save()
    return HttpResponse("1") 

def export_to_excel(request):
    if request.method == 'POST':
        query_month = request.POST.get('month','').encode('ascii','ignore') 
        query_year = int(request.POST.get('year','').encode('ascii','ignore'))
        month_year = MonthYear(query_month, query_year)
        
        if month_year.validate_date() == False:
            messages.error(request, 'Data not available for selected month and year')
            return render(request,'excel.html')
        
        wb = get_project_excel_sheet(month_year)
        response = HttpResponse(save_virtual_workbook(wb), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Analytics.xlsx"'
        return response
    else:
        return render(request,'excel.html')