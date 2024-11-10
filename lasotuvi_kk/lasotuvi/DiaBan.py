# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""

from lasotuvi.AmDuong import diaChi, dichCung, khoangCachCung, ngayThangNamCanChi

from lasotuvi.Sao import (saoLiemTrinh, saoTuVi, saoThienDong, saoVuKhuc, saoVanKhuc,
                          saoThienCo, saoThienPhu, saoThaiAm, saoThamLang, saoCuMon,
                          saoThienTuong, saoThienLuong, saoThatSat, saoPhaQuan, saoVanXuong,
                          saoTaPhu, saoHuuBat, saoThaiDuong)

class cungDiaBan(object):
    """docstring for cungDiaBan"""
    def __init__(self, cungID):
        # super(cungDiaBan, self).__init__()
        hanhCung = [None, "Thủy", "Thổ", "Mộc", "Mộc", "Thổ", "Hỏa",
                    "Hỏa", "Thổ", "Kim", "Kim", "Thổ", "Thủy"]
        self.cungSo = cungID
        self.hanhCung = hanhCung[cungID]
        self.cungSao = []
        self.cungAmDuong = -1 if (self.cungSo % 2 == 0) else 1
        self.cungTen = diaChi[self.cungSo]['tenChi']
        self.cungThan = False

    def themSao(self, sao):
        dacTinhSao(self.cungSo, sao)
        self.cungSao.append(sao.__dict__)
        self.cungSao.sort(key=lambda x: x['priority'], reverse=True)
        return self

    def cungChu(self, tenCungChu):
        self.cungChu = tenCungChu
        return self

    def daiHan(self, daiHan):
        self.cungDaiHan = daiHan
        return self
    
    def luuDaiHan(self, luuDaiHan):
        self.luuDaiHan = luuDaiHan
        return self
    
    def luuTieuHan(self, luuTieuHan):
        self.luuTieuHan = luuTieuHan
        return self

    def tieuHan(self, tieuHan):
        self.cungTieuHan = diaChi[tieuHan + 1]['tenChi']
        return self
    
    def canDiaBan(self, canDiaBanID: int, canDiaBanTen: str):
        self.canDiaBanID = canDiaBanID
        self.canDiaBanTen = canDiaBanTen
        return self

    def anCungThan(self):
        self.cungThan = True

    def anTuan(self):
        self.tuanTrung = True

    def anTriet(self):
        self.trietLo = True

    def anLyTam(self, canDoiID):
        bangHoa = [
            [saoLiemTrinh, saoPhaQuan, saoVuKhuc, saoThaiDuong],
            [saoThienCo, saoThienLuong, saoTuVi, saoThaiAm],
            [saoThienDong, saoThienCo, saoVanXuong, saoLiemTrinh],
            [saoThaiAm, saoThienDong, saoThienCo, saoCuMon],
            [saoThamLang, saoThaiAm, saoHuuBat, saoThienCo],
            [saoVuKhuc, saoThamLang, saoThienLuong, saoVanKhuc],
            [saoThaiDuong, saoVuKhuc, saoThaiAm, saoThienDong],
            [saoCuMon, saoThaiDuong, saoVanKhuc, saoVanXuong],
            [saoThienLuong, saoTuVi, saoTaPhu, saoVuKhuc],
            [saoPhaQuan, saoCuMon, saoThaiAm, saoThamLang]
        ]
        self.lyTamID = []
        self.huongTamID = []
        canID = self.canDiaBanID
        for i in range(4):
            if bangHoa[canID-1][i].saoID in [sao['saoID'] for sao in self.cungSao]:
                self.lyTamID.append(i)
            if bangHoa[canDoiID-1][i].saoID in [sao['saoID'] for sao in self.cungSao]:
                self.huongTamID.append(i)
        return self
    

class diaBan(object):
    def __init__(self, thangSinhAmLich, gioSinhAmLich, tuoi):
        super(diaBan, self).__init__()
        self.thangSinhAmLich = thangSinhAmLich
        self.gioSinhAmLich = gioSinhAmLich
        self.thapNhiCung = [cungDiaBan(i) for i in range(13)]
        self.tuoi = tuoi
        self.nhapCungChu()
        self.nhapCungThan()

    def cungChu(self, thangSinhAmLich, gioSinhAmLich):
        self.cungThan = dichCung(3, thangSinhAmLich - 1, gioSinhAmLich - 1)
        self.cungMenh = dichCung(3, thangSinhAmLich - 1, - (gioSinhAmLich) + 1)
        cungPhuMau = dichCung(self.cungMenh, 1)
        cungPhucDuc = dichCung(self.cungMenh, 2)
        cungDienTrach = dichCung(self.cungMenh, 3)
        cungQuanLoc = dichCung(self.cungMenh, 4)
        self.cungNoboc = dichCung(self.cungMenh, 5)  # Để an sao Thiên thương
        cungThienDi = dichCung(self.cungMenh, 6)
        self.cungTatAch = dichCung(self.cungMenh, 7)  # an sao Thiên sứ
        cungTaiBach = dichCung(self.cungMenh, 8)
        cungTuTuc = dichCung(self.cungMenh, 9)
        cungTheThiep = dichCung(self.cungMenh, 10)
        cungHuynhDe = dichCung(self.cungMenh, 11)

        cungChuThapNhiCung = [
            {
                'cungId': 1,
                'tenCung': "Mệnh",
                'cungSoDiaBan': self.cungMenh
            },
            {
                'cungId': 2,
                'tenCung': "Phụ Mẫu",
                'cungSoDiaBan': cungPhuMau

            },
            {
                'cungId': 3,
                'tenCung': "Phúc Đức",
                'cungSoDiaBan': cungPhucDuc

            },
            {
                'cungId': 4,
                'tenCung': "Điền Trạch",
                'cungSoDiaBan': cungDienTrach

            },
            {
                'cungId': 5,
                'tenCung': "Quan Lộc",
                'cungSoDiaBan': cungQuanLoc

            },
            {
                'cungId': 6,
                'tenCung': "Nô Bộc",
                'cungSoDiaBan': self.cungNoboc

            },
            {
                'cungId': 7,
                'tenCung': "Thiên Di",
                'cungSoDiaBan': cungThienDi

            },
            {
                'cungId': 8,
                'tenCung': "Tật Ách",
                'cungSoDiaBan': self.cungTatAch

            },
            {
                'cungId': 9,
                'tenCung': "Tài Bạch",
                'cungSoDiaBan': cungTaiBach

            },
            {
                'cungId': 10,
                'tenCung': "Tử Tức",
                'cungSoDiaBan': cungTuTuc

            },
            {
                'cungId': 11,
                'tenCung': "Phu Thê",
                'cungSoDiaBan': cungTheThiep

            },
            {
                'cungId': 12,
                'tenCung': "Huynh Đệ",
                'cungSoDiaBan': cungHuynhDe

            }
        ]
        return cungChuThapNhiCung

    def nhapCungChu(self):
        for cung in self.cungChu(self.thangSinhAmLich, self.gioSinhAmLich):
            self.thapNhiCung[cung['cungSoDiaBan']].cungChu(cung['tenCung'])
        return self

    def nhapDaiHan(self, cucSo, gioiTinh):
        """Nhap dai han

        Args:
            cucSo (TYPE): Description
            gioiTinh (TYPE): Description

        Returns:
            TYPE: Description
        """
        for cung in self.thapNhiCung:
            khoangCach = khoangCachCung(cung.cungSo, self.cungMenh, gioiTinh)
            cung.daiHan(cucSo + khoangCach * 10)
        return self

    def nhapTieuHan(self, khoiTieuHan, gioiTinh, chiNam):
        # Vị trí khởi tiểu Hạn là của năm sinh theo chi
        # vì vậy cần phải tìm vị trí cung Tý của năm đó
        viTriCungTy1 = dichCung(khoiTieuHan, -gioiTinh * (chiNam - 1))

        # Tiếp đó là nhập hạn
        for cung in self.thapNhiCung:
            khoangCach = khoangCachCung(cung.cungSo, viTriCungTy1, gioiTinh)
            cung.tieuHan(khoangCach)
        return self

    def nhapCungThan(self):
        self.thapNhiCung[self.cungThan].anCungThan()

    def nhapSao(self, cungSo, *args):
        for sao in args:
            self.thapNhiCung[cungSo].themSao(sao)
        return self

    def nhapTuan(self, *args):
        for cung in args:
            self.thapNhiCung[cung].anTuan()
        return self

    def nhapTriet(self, *args):
        for cung in args:
            self.thapNhiCung[cung].anTriet()
        return self
    
    def nhapCanDiaBan(self, canNam):
        can = [
            "G.",
            "Â.",
            "B.",
            "Đ.",
            "M.",
            "K.",
            "C.", 
            "T.",
            "N.", 
            "Q."
        ]
        for cung in self.thapNhiCung:
            canCungId = (canNam%5*2 + ((cung.cungSo + 9)%12))%10+1
            canCungTen = can[canCungId-1]
            cung.canDiaBan(canCungId, canCungTen)
        return self

    def nhapLuuDaiHan(self, *args):
        cungLuuDaiHan = [
            "ĐV.Mệnh",
            "ĐV.Phụ",
            "ĐV.Phúc",
            "ĐV.Điền",
            "ĐV.Quan",
            "ĐV.Nô",
            "ĐV.Di",
            "ĐV.Tật",
            "ĐV.Tài",
            "ĐV.Tử",
            "ĐV.Phối",
            "ĐV.Bào"
        ]
        canDVMenhID = 0
        for cung in self.thapNhiCung:
            for i in range(12):
                index = (self.tuoi + 10*i)%120    
                if index >= int(cung.cungDaiHan) and index < int(cung.cungDaiHan) + 10:
                    cung = cung.luuDaiHan(cungLuuDaiHan[i])
        for cung in self.thapNhiCung:
            index = self.tuoi
            if index >= int(cung.cungDaiHan) and index < int(cung.cungDaiHan) + 10:
                canDVMenhID = cung.canDiaBanID

        self.canDVMenhID = canDVMenhID
        return self

    def nhapLuuTieuHan(self, chiNamXem, *args):
        cungLuuTieuHan = [
            "LN.Mệnh",
            "LN.Phụ",
            "LN.Phúc",
            "LN.Điền",
            "LN.Quan",
            "LN.Nô",
            "LN.Di",
            "LN.Tật",
            "LN.Tài",
            "LN.Tử",
            "LN.Phối",
            "LN.Bào"
        ]
        for cung in self.thapNhiCung:
            tieuHanId = (cung.cungSo + 12 - chiNamXem)%12
            cung = cung.luuTieuHan(cungLuuTieuHan[tieuHanId])
        return self
    
    def nhapLyTam(self):
        for i in range(len(self.thapNhiCung)):
            cungDoiID = (i+6)%12
            canDoiID = self.thapNhiCung[cungDoiID].canDiaBanID
            self.thapNhiCung[i].anLyTam(canDoiID)
        return self

def dacTinhSao(viTriDiaBan, sao):
    saoId = sao.saoID
    maTranDacTinh = {
        1: ["Tử vi", "B", "Đ", "M", "B", "V", "M", "M", "Đ", "M", "B", "V",
            "B"],
        2: ["Liêm trinh", "V", "Đ", "V", "H", "M", "H", "V", "Đ", "V", "H",
            "M", "H"],
        3: ["Thiên đồng", "V", "H", "M", "Đ", "H", "Đ", "H", "H", "M", "H",
            "H", "Đ"],
        4: ["Vũ khúc", "V", "M", "V", "Đ", "M", "H", "V", "M", "V", "Đ", "M",
            "H"],
        5: ["Thái dương", "H", "Đ", "V", "V", "V", "M", "M", "Đ", "H", "H",
            "H", "H"],
        6: ["Thiên cơ", "Đ", "Đ", "H", "M", "M", "V", "Đ", "Đ", "V", "M", "M",
            "H"],
        7: ["Thiên phủ", "M", "B", "M", "B", "V", "Đ", "M", "Đ", "M", "B",
             "V", "Đ"],
        8: ["Thái âm", "V", "Đ", "H", "H", "H", "H", "H", "Đ", "V", "M",
            "M", "M"],
        9: ["Tham lang", "H", "M", "Đ", "H", "V", "H", "H", "M", "Đ", "H",
            "V", "H"],
        10: ["Cự môn", "V", "H", "V", "M", "H", "H", "V", "H", "Đ", "M", "H",
             "Đ"],
        11: ["Thiên tướng", "V", "Đ", "M", "H", "V", "Đ", "V", "Đ", "M", "H",
             "V", "Đ"],
        12: ["Thiên lương", "V", "Đ", "V", "V", "M", "H", "M", "Đ", "V", "H",
             "M", "H"],
        13: ["Thất sát", "M", "Đ", "M", "H", "H", "V", "M", "Đ", "M", "H",
             "H", "V"],
        14: ["Phá quân", "M", "V", "H", "H", "Đ", "H", "M", "V", "H", "H",
             "Đ", "H"],
        51: ["Đà la", "H", "Đ", "H", "H", "Đ", "H", "H", "Đ", "H", "H", "Đ",
             "H"],
        52: ["Kình dương", "H", "Đ", "H", "H", "Đ", "H", "H", "Đ", "H", "H",
             "Đ", "H"],
        55: ["Linh tinh", "H", "H", "Đ", "Đ", "Đ", "Đ", "Đ", "H", "H", "H",
             "H", "H"],
        56: ["Hỏa tinh", "H", "H", "Đ", "Đ", "Đ", "Đ", "Đ", "H", "H", "H",
             "H", "H"],
        57: ["Văn xương", "H", "Đ", "H", "Đ", "H", "Đ", "H", "Đ", "H", "H",
             "Đ", "Đ"],
        58: ["Văn khúc", "H", "Đ", "H", "Đ", "H", "Đ", "H", "Đ", "H", "H",
             "Đ", "Đ"],
        53: ["Địa không", "H", "H", "Đ", "H", "H", "Đ", "H", "H", "Đ", "H",
             "H", "Đ"],
        54: ["Địa kiếp", "H", "H", "Đ", "H", "H", "Đ", "H", "H", "Đ", "H", "H",
             "Đ"],
        95: ["Hóa kỵ", None, "Đ", None, None, "Đ", None, None, "Đ", None, None,
             "Đ", None],
        36: ["Đại hao", None, None, "Đ", "Đ", None, None, None, None, "Đ", "Đ",
             None, None],
        30: ["Tiểu Hao", None, None, "Đ", "Đ", None, None, None, None, "Đ",
             "Đ", None, None],
        69: ["Thiên khốc", "Đ", "Đ", None, "Đ", None, None, "Đ", "Đ", None,
             "Đ", None, None],
        70: ["Thiên hư", "Đ", "Đ", None, "Đ", None, None, "Đ", "Đ", None, "Đ",
             None, None],
        98: ["Thiên mã", None, None, "Đ", None, None, "Đ", None, None, None,
             None, None, None],
        73: ["Thiên Hình", None, None, "Đ", "Đ", None, None, None, None, "Đ",
             "Đ", None, None],
        74: ["Thiên riêu", None, None, "Đ", "Đ", None, None, None, None, None,
             "Đ", "Đ", None],

    }
    if sao.saoID in maTranDacTinh.keys():
        if maTranDacTinh[sao.saoID][viTriDiaBan] in ["M", "V", "Đ", "B", "H"]:
            sao.anDacTinh(maTranDacTinh[sao.saoID][viTriDiaBan])
