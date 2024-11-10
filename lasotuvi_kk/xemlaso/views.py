import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from lasotuvi.DiaBan import diaBan
from lasotuvi.ThienBan import lapThienBan

from .utils import lapDiaBan


def api(request):
    now = datetime.datetime.now()
    hoTen = (request.GET.get('hoten'))
    dob = request.GET.get('date', '')
    namxem = int(request.GET.get('namxem', now.year))
    (ngaySinh, thangSinh, namSinh) = (int(i) for i in dob.lower().split('/')) if len(dob)>0 else (now.day, now.month, now.year)
    
    if namxem < namSinh:
        namxem = namSinh

    gioiTinh = 1 if request.GET.get('gioitinh') == 'nam' else -1
    gioSinh = int(request.GET.get('giosinh', 1))
    timeZone = int(request.GET.get('muigio', 7))
    duongLich = True
    db = lapDiaBan(diaBan, ngaySinh, thangSinh, namSinh, gioSinh,
                   gioiTinh, duongLich, timeZone, namxem=namxem)
    thienBan = lapThienBan(ngaySinh, thangSinh, namSinh,
                           gioSinh, gioiTinh, hoTen, db, namxem=namxem)
    laso = {
        'thienBan': thienBan,
        'thapNhiCung': db.thapNhiCung
    }
    my_return = (json.dumps(laso, default=lambda o: o.__dict__))
    return HttpResponse(my_return, content_type="application/json")


def lasotuvi_django_index(request):
    return render(request, 'index.html')