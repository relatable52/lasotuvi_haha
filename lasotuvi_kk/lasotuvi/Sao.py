# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""
from lasotuvi.AmDuong import nguHanh


class Sao(object):
    """Summary
        Args:
            saoID (int): 1, 2, ...
            saoTen (TYPE): Tử vi, Tham lang,...
            saoNguHanh (TYPE): K, M, T, H, O
            saoLoai (str, optional): Sao tốt < 10, sau xấu > 10
                1: Chính tinh, 2: Phụ tinh nói chung
                3: Quý tinh, 4: Quyền tinh, 5: Phúc tinh, 6: Văn tinh
                7: Đài các tinh, 8: Đào hoa tinh

                11: Sát tinh, 12: Bại tinh, 13: Ám tinh, 14: Dâm tinh,
                15: Hình tinh
            saoPhuongVi (str, optional): Bắc Đẩu tinh, Nam Bắc Đẩu tinh
            saoAmDuong (str, optional): Âm Dương của sao
            vongTrangSinh (int, optional): 0/None: Không thuộc vòng Tràng sinh
                                            1: Thuộc vòng Tràng sinh
        """

    def __init__(self, saoID, saoTen, saoNguHanh, saoLoai=2, saoPhuongVi="",
                 saoAmDuong="", vongTrangSinh=0, tenNamPhai = "", dam=False):
        super(Sao, self).__init__()
        self.saoID = saoID
        self.saoTen = " ".join([i[0].upper()+i[1:] for i in saoTen.split()])
        self.saoNguHanh = saoNguHanh
        self.saoLoai = saoLoai
        self.saoPhuongVi = saoPhuongVi
        self.saoAmDuong = saoAmDuong
        self.vongTrangSinh = vongTrangSinh
        self.cssSao = nguHanh(saoNguHanh)['css']
        self.saoDacTinh = None
        self.tenNamPhai = tenNamPhai if tenNamPhai else self.saoTen

        if(dam):
            self.cssSao += " bold"
            self.priority = 1
        else:
            self.priority = 0

    def anDacTinh(self, dacTinh):
        """An Đặc tính cho sao: V, M, Đ, B, H
        Args: saoDacTinh (str): Đặc tính của sao, Vượng (V), Miếu (M),
                                Đắc (Đ), Bình (B), Hãm (H)
        Returns:
            object: self
        """
        dt = {
            "V": "vuongDia",
            "M": "mieuDia",
            "Đ": "dacDia",
            "B": "binhHoa",
            "H": "hamDia",
        }
        self.saoDacTinh = dacTinh
        # self.saoTen += " (%s)" % dacTinh
        # self.cssSao = dt[dacTinh]
        return self

    def anCung(self, saoViTriCung):
        """Summary

        Returns:
            TYPE: Description
        """
        self.saoViTriCung = saoViTriCung
        return self


# Tử vi tinh hệ
saoTuVi = Sao(1, u"Tử vi", "O", 1, u"Đế tinh", 1, 0)
saoLiemTrinh = Sao(2, u"Liêm trinh", "H", 1, u"Bắc đẩu tinh", 1, 0)
saoThienDong = Sao(3, "Thiên đồng", "T", 1, "Bắc đẩu tinh", 1, 0)
saoVuKhuc = Sao(4, "Vũ khúc", "K", 1, "Bắc đẩu tinh", -1, 0)
saoThaiDuong = Sao(5, "Thái Dương", "H", 1, "Nam đẩu tinh", 1, 0)
saoThienCo = Sao(6, "Thiên cơ", "M", 1, "Nam đẩu tinh", -1, 0)

# Thiên phủ tinh hệ
saoThienPhu = Sao(7, "Thiên phủ", "O", 1, "Nam đẩu tinh", 1, 0)
saoThaiAm = Sao(8, "Thái âm", "T", 1, "Bắc đẩu tinh", -1, 0)
saoThamLang = Sao(9, "Tham lang", "T", 1, "Bắc đẩu tinh", -1, 0)
saoCuMon = Sao(10, "Cự môn", "T", 1, "Bắc đẩu tinh", -1, 0)
saoThienTuong = Sao(11, "Thiên tướng", "T", 1, "Nam đẩu tinh", 1, 0)
saoThienLuong = Sao(12, "Thiên lương", "O", 1, "Nam đẩu tinh", -1, 0)
saoThatSat = Sao(13, "Thất sát", "K", 1, "Nam đẩu tinh", 1, 0)
saoPhaQuan = Sao(14, "Phá quân", "T", 1, "Bắc đẩu tinh", -1, 0)

# Vòng Địa chi - Thái tuế
saoThaiTue = Sao(15, "Thái tuế", "H", 15, "", 0)
saoThaiTue = Sao(15, "Thái tuế", "H", 15, "", 0)
saoThieuDuong = Sao(16, "Thiếu dương", "H", 5, tenNamPhai="Hối Khí")
saoTangMon = Sao(17, "Tang môn", "M", 12)
saoTangMon = Sao(17, "Tang môn", "M", 12)
saoThieuAm = Sao(18, "Thiếu âm", "T", 5, tenNamPhai="Quán Sách")
saoQuanPhu3 = Sao(19, "Quan phù", "H", 12)
saoTuPhu = Sao(20, "Tử phù", "H", 12, tenNamPhai="Tiểu Hao")
saoTuPhu = Sao(20, "Tử phù", "H", 12, tenNamPhai="Tiểu Hao")
saoTuePha = Sao(21, "Tuế phá", "H", 12)
saoLongDuc = Sao(22, "Long đức", "T", 5)
saoBachHo = Sao(23, "Bạch hổ", "K", 12)
saoBachHo = Sao(23, "Bạch hổ", "K", 12)
saoPhucDuc = Sao(24, "Phúc đức", "O", 5)
saoDieuKhach = Sao(25, "Điếu khách", "H", 12)
saoTrucPhu = Sao(26, "Trực phù", "H", 16, tenNamPhai="Bệnh Phù")
saoTrucPhu = Sao(26, "Trực phù", "H", 16, tenNamPhai="Bệnh Phù")

#  Vòng Thiên can - Lộc tồn
saoLocTon = Sao(27, "Lộc tồn", "O", 3, "Bắc đẩu tinh", dam=True)
saoBacSy = Sao(109, "Bác sỹ", "T", 5, )
saoLucSi = Sao(28, "Lực sĩ", "H", 2)
saoThanhLong = Sao(29, "Thanh long", "T", 5)
saoTieuHao = Sao(30, "Tiểu hao", "H", 12)
saoTuongQuan = Sao(31, "Tướng quân", "M", 4)
saoTieuHao = Sao(30, "Tiểu hao", "H", 12)
saoTuongQuan = Sao(31, "Tướng quân", "M", 14)
saoTauThu = Sao(32, "Tấu thư", "K", 3)
saoPhiLiem = Sao(33, "Phi liêm", "H", 12)
saoPhiLiem = Sao(33, "Phi liêm", "H", 12)
saoHyThan = Sao(34, "Hỷ thần", "H", 5)
saoBenhPhu = Sao(35, "Bệnh phù", "O", 12)
saoDaiHao = Sao(36, "Đại hao", "H", 12)
saoDaiHao = Sao(36, "Đại hao", "H", 12)
saoPhucBinh = Sao(37, "Phục binh", "H", 13)
saoQuanPhu2 = Sao(38, "Quan phủ", "H", 12)
saoQuanPhu2 = Sao(38, "Quan phủ", "H", 12)

# Vòng Tràng sinh
saoTrangSinh = Sao(39, "Tràng sinh", "T", 5, vongTrangSinh=1)
saoMocDuc = Sao(40, "Mộc dục", "T", 14, vongTrangSinh=1)
saoQuanDoi = Sao(41, "Quan đới", "K", 4, vongTrangSinh=1)
saoLamQuan = Sao(42, "Lâm quan", "K", 7, vongTrangSinh=1)
saoDeVuong = Sao(43, "Đế vượng", "K", 5, vongTrangSinh=1)
saoSuy = Sao(44, "Suy", "T", 12, vongTrangSinh=1)
saoBenh = Sao(45, "Bệnh", "H", 12, vongTrangSinh=1)
saoTu = Sao(46, "Tử", "H", 12, vongTrangSinh=1)
saoMo = Sao(47, "Mộ", "O", vongTrangSinh=1)
saoTuyet = Sao(48, "Tuyệt", "O", 12, vongTrangSinh=1)
saoThai = Sao(49, "Thai", "O", 14, vongTrangSinh=1)
saoDuong = Sao(50, "Dưỡng", "M", 2, vongTrangSinh=1)

# Lục sát
#    Kình dương đà la
saoDaLa = Sao(51, "Đà la", "K", 11, dam=True)
saoKinhDuong = Sao(52, "Kình dương", "K", 11, dam=True)

#    Địa không - Địa kiếp
saoDiaKhong = Sao(53, "Địa không", "H", 11, dam=True)
saoDiaKiep = Sao(54, "Địa kiếp", "H", 11, dam=True)

#    Hỏa tinh - Linh tinh
saoLinhTinh = Sao(55, "Linh tinh", "H", 11, dam=True)
saoHoaTinh = Sao(56, "Hỏa tinh", "H", 11, dam=True)

# Sao Âm Dương
#    Văn xương - Văn khúc
saoVanXuong = Sao(57, "Văn xương", "K", 6, dam=True)
saoVanKhuc = Sao(58, "Văn Khúc", "T", 6, dam=True)

#    Thiên khôi - Thiên Việt
saoThienKhoi = Sao(59, "Thiên khôi", "H", 6, dam=True)
saoThienViet = Sao(60, "Thiên việt", "H", 6, dam=True)

#    Tả phù - Hữu bật
saoTaPhu = Sao(61, "Tả phù", "O", 2, dam=True)
saoHuuBat = Sao(62, "Hữu bật", "T", 2, dam=True)
saoHuuBat = Sao(62, "Hữu bật", "T", 2, dam=True)

#    Long trì - Phượng các
saoLongTri = Sao(63, "Long trì", "T", 3)
saoPhuongCac = Sao(64, "Phượng các", "M", 3)
saoPhuongCac = Sao(64, "Phượng các", "M", 3)

#    Tam thai - Bát tọa
saoTamThai = Sao(65, "Tam thai", "T", 7)
saoBatToa = Sao(66, "Bát tọa", "M", 7)
saoTamThai = Sao(65, "Tam thai", "T", 7)
saoBatToa = Sao(66, "Bát tọa", "M", 7)

#    Ân quang - Thiên quý
saoAnQuang = Sao(67, "Ân quang", "M", 3)
saoThienQuy = Sao(68, "Thiên quý", "O", 3)

# Sao đôi khác
saoThienKhoc = Sao(69, "Thiên khốc", "K", 12)
saoThienHu = Sao(70, "Thiên hư", "T", 12)
saoThienKhoc = Sao(69, "Thiên khốc", "K", 12)
saoThienHu = Sao(70, "Thiên hư", "T", 12)
saoThienDuc = Sao(71, "Thiên đức", "H", 5)
saoNguyetDuc = Sao(72, "Nguyệt đức", "H", 5)
saoThienHinh = Sao(73, "Thiên hình", "H", 15, dam= True)
saoThienRieu = Sao(74, "Thiên riêu", "T", 13, dam= True)
saoThienHinh = Sao(73, "Thiên hình", "H", 15, dam= True)
saoThienRieu = Sao(74, "Thiên riêu", "T", 13, dam= True)
saoThienY = Sao(75, "Thiên y", "T", 5)
saoQuocAn = Sao(76, "Quốc ấn", "O", 6)
saoDuongPhu = Sao(77, "Đường phù", "M", 4)
saoDaoHoa = Sao(78, "Đào hoa", "M", 8, dam= True)
saoHongLoan = Sao(79, "Hồng loan", "T", 8, dam= True)
saoThienHy = Sao(80, "Thiên hỷ", "T", 5, dam= True)
saoDaoHoa = Sao(78, "Đào hoa", "M", 8, dam= True)
saoHongLoan = Sao(79, "Hồng loan", "T", 8, dam= True)
saoThienHy = Sao(80, "Thiên hỷ", "T", 5, dam= True)
saoThienGiai = Sao(81, "Thiên giải", "H", 5)
saoDiaGiai = Sao(82, "Địa giải", "O", 5)
saoGiaiThan = Sao(83, "Giải thần", "M", 5)
saoThaiPhu = Sao(84, "Thai phụ", "K", 6)
saoPhongCao = Sao(85, "Phong cáo", "O", 4)
saoThienTai = Sao(86, "Thiên tài", "O", 2)
saoThienTho = Sao(87, "Thiên thọ", "O", 5)
saoThienThuong = Sao(88, "Thiên thương", "O", 12)
saoThienSu = Sao(89, "Thiên sứ", "T", 12)
saoThienLa = Sao(90, "Thiên la", "K", 12)
saoDiaVong = Sao(91, "Địa võng", "K", 12)
saoHoaKhoa = Sao(92, "Hóa khoa", "M", 5, dam=True)
saoHoaQuyen = Sao(93, "Hóa quyền", "H", 4, dam=True)
saoHoaLoc = Sao(94, "Hóa Lộc", "K", 3, dam=True)
saoThienLa = Sao(90, "Thiên la", "K", 12)
saoDiaVong = Sao(91, "Địa võng", "K", 12)
saoHoaKhoa = Sao(92, "Hóa khoa", "M", 5, dam=True)
saoHoaQuyen = Sao(93, "Hóa quyền", "H", 4, dam=True)
saoHoaLoc = Sao(94, "Hóa Lộc", "K", 3, dam=True)
saoHoaKy = Sao(95, "Hóa Kỵ", "T", 13, dam=True)
saoCoThan = Sao(96, "Cô Thần", "O", 13)
saoQuaTu = Sao(97, "Quả Tú", "O", 13)
saoThienMa = Sao(98, "Thiên Mã", "H", 3, dam= True)
saoThienMa = Sao(98, "Thiên Mã", "H", 3, dam= True)
saoPhaToai = Sao(99, "Phá Toái", "H", 12)
saoThienQuan = Sao(100, "Thiên Quan", "H", 5)
saoThienPhuc = Sao(101, "Thiên Phúc", "O", 5)
saoThienPhuc = Sao(101, "Thiên Phúc", "O", 5)
saoLuuHa = Sao(102, "Lưu Hà", "T", 12)
saoThienTru = Sao(103, "Thiên Trù", "O", 5)
saoKiepSat = Sao(104, "Kiếp Sát", "H", 11)
saoHoaCai = Sao(105, "Hoa Cái", "K", 14)
saoVanTinh = Sao(106, "LN Văn Tinh", "K", 6)
saoHoaCai = Sao(105, "Hoa Cái", "K", 4)
saoVanTinh = Sao(106, "LN Văn Tinh", "K", 6)
saoDauQuan = Sao(107, "Đẩu Quân", "H", 12)
saoThienKhong = Sao(108, "Thiên Không", "H", 11)

#Sao Lưu
luuDVLoc = Sao(109, "ĐV.Hóa Lộc", "K", 3)
luuDVQuyen = Sao(110, "ĐV.Hóa Quyền", "H", 4)
luuDVKhoa = Sao(111, "ĐV.Hóa Khoa", "M", 5)
luuDVKy = Sao(112, "ĐV.Hóa Kỵ", "T", 13)
luuTVLoc = Sao(113,"LN.Hóa Lộc","K", 3)
luuTVQuyen = Sao(114,"LN.Hóa Quyền","H", 4)
luuTVKhoa  =Sao(115,"LN.Hóa Khoa","M", 5)
luuTVKy = Sao(116,"LN.Hóa Kị","T", 13)
luuDVLoc = Sao(109, "ĐV.Hóa Lộc", "K", 3)
luuDVQuyen = Sao(110, "ĐV.Hóa Quyền", "H", 4)
luuDVKhoa = Sao(111, "ĐV.Hóa Khoa", "M", 5)
luuDVKy = Sao(112, "ĐV.Hóa Kỵ", "T", 13)
luuTVLoc = Sao(113,"LN.Hóa Lộc","K", 3)
luuTVQuyen = Sao(114,"LN.Hóa Quyền","H", 4)
luuTVKhoa  =Sao(115,"LN.Hóa Khoa","M", 5)
luuTVKy = Sao(116,"LN.Hóa Kị","T", 13)
luuThaiTue = Sao(117, "L.Thái tuế", "H", 15)
luuKinhDuong = Sao(118,"L.Kình Dương","K", 11)
luuDaLa = Sao(119,"L.Đà La","K", 11)
luuTangMon = Sao(120,"L.Tang Môn","M", 12)
luuBachHo = Sao(121,"L.Bạch Hổ", "K", 12)
luuThienKhoc = Sao(122,"L.Thiên Khốc","K", 12)
luuThienHu = Sao(123,"L.Thiên Hư","T", 12)
luuLocTon = Sao(124, "L.Lộc Tồn", "O", 3)
luuThienMa = Sao(125,"L.Thiên Mã", "H", 3)

# Sao khâm thiên(thêm và lá số khâm thiên )
saoTuongTinh = Sao(126, "Tướng Tinh", "T", 9)
saoPhanAn = Sao(127, "Phan An", "T", 9)
saoTueDich = Sao(128, "Tuế Dịch", "T", 9)
saoTucThan = Sao(129, "Tức Thần", "T", 21)
saoHoaCai1 = Sao(130, "Hoa Cái", "T", 9)
saoKiepSat1 = Sao(131, "Kiếp Sát", "H", 21)
saoTaiSat = Sao(132, "Tai Sát", "T", 21)
saoThienSat = Sao(133, "Thiên Sát", "T", 21)
saoChiBoi = Sao(134, "Chỉ Bối", "T", 21)
saoHamTri = Sao(135, "Hàm Trì", "M", 9)
saoNguyetSat = Sao(136, "Nguyệt Sát", "T", 21)
saoVongThan = Sao(137, "Vong Thần", "T", 21)
saoThienVu = Sao(141, "Thiên Vu", "O", 9)
saoThienNguyet = Sao(142, "Thiên Nguyệt", "H", 21)
saoAmSat = Sao(143, "Âm Sát", "O", 21)
saoTieuHao1 = Sao(144, "Tiểu Hao", "H", 21)
saoHoiKhi = Sao(138, "Hối Khí", "H", 9)
saoQuanSach = Sao(139, "Quán Sách", "T", 9)
saoBenhPhu1 = Sao(140, u"Bệnh Phù", "H", 21)

DVLocTon = Sao(141, "ĐV.Lộc Tồn", "O", 2)
DVKinh = Sao(142,"ĐV.Kình Dương", "K", 13)
DVDa = Sao(143, "ĐV.Đà La", "K", 13)
saoBenhPhu1 = Sao(140, u"Bệnh Phù", "H", 21)