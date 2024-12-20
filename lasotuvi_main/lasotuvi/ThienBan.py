# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""
from lasotuvi.AmDuong import (canChiNgay, diaChi, ngayThangNam, ngayThangNamCanChi,
                     nguHanh, nguHanhNapAm, thienCan, timCuc, sinhKhac)
import time
from lasotuvi.Lich_HND import jdFromDate


class lapThienBan(object):
    def __init__(self, nn, tt, nnnn, gioSinh, gioiTinh, ten, diaBan,
                 duongLich=True, timeZone=7, namxem: int = 2024):
        super(lapThienBan, self).__init__()
        self.gioiTinh = 1 if gioiTinh == 1 else -1
        self.namNu = "Nam" if gioiTinh == 1 else "Nữ"

        chiGioSinh = diaChi[gioSinh]
        canGioSinh = ((jdFromDate(nn, tt, nnnn) - 1) * 2 % 10 + gioSinh) % 10
        if canGioSinh == 0:
            canGioSinh = 10
        self.chiGioSinh = chiGioSinh
        self.canGioSinh = canGioSinh
        self.gioSinh = "{} {}".format(thienCan[canGioSinh]['tenCan'],
                                      chiGioSinh['tenChi'])
        self.giosinhSo = chiGioSinh['giosinhSo']
        self.timeZone = timeZone
        self.today = time.strftime("%d/%m/%Y")
        self.ngayDuong, self.thangDuong, self.namDuong, self.ten = \
            nn, tt, nnnn, ten
        self.namxem = namxem
        if duongLich is True:
            self.ngayAm, self.thangAm, self.namAm, self.thangNhuan = \
                ngayThangNam(self.ngayDuong, self.thangDuong, self.namDuong,
                             True, self.timeZone)
        else:
            self.ngayAm, self.thangAm, self.namAm = self.ngayDuong,\
                self.thangDuong, self.namDuong
        self.tuoi = namxem - self.namAm + 1
        _, _, namxemamlich, _ = ngayThangNam(1, 6, namxem, True, timeZone)
        _, _, self.canNamXem, self.chiNamXem = ngayThangNamCanChi(1, 1, namxemamlich, timeZone)
        self.canNamXemTen = thienCan[self.canNamXem]['tenCan']
        self.chiNamXemTen = diaChi[self.chiNamXem]['tenChi']
        self.canThang, self.chiThang,  self.canNam, self.chiNam = \
            ngayThangNamCanChi(self.ngayAm, self.thangAm,
                               self.namAm, False, self.timeZone)
        self.chiThangReal = (self.chiThang + 1)%12 +1
        self.canThangTen = thienCan[self.canThang]['tenCan']
        self.canNamTen = thienCan[self.canNam]['tenCan']
        self.chiThangTen = diaChi[self.chiThangReal]['tenChi']
        self.chiNamTen = diaChi[self.chiNam]['tenChi']

        self.canNgay, self.chiNgay = canChiNgay(
            self.ngayDuong, self.thangDuong, self.namDuong,
            duongLich, timeZone)
        self.canNgayTen = thienCan[self.canNgay]['tenCan']
        self.chiNgayTen = diaChi[self.chiNgay]['tenChi']

        cungAmDuong = 1 if (diaBan.cungMenh % 2 == 1) else -1
        self.amDuongNamSinh = "Dương" if (self.chiNam % 2 == 1) else "Âm"
        self.amDuongNamSinhId = 1 if (self.chiNam % 2 == 1) else -1
        if (cungAmDuong * self.amDuongNamSinhId == 1):
            self.amDuongMenh = "Âm dương thuận lý"
        else:
            self.amDuongMenh = "Âm dương nghịch lý"

        cuc = timCuc(diaBan.cungMenh, self.canNam)
        self.hanhCuc = nguHanh(cuc)['id']
        self.tenCuc = nguHanh(cuc)['tenCuc']

        chiCungMenh = diaBan.thapNhiCung[diaBan.cungMenh].cungSo

        self.menhChu = diaChi[chiCungMenh]['menhChu']
        self.thanChu = diaChi[self.chiNam]['thanChu']

        self.menh = nguHanhNapAm(self.chiNam, self.canNam)
        menhId = nguHanh(self.menh)['id']
        menhCuc = sinhKhac(menhId, self.hanhCuc)
        if menhCuc == 1:
            self.sinhKhac = "Mệnh sinh Cục"
        elif menhCuc == -1:
            self.sinhKhac = "Mệnh khắc Cục"
        elif menhCuc == -1j:
            self.sinhKhac = "Cục khắc Mệnh"
        elif menhCuc == 1j:
            self.sinhKhac = "Cục sinh Mệnh"
        else:
            self.sinhKhac = "Cục Mệnh bình hòa"

        self.banMenh = nguHanhNapAm(self.chiNam, self.canNam, True)
