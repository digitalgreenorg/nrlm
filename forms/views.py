# Create your views here.
from django.contrib import auth
from django.core import urlresolvers
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from models import CocoUser, FullDownloadStats
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook
from openpyxl.style import Alignment, Border, Color, NumberFormat
from openpyxl.worksheet import RowDimension

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
    return render(request,'excel.html')

class CustomRowDimension(object):
    """Information about the display properties of a row."""
    __slots__ = ('row_index',
                 'height',
                 'visible',
                 'outline_level',
                 'collapsed',
                 'style_index',)

    def __init__(self, index=0):
        self.row_index = index
        self.height = 10
        self.visible = True
        self.outline_level = 0
        self.collapsed = False
        self.style_index = None

def excel_download(request):
    month=request.GET.get('month','')
    year=request.GET.get('year','')
    wb = Workbook()
    ws = wb.get_active_sheet()
    ws.title = "NRLP"
    
    c = ws.cell('A1')
    c.value = 'State'
    ws.merge_cells('A1:A2')
    c.style.alignment.wrap_text = True
    c.style.alignment.horizontal = Alignment.HORIZONTAL_CENTER
    c.style.alignment.vertical = Alignment.VERTICAL_CENTER
    c.style.borders.bottom.border_style = Border.BORDER_THIN
        
    c = ws.cell('B1')
    c.value = 'Total number of Blocks in which intensive strategy implementation is in progress'
    ws.row_dimensions[1].height = 35
    #ws.row_dimensions[2].height = 56
    ws.merge_cells('B1:F1')
    
    c = ws.cell('G1')
    c.value= 'Total number of Gram Panchayats in which intensive strategy implementation is in progress'
    ws.merge_cells('G1:K1')

    
    c = ws.cell('L1')
    c.value = 'Total number of villages in which intensive strategy implementation is in progress'
    ws.merge_cells('L1:P1')
    
    c = ws.cell('Q1')
    c.value = 'Number of New SHGs promoted with NRLM target households'
    ws.merge_cells('Q1:U1')
    
    c = ws.cell('V1')
    c.value = 'Number of Pre-NRLM SHGs brought into the NRLM fold after revival/training and strengthening'
    ws.merge_cells('V1:Z1')
    
    c = ws.cell('AA1')
    c.value = 'Total number of SHGs under NRLM fold in Intensive blocks (3.1 + 3.2)'
    ws.merge_cells('AA1:AE1')
    
    c = ws.cell('AF1')
    c.value = 'Number of SHGs provided basic SHG training at community level'
    ws.merge_cells('AF1:AJ1')
    
    c = ws.cell('AK1')
    c.value = 'Number of SHGs in which standard bookkeeping practices introduced'
    ws.merge_cells('AK1:AO1')
    
    c = ws.cell('AP1')
    c.value = 'Number of all SHGs following Pancha Sutras'
    ws.merge_cells('AP1:AT1')
    
    c = ws.cell('AU1')
    c.value = 'Number of SHGs bookkeepers identified and positioned after initial training'
    ws.merge_cells('AU1:AY1')
    
    c = ws.cell('AZ1')
    c.value = 'Number of internal CRPs identified and trained in the intensive blocks'
    ws.merge_cells('AZ1:BD1')
    
    c = ws.cell('BE1')
    c.value = 'Number of SHGs which are more than 3 month old'
    ws.merge_cells('BE1:BI1')
    
    c = ws.cell('BJ1')
    c.value = 'Number of 3 month old SHGs having bank accounts'
    ws.merge_cells('BJ1:BN1')
    
    c = ws.cell('BO1')
    c.value = 'Number of all 3 month old SHGs provided RF (5.5+5.6+5.7+5.8)'
    ws.merge_cells('BO1:BS1')
    
    c = ws.cell('BT1')
    c.value = 'Amount of RF provided to all SHGs  (Rs. In Lakhs) (5.10+5.11+5.12+5.13)'
    ws.merge_cells('BT1:BX1')
    
    c = ws.cell('BY1')
    c.value = 'Number of 6 month old SHGs in intensive blocks'
    ws.merge_cells('BY1:CC1')
    
    c = ws.cell('CD1')
    c.value = 'Number of SHGs which have prepared Micro Investment Plan (MIP)/Micro Credit Plan (MCP)'
    ws.merge_cells('CD1:CH1')
    
    c = ws.cell('CI1')
    c.value = 'Total Number of all SHGs provided CIF/VRF (6.5+6.6+6.7+6.8)'
    ws.merge_cells('CI1:CM1')
        
    c = ws.cell('CN1')
    c.value = 'Amount of CIF/VRF provided to all SHGs (in Rs.Lakhs) (6.10+6.11+6.12+6.13)'
    ws.merge_cells('CN1:CR1')
    
    c = ws.cell('CS1')
    c.value = 'Number of VOs formed'
    ws.merge_cells('CS1:CW1')
    
    c = ws.cell('CX1')
    c.value = 'Number of VOs provided training on basic VO management'
    ws.merge_cells('CX1:DB1')
    
    c = ws.cell('DC1')
    c.value = 'Number of VOs provided VRF (CIF)'
    ws.merge_cells('DC1:DG1')
    
    c = ws.cell('DH1')
    c.value = 'Amount of VRF(CIF) provided to VOs (in Rs.Lakhs)'
    ws.merge_cells('DH1:DL1')
    
    c = ws.cell('DM1')
    c.value = 'Number of CLFs formed'
    ws.merge_cells('DM1:DQ1')
    
    c = ws.cell('DR1')
    c.value = 'Number of CLFs provided CIF'
    ws.merge_cells('DR1:DV1')
    
    c = ws.cell('DW1')
    c.value = 'Amount of CIF provided to CLFs (in Rs.Lakhs)'
    ws.merge_cells('DW1:EA1')
    
    for i in xrange(1,131,5):
        c = ws.cell(row = 0, column = i)
        c.style.alignment.wrap_text = True
        c.style.alignment.horizontal = Alignment.HORIZONTAL_CENTER
        c.style.alignment.vertical = Alignment.VERTICAL_CENTER
        c.style.borders.left.border_style = Border.BORDER_THIN
        c.style.borders.bottom.border_style = Border.BORDER_THIN
        for j in range(1,5):
            c = ws.cell(row = 0, column = i+j)
            c.style.borders.bottom.border_style = Border.BORDER_THIN
    c.style.borders.right.border_style = Border.BORDER_THIN        
    
    for i in xrange(1,131,5):
        for j in range(0,5):
            c = ws.cell(row = 1, column = i+j)
            c.style.alignment.wrap_text = True
            c.style.alignment.horizontal = Alignment.HORIZONTAL_CENTER
            c.style.alignment.vertical = Alignment.VERTICAL_CENTER
            c.style.borders.left.border_style = Border.BORDER_THIN
            c.style.borders.bottom.border_style = Border.BORDER_THIN
            c.style.borders.top.border_style = Border.BORDER_THIN
            c.style.font.size = 8
            if j == 0:
                c.value = "Progress upto Mar'13"
            elif j == 1:
                c.value = "Annual Target \nFY 2013-14"
            elif j == 2:
                c.value = "Progress upto previous month since Apr'13"
            elif j == 3:
                c.value = "Progress during the Reporting Month"
            else:
                c.value = "Cummulative progress (since inception of NRLM)"
    c.style.borders.right.border_style = Border.BORDER_THIN
    
    response = HttpResponse(save_virtual_workbook(wb), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Analytics.xlsx"'
    return response