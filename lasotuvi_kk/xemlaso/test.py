import datetime
import json
from utils import lapDiaBan
from lasotuvi.DiaBan import diaBan
from lasotuvi.ThienBan import lapThienBan

def api(hoten="haha", ngay=1, thang=1, nam=2004, gioi="nam", gio=1, zone=7):
    now = datetime.datetime.now()
    hoTen = (hoten)
    ngaySinh = int(ngay)
    thangSinh = int(thang)
    namSinh = int(nam)
    gioiTinh = 1 if gioi == 'nam' else -1
    gioSinh = int(gio)
    timeZone = int(zone)
    duongLich = False
    db = lapDiaBan(diaBan, ngaySinh, thangSinh, namSinh, gioSinh,
                   gioiTinh, duongLich, timeZone)
    thienBan = lapThienBan(ngaySinh, thangSinh, namSinh,
                           gioSinh, gioiTinh, hoTen, db)
    laso = {
        'thienBan': thienBan,
        'thapNhiCung': db.thapNhiCung
    }
    my_return = (json.dumps(laso, default=lambda o: o.__dict__))
    
    with open('test.json', 'w', encoding='utf8') as f:
        f.write(my_return.encode().decode("unicode-escape"))

    return my_return

print(api())
