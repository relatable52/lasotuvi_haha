$(document).ready(function () {
    var uploadLaso = "/upload";
    var d = new Date();
    var thismonth = d.getMonth() + 1;
    var today = d.getDate();
    var thisyear = d.getFullYear();
    $("#ngaysinh").val(today);
    $("#thangsinh").val(thismonth);
    $("#namsinh").val(thisyear);
    function dichCung(cungBanDau, soCungDich) {
        var cungSauKhiDich = Math.floor(cungBanDau);
        cungSauKhiDich += Math.floor(soCungDich);
        if (cungSauKhiDich % 12 == 0) {
            return 12;
        }
        else {
            return cungSauKhiDich % 12;
        }
    }
    diaban = $("[cung-id]").click(function () {
        $("[cung-id]").removeClass("xungChieu");
        cungid = $(this).attr('cung-id');
        cungXungChieu = dichCung(cungid, 6);
        cungTamHop1 = dichCung(cungid, 4);
        cungTamHop2 = dichCung(cungid, 8);
        console.log(cungXungChieu, cungTamHop1)
        $(this).addClass("xungChieu");
        $("[cung-id=" + cungXungChieu + "]").addClass("xungChieu");
        $("[cung-id=" + cungTamHop1 + "]").addClass("xungChieu");
        $("[cung-id=" + cungTamHop2 + "]").addClass("xungChieu");
    });
    $("#thienBan").click(function () {
        $("[cung-id]").removeClass("xungChieu");
    });
    function lapLaSo(laso) {
        try {
            console.log(thienBandiaBan)
        }
        catch (error) {
            baoLoi(error);
        }
    }
    $("input#laplaso").click(function () {
        $("#laso").removeClass("anlaso");
        $("#urlLaso").val("");
        $.ajax({
            url: 'api',
            type: 'GET',
            dataType: 'json',
            data: $('form#lstv').serialize(),
            success: function (thienBandiaBan) {
                lapLaSo(thienBandiaBan);
                console.log(thienBandiaBan);
            },
            error: function (thienBandiaBan) { baoLoi(thienBandiaBan); }
        });
    });
    function baoLoi(data) {
        $("#laso").addClass("anlaso");
        alert("Có lỗi, không thể lấy được lá số.");
    }
    $("input#luulaso").click(function () {
        if ($("#laso").is(':hidden')) {
            alert("Hãy an lá số trước khi lưu!");
            return false;
        }
        html2canvas(document.getElementById("laso"), {
            background: '#FFFFFF',
            onrendered: function (canvas) {
                // var ctx = canvas.getContext('2d');
                // ctx.webkitImageSmoothingEnabled = false;
                // ctx.mozImageSmoothingEnabled = false;
                // ctx.imageSmoothingEnabled = false;
                $("#urlLaso").val("");
                var a = document.createElement('a');
                a.href = canvas.toDataURL("image/jpeg").replace("image/jpeg", "image/octet-stream");
                a.download = 'laso.jpg';
                a.click();
            },
            width: 805,
            height: 965
        });
    });

    $("input#uploadLaso").click(function (){
        if ($("#laso").is(':hidden')) {
            alert("Hãy an lá số trước khi upload!");
            return false;
        }

        html2canvas(document.getElementById("laso"),{
            background: '#FFFFFF',
            onrendered: function (canvas){
                canvasData = canvas.toDataURL("image/jpeg").replace("image/jpeg", "image/octet-stream");
                $.ajax({
                    url: uploadLaso,
                    type: "POST",
                    data: {
                        image: canvasData,
                        hoten: $("#hoten").val(),
                        ngaysinh: $("#ngaysinh").val(),
                        thangsinh: $("#thangsinh").val(),
                        namsinh: $("#namsinh").val()
                    },
                    dataType: "json",
                    success: function (response){
                        if (response.error == false){
                            $("#urlLaso").val(response.message);
                            alert("Upload thành công.");
                        }else{
                            alert("Có lỗi, không lưu được lá số trên server.");
                        }

                    }
                }).fail(function(){
                    alert("Có lỗi, không lưu được lá số trên server.");
                });
            }
        });
    });
    function download(strData, strFileName, strMimeType) {
        var D = document, A = arguments, a = D.createElement("a"), d = A[0], n = A[1], t = A[2] || "text/plain";
        //build download link:
        a.href = "data:" + strMimeType + "," + escape(strData);
        if (window.MSBlobBuilder) {
            var bb = new MSBlobBuilder();
            bb.append(strData);
            return navigator.msSaveBlob(bb, strFileName);
        } /* end if(window.MSBlobBuilder) */
        if ('download' in a) {
            a.setAttribute("download", n);
            a.innerHTML = "downloading...";
            D.body.appendChild(a);
            setTimeout(function () {
                var e = D.createEvent("MouseEvents");
                e.initMouseEvent("click", true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                a.dispatchEvent(e);
                D.body.removeChild(a);
            }, 66);
            return true;
        } /* end if('download' in a) */
        ; //end if a[download]?
        //do iframe dataURL download:
        var f = D.createElement("iframe");
        D.body.appendChild(f);
        f.src = "data:" + (A[2] ? A[2] : "application/octet-stream") + (window.btoa ? ";base64" : "") + "," + (window.btoa ? window.btoa : escape)(strData);
        setTimeout(function () {
            D.body.removeChild(f);
        }, 333);
        return true;
    } /* end download() */
});
