# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""

from lasotuvi.Lich_HND import S2L, L2S, jdFromDate


thienCan = [
    {
        "id": 0,
        "chuCaiDau": None,
        "tenCan": None,
        "nguHanh": None,
        "nguHanhID": None,
        "vitriDiaBan": None,
        'amDuong': None
    },
    {
        "id": 1,
        "chuCaiDau": "G",
        "tenCan": "Giáp",
        "nguHanh": "M",
        "nguHanhID": 2,
        "vitriDiaBan": 3,
        'amDuong': 1
    },
    {
        "id": 2,
        "chuCaiDau": "A",
        "tenCan": "Ất",
        "nguHanh": "M",
        "nguHanhID": 2,
        "vitriDiaBan": 4,
        'amDuong': -1
    },
    {
        "id": 3,
        "chuCaiDau": "B",
        "tenCan": "Bính",
        "nguHanh": "H",
        "nguHanhID": 4,
        "vitriDiaBan": 6,
        'amDuong': 1
    },
    {
        "id": 4,
        "chuCaiDau": "D",
        "tenCan": "Đinh",
        "nguHanh": "H",
        "nguHanhID": 4,
        "vitriDiaBan": 7,
        'amDuong': -1
    },
    {
        "id": 5,
        "chuCaiDau": "M",
        "tenCan": "Mậu",
        "nguHanh": "O",
        "nguHanhID": 5,
        "vitriDiaBan": 6,
        'amDuong': 1
    },
    {
        "id": 6,
        "chuCaiDau": "K",
        "tenCan": "Kỷ",
        "nguHanh": "O",
        "nguHanhID": 5,
        "vitriDiaBan": 7,
        'amDuong': -1
    },
    {
        "id": 7,
        "chuCaiDau": "C",
        "tenCan": "Canh",
        "nguHanh": "K",
        "nguHanhID": 1,
        "vitriDiaBan": 9,
        'amDuong': 1
    },
    {
        "id": 8,
        "chuCaiDau": "T",
        "tenCan": "Tân",
        "nguHanh": "K",
        "nguHanhID": 1,
        "vitriDiaBan": 10,
        'amDuong': -1
    },
    {
        "id": 9,
        "chuCaiDau": "N",
        "tenCan": "Nhâm",
        "nguHanh": "T",
        "nguHanhID": 3,
        "vitriDiaBan": 12,
        'amDuong': 1
    },
    {
        "id": 10,
        "chuCaiDau": "Q",
        "tenCan": "Quý",
        "nguHanh": "T",
        "nguHanhID": 3,
        "vitriDiaBan": 1,
        'amDuong': -1
    },
]


diaChi = [
    {
        "id": 0,
        "tenChi": "Hem có",
        "tenHanh": ":D",
        "amDuong": 0
    },
    {
        "id": 1,
        "tenChi": "Tý",
        "giosinhSo": "23 giờ - 1 giờ",
        "tenHanh": "T",
        "menhChu": "Tham Lang",
        "thanChu": "Linh Tinh",
        "amDuong": 1
    },
    {
        "id": 2,
        "tenChi": "Sửu",
        "giosinhSo": "1 giờ - 3 giờ",
        "tenHanh": "O",
        "menhChu": "Cự Môn",
        "thanChu": "Thiên Tướng",
        "amDuong": -1
    },
    {
        "id": 3,
        "tenChi": "Dần",
        "giosinhSo": "3 giờ - 5 giờ",
        "tenHanh": "M",
        "menhChu": "Lộc Tồn",
        "thanChu": "Thiên Lương",
        "amDuong": 1
    },
    {
        "id": 4,
        "tenChi": "Mão",
        "giosinhSo": "5 giờ - 7 giờ",
        "tenHanh": "M",
        "menhChu": "Văn Khúc",
        "thanChu": "Thiên Đồng",
        "amDuong": -1
    },
    {
        "id": 5,
        "tenChi": "Thìn",
        "giosinhSo": "7 giờ - 9 giờ",
        "tenHanh": "O",
        "menhChu": "Liêm Trinh",
        "thanChu": "Văn Xương",
        "amDuong": 1
    },
    {
        "id": 6,
        "tenChi": "Tỵ",
        "giosinhSo": "9 giờ - 11 giờ",
        "tenHanh": "H",
        "menhChu": "Vũ Khúc",
        "thanChu": "Thiên Cơ",
        "amDuong": -1
    },
    {
        "id": 7,
        "tenChi": "Ngọ",
        "giosinhSo": "11 giờ - 13 giờ",
        "tenHanh": "H",
        "menhChu": "Phá Quân",
        "thanChu": "Hỏa Tinh",
        "amDuong": 1
    },
    {
        "id": 8,
        "tenChi": "Mùi",
        "giosinhSo": "13 giờ - 15 giờ",
        "tenHanh": "O",
        "menhChu": "Vũ Khúc",
        "thanChu": "Thiên Tướng",
        "amDuong": -1
    },
    {
        "id": 9,
        "tenChi": "Thân",
        "giosinhSo": "15 giờ - 17 giờ",
        "tenHanh": "K",
        "menhChu": "Liêm Trinh",
        "thanChu": "Thiên Lương",
        "amDuong": 1
    },
    {
        "id": 10,
        "tenChi": "Dậu",
        "giosinhSo": "17 giờ - 19 giờ",
        "tenHanh": "K",
        "menhChu": "Văn Khúc",
        "thanChu": "Thiên Đồng",
        "amDuong": -1
    },
    {
        "id": 11,
        "tenChi": "Tuất",
        "giosinhSo": "19 giờ - 21 giờ",
        "tenHanh": "O",
        "menhChu": "Lộc Tồn",
        "thanChu": "Văn Xương",
        "amDuong": 1
    },
    {
        "id": 12,
        "tenChi": "Hợi",
        "giosinhSo": "21 giờ - 23 giờ",
        "tenHanh": "T",
        "menhChu": "Cự Môn",
        "thanChu": "Thiên Cơ",
        "amDuong": -1
    }
]


def ngayThangNam(nn, tt, nnnn, duongLich=True, timeZone=7):
    """Summary

    Args:
        nn (TYPE): ngay
        tt (TYPE): thang
        nnnn (TYPE): nam
        duongLich (bool, optional): bool
        timeZone (int, optional): +7 Vietnam

    Returns:
        TYPE: Description

    Raises:
        Exception: Description
    """
    thangNhuan = 0
    # if nnnn > 1000 and nnnn < 3000 and nn > 0 and \
    if nn > 0 and \
       nn < 32 and tt < 13 and tt > 0:
        if duongLich is True:
            [nn, tt, nnnn, thangNhuan] = S2L(nn, tt, nnnn, timeZone=timeZone)
        return [nn, tt, nnnn, thangNhuan]
    else:
        raise Exception("Ngày, tháng, năm không chính xác.")


def canChiNgay(nn, tt, nnnn, duongLich=True, timeZone=7, thangNhuan=False):
    """Summary

    Args:
        nn (int): ngày
        tt (int): tháng
        nnnn (int): năm
        duongLich (bool, optional): True nếu là dương lịch, False âm lịch
        timeZone (int, optional): Múi giờ
        thangNhuan (bool, optional): Có phải là tháng nhuận không?

    Returns:
        TYPE: Description
    """
    if duongLich is False:
        [nn, tt, nnnn] = L2S(nn, tt, nnnn, thangNhuan, timeZone)
    jd = jdFromDate(nn, tt, nnnn)
    # print jd
    canNgay = (jd + 9) % 10 + 1
    chiNgay = (jd + 1) % 12 + 1
    return [canNgay, chiNgay]


def canChiGio(canNgay, gio):
    """Phần này có lẽ chưa cần thiết và sẽ bổ sung sau.

    Args:
        canNgay (int): Can của ngày cần xem, 1: Giáp, 2: Ất, 3: Bính,...
        gio (int): Chi của giờ, 1: Tý, 2: Sửu,...

    Returns:
        TYPE: Description
    """
    return False


def ngayThangNamCanChi(nn, tt, nnnn, duongLich=True, timeZone=7):
    """chuyển đổi năm, tháng âm/dương lịch sang Can, Chi trong tiếng Việt.
    Không tính đến can ngày vì phải chuyển đổi qua lịch Julius.

    Hàm tìm can ngày là hàm canChiNgay(nn, tt, nnnn, duongLich=True,\
                                    timeZone=7, thangNhuan=False)

    Args:
        nn (int): Ngày
        tt (int): Tháng
        nnnn (int): Năm

    Returns:
        TYPE: Description
    """
    if duongLich is True:
        [nn, tt, nnnn, thangNhuan] = \
            ngayThangNam(nn, tt, nnnn, timeZone=timeZone)
    # Can của tháng
    canThang = (nnnn * 12 + tt + 3) % 10 + 1
    chiThang = tt
    # Can chi của năm
    canNamSinh = (nnnn + 6) % 10 + 1
    chiNam = (nnnn + 8) % 12 + 1

    return [canThang, chiThang, canNamSinh, chiNam]

    
def nguHanh(tenHanh):
    """
    Args:
        tenHanh (string): Tên Hành trong ngũ hành, Kim hoặc K, Moc hoặc M,
        Thuy hoặc T, Hoa hoặc H, Tho hoặc O

    Returns:
        Dictionary: ID của Hành, tên đầy đủ của Hành, số Cục của Hành

    Raises:
        Exception: Description
    """
    if tenHanh in ["Kim", "K"]:
        return {"id": 1, "tenHanh": "Kim", "cuc": 4, "tenCuc": "Kim tứ Cục",
                "css": "hanhKim"}
    elif tenHanh == "Moc" or tenHanh == "M":
        return {"id": 2, "tenHanh": "Mộc", "cuc": 3, "tenCuc": "Mộc tam Cục",
                "css": "hanhMoc"}
    elif tenHanh == "Thuy" or tenHanh == "T":
        return {"id": 3, "tenHanh": "Thủy", "cuc": 2, "tenCuc": "Thủy nhị Cục",
                "css": "hanhThuy"}
    elif tenHanh == "Hoa" or tenHanh == "H":
        return {"id": 4, "tenHanh": "Hỏa", "cuc": 6, "tenCuc": "Hỏa lục Cục",
                "css": "hanhHoa"}
    elif tenHanh == "Tho" or tenHanh == "O":
        return {"id": 5, "tenHanh": "Thổ", "cuc": 5, "tenCuc": "Thổ ngũ Cục",
                "css": "hanhTho"}
    elif tenHanh == "none":
        return {"id": 6, "css":"none"}
    else:
        raise Exception(
            "Tên Hành phải thuộc Kim (K), Mộc (M), Thủy (T), \
             Hỏa (H) hoặc Thổ (O)")


def sinhKhac(hanh1, hanh2):
    """
    Args:
        hanh1 (TYPE): Description
        hanh2 (TYPE): Description

    Returns:
        TYPE: Description
    """
    matranSinhKhac = [
        [None, None, None, None, None, None],
        [None, 0, -1, 1, -1j, 1j],
        [None, -1j, 0, 1j, 1, -1],
        [None, 1j, 1, 0, 1, -1j],
        [None, -1, 1j, -1j, 0, 1],
        [None, 1, -1j, -1, 1j, 0]
    ]
    return matranSinhKhac[hanh1][hanh2]


def nguHanhNapAm(diaChi, thienCan, xuatBanMenh=False):
    """Sử dụng Ngũ Hành nạp âm để tính Hành của năm.

    Args:
        diaChi (integer): Số thứ tự của địa chi (Tý=1, Sửu=2,...)
        thienCan (integer): Số thứ tự của thiên can (Giáp=1, Ất=2,...)

    Returns:
        Trả về chữ viết tắt Hành của năm (K, T, H, O, M)
    """
    banMenh = {
        "K1": "HẢI TRUNG KIM",
        "T1": "GIÁNG HẠ THỦY",
        "H1": "TÍCH LỊCH HỎA",
        "O1": "BÍCH THƯỢNG THỔ",
        "M1": "TANG ÐỐ MỘC",
        "T2": "ÐẠI KHÊ THỦY",
        "H2": "LƯ TRUNG HỎA",
        "O2": "THÀNH ÐẦU THỔ",
        "M2": "TÒNG BÁ MỘC",
        "K2": "KIM BẠCH KIM",
        "H3": "PHÚ ÐĂNG HỎA",
        "O3": "SA TRUNG THỔ",
        "M3": "ÐẠI LÂM MỘC",
        "K3": "BẠCH LẠP KIM",
        "T3": "TRƯỜNG LƯU THỦY",
        "K4": "SA TRUNG KIM",
        "T4": "THIÊN HÀ THỦY",
        "H4": "THIÊN THƯỢNG HỎA",
        "O4": "LỘ BÀN THỔ",
        "M4": "DƯƠNG LIỄU MỘC",
        "T5": "TUYỀN TRUNG THỦY",
        "H5": "SƠN HẠ HỎA",
        "O5": "ÐẠI TRẠCH THỔ",
        "M5": "THẠCH LỰU MỘC",
        "K5": "KIẾM PHONG KIM",
        "H6": "SƠN ÐẦU HỎA",
        "O6": "ỐC THƯỢNG THỔ",
        "M6": "BÌNH ÐỊA MỘC",
        "K6": "XOA XUYẾN KIM",
        "T6": "ÐẠI HẢI THỦY"}
    matranNapAm = [
        [0, "G", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "N", "Q"],
        [1, "K1", False, "T1", False, "H1", False, "O1", False, "M1", False],
        [2, False, "K1", False, "T1", False, "H1", False, "O1", False, "M1"],
        [3, "T2", False, "H2", False, "O2", False, "M2", False, "K2", False],
        [4, False, "T2", False, "H2", False, "O2", False, "M2", False, "K2"],
        [5, "H3", False, "O3", False, "M3", False, "K3", False, "T3", False],
        [6, False, "H3", False, "O3", False, "M3", False, "K3", False, "T3"],
        [7, "K4", False, "T4", False, "H4", False, "O4", False, "M4", False],
        [8, False, "K4", False, "T4", False, "H4", False, "O4", False, "M4"],
        [9, "T5", False, "H5", False, "O5", False, "M5", False, "K5", False],
        [10, False, "T5", False, "H5", False, "O5", False, "M5", False, "K5"],
        [11, "H6", False, "O6", False, "M6", False, "K6", False, "T6", False],
        [12, False, "H6", False, "O6", False, "M6", False, "K6", False, "T6"]
    ]
    try:
        nh = matranNapAm[diaChi][thienCan]
        if nh[0] in ["K", "M", "T", "H", "O"]:
            if xuatBanMenh is True:
                return banMenh[nh]
            else:
                return nh[0]
    except:
        raise Exception(nguHanhNapAm.__doc__)


def dichCung(cungBanDau, *args):
    cungSauKhiDich = int(cungBanDau)
    for soCungDich in args:
        cungSauKhiDich += int(soCungDich)
    if cungSauKhiDich % 12 is 0:
        return 12
    return cungSauKhiDich % 12


def khoangCachCung(cung1, cung2, chieu=1):
    if chieu is 1:  # Con trai, chiều dương
        return (cung1 - cung2 + 12) % 12
    else:
        return (cung2 - cung1 + 12) % 12


def timCuc(viTriCungMenhTrenDiaBan, canNamSinh):
    canThangGieng = (canNamSinh * 2 + 1) % 10
    canThangMenh = ((viTriCungMenhTrenDiaBan - 3) % 12 + canThangGieng) % 10
    if canThangMenh is 0:
        canThangMenh = 10
    return nguHanhNapAm(viTriCungMenhTrenDiaBan, canThangMenh)


def timTuVi(cuc, ngaySinhAmLich):
    """Tìm vị trí của sao Tử vi

    Args:
        cuc (TYPE): Description
        ngaySinhAmLich (TYPE): Description

    Returns:
        TYPE: Description

    Raises:
        Exception: Description
    """
    cungDan = 3  # Vị trí cung Dần ban đầu là 3
    cucBanDau = cuc
    if cuc not in [2, 3, 4, 5, 6]:  # Tránh trường hợp infinite loop
        raise Exception("Số cục phải là 2, 3, 4, 5, 6")
    while cuc < ngaySinhAmLich:
        cuc += cucBanDau
        cungDan += 1  # Dịch vị trí cung Dần
    saiLech = cuc - ngaySinhAmLich
    if saiLech % 2 is 1:
        saiLech = -saiLech  # Nếu sai lệch là chẵn thì tiến, lẻ thì lùi
    return dichCung(cungDan, saiLech)


def timTrangSinh(cucSo):
    """Tìm vị trí của Tràng sinh
    Theo thứ tự cục số
    vị trí Tràng sinh sẽ là Dần, Tỵ, Thân hoặc Hợi

    *LƯU Ý* Theo cụ Thiên Lương: Nam -> Thuận, Nữ -> Nghịch

    Args:
        cucSo (int): số cục (2, 3, 4, 5, 6)

    Returns:
        int: Vị trí sao Tràng sinh

    Raises:
        Exception: Description
    """
    if cucSo == 6:  # Hỏa lục cục
        return 3  # Tràng sinh ở Dần
    elif cucSo == 4:  # Kim tứ cục
        return 6  # Tràng sinh ở Tỵ
    elif cucSo == 2 or cucSo == 5:  # Thủy nhị cục, Thổ ngũ cục
        return 9  # Tràng sinh ở Thân
    elif cucSo == 3:  # Mộc tam cục
        return 12  # Tràng sinh ở Hợi
    else:
        # print cucSo
        raise Exception("Không tìm được cung an sao Trường sinh")


def timHoaLinh(chiNamSinh, gioSinh, gioiTinh, amDuongNamSinh):
    if chiNamSinh in [3, 7, 11]:
        khoiCungHoaTinh = 2
        khoiCungLinhTinh = 4
    elif chiNamSinh in [1, 5, 9]:
        khoiCungHoaTinh = 3
        khoiCungLinhTinh = 11
    elif chiNamSinh in [6, 10, 2]:
        khoiCungHoaTinh = 11
        khoiCungLinhTinh = 4
    elif chiNamSinh in [12, 4, 8]:
        khoiCungHoaTinh = 10
        khoiCungLinhTinh = 11
    else:
        raise Exception("Không thể khởi cung tìm Hỏa-Linh")
    # print khoiCungHoaTinh, khoiCungLinhTinh

    if (gioiTinh * amDuongNamSinh) == -1:
        viTriHoaTinh = dichCung(khoiCungHoaTinh + 1, (-1) * gioSinh)
        viTriLinhTinh = dichCung(khoiCungLinhTinh - 1, gioSinh)
    elif (gioiTinh * amDuongNamSinh) == 1:
        viTriHoaTinh = dichCung(khoiCungHoaTinh - 1, gioSinh)
        viTriLinhTinh = dichCung(khoiCungLinhTinh + 1, (-1) * gioSinh)

    return [viTriHoaTinh, viTriLinhTinh]


def timThienKhoi(canNam):
    khoiViet = [None, 2, 1, 12, 12, 2, 1, 3, 3, 4, 4]
    try:
        return khoiViet[canNam]
    except:
        raise Exception("Không tìm được vị trí Khôi-Việt")


def timThienQuanThienPhuc(canNam):
    # Giáp dương Nhâm khuyển Ất long nghi
    # Mậu thổ Canh chư Quý mã thượng
    # Kỳ nhân quý hiển khả tiên tri
    thienQuan = [None, 8, 5, 6, 3, 4, 10, 12, 10, 11, 7]

    # Giáp ái kim kê Ất ái hầu
    # Đinh chư Bính thử Kỷ hổ đầu
    # Tân quý phùng xà phúc lộc nhiêu
    thienPhuc = [None, 10, 9, 1, 12, 4, 3, 7, 6, 7, 6]
    try:
        return thienQuan[canNam], thienPhuc[canNam]
    except:
        raise Exception("Không tìm được Quan-Phúc")


def timCoThan(chiNam):
    if chiNam in [12, 1, 2]:
        return 3
    elif chiNam in [3, 4, 5]:
        return 6
    elif chiNam in [6, 7, 8]:
        return 9
    else:
        return 12


def timThienMa(chiNam):
    demNghich = chiNam % 4
    if demNghich == 1:
        return 3
    elif demNghich == 2:
        return 12
    elif demNghich == 3:
        return 9
    elif demNghich == 0:
        return 6
    else:
        raise Exception("Không tìm được Thiên mã")
    

def timTuongTinh(chinam):
    demnghich = chinam % 4
    if demnghich == 1:
        return 1
    elif demnghich == 2:
        return 10
    elif demnghich == 3:
        return 7
    elif demnghich == 0:
        return 4

def timThienVu(chiThang):
    if chiThang == 1 or chiThang == 5 or chiThang == 9:
        return 6
    elif chiThang == 3 or chiThang == 7 or chiThang == 11:
        return 3
    elif chiThang == 4 or chiThang ==8 or chiThang == 12:
        return 12
    elif chiThang == 2 or chiThang == 6 or chiThang == 10:
        return 9

def timThienNguyet(chiThang):
    if chiThang == 1 or chiThang == 11:
        return 11
    elif chiThang == 4 or chiThang == 9 or chiThang == 12:
        return 3
    elif chiThang == 5 or chiThang == 8:
        return 8
    elif chiThang == 6:
        return 4
    elif chiThang == 3:
        return 5
    elif chiThang == 2:
        return 6
    elif chiThang == 10:
        return 7
    elif chiThang == 7:
        return 12

def timAmSat(chiThang):
    dem = chiThang % 6
    if dem == 0:
        return 5
    elif dem == 1:
        return 3
    elif dem == 2:
        return 1
    elif dem == 3:
        return 11
    elif dem == 4:
        return 9
    elif dem == 5:
        return 7

def timPhaToai(chiNam):
    demNghich = chiNam % 3
    if demNghich == 0:
        return 10
    elif demNghich == 1:
        return 6
    elif demNghich == 2:
        return 2
    else:
        raise Exception("Không tìm được Phá toái")


def timTriet(canNam):
    # Giáp Kỷ, Thân Dậu cung
    if canNam in [1, 6]:
        return 9, 10

    # Ất Canh, Ngọ Mùi cung
    elif canNam in [2, 7]:
        return 7, 8

    # Bính Tân, Thìn Tị cung
    elif canNam in [3, 8]:
        return 5, 6

    # Đinh Nhâm, Dần Mão cung
    elif canNam in [4, 9]:
        return 3, 4

    # Mậu Quý, Tý Sửu cung
    elif canNam in [5, 10]:
        return 1, 2
    else:
        raise Exception("Không tìm được Triệt")


def timLuuTru(canNam):
    maTranLuuHa = [None, 10, 11, 8, 5, 6, 7, 9, 4, 12, 3]
    maTranThienTru = [None, 6, 7, 1, 6, 7, 9, 3, 7, 10, 11]
    try:
        return maTranLuuHa[canNam], maTranThienTru[canNam]
    except:
        raise Exception("Không tìm được Lưu - Trù")
