const width = 720;
const height = 1020;
var scale = 1;

var lasoData = null;

function velaso(laso, loaiLaSo = 0){
    // Define the SVG canvas dimensions
    scale = 1;
    const cell_width = width/4;
    const cell_height = height/4;

    // Create the SVG container
    document.getElementById("chart").innerHTML = '';
    document.getElementById("printable").innerHTML = '';
    const chart_svg = d3.select("#chart")
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("viewBox", `0 0 ${width} ${height}`)
        .attr("id", "chart_svg")
        .attr("preserveAspectRatio", "xMinYMin meet");

    var printable = d3.select("#printable")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("viewBox", `0 0 ${width} ${height}`)
    .append("use")
    .attr("xlink:href", "#chart_svg");
   
    const svg = chart_svg.append("g");

    svg.append("rect")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", width)
        .attr("height", height)
        .attr("fill", "rgb(242, 242, 234)")
        .attr("stroke", "black");

    svg.append("rect")
        .attr("x", cell_width)
        .attr("y", cell_height)
        .attr("width", cell_width*2)
        .attr("height", cell_height*2)
        .attr("fill", "none")
        .attr("stroke", "black")

    for(let i=1; i<4; i++){
        svg.append("line")
            .attr("x1", 0)
            .attr("y1", cell_height*i)
            .attr("x2", cell_width)
            .attr("y2", cell_height*i)
            .attr("stroke", "black");
        svg.append("line")
            .attr("x1", 3*cell_width)
            .attr("y1", cell_height*i)
            .attr("x2", width)
            .attr("y2", cell_height*i)
            .attr("stroke", "black");
        svg.append("line")
            .attr("x1", cell_width*i)
            .attr("y1", 0)
            .attr("x2", cell_width*i)
            .attr("y2", cell_height)
            .attr("stroke", "black");
        svg.append("line")
            .attr("x1", cell_width*i)
            .attr("y1", cell_height*3)
            .attr("x2", cell_width*i)
            .attr("y2", height)
            .attr("stroke", "black");
    }

    svg.append("defs")
        .append("marker")
        .attr("id", "arrowhead")
        .attr("viewBox", "0 -5 10 10")
        .attr("refX", 10)  // Controls position of the arrowhead along the path
        .attr("refY", 0)
        .attr("markerWidth", 6)
        .attr("markerHeight", 6)
        .attr("orient", "auto")  // Keeps arrowhead pointed along the path direction
        .append("path")
        .attr("d", "M0,-5L10,0L0,5")
        .attr("fill", "red");

    function addText(text, x, y, style="", justify="middle"){
        svg.append("text")
        .attr("class", style)
        .attr("x", x)    
        .attr("y", y)   
        .attr("dy", ".35em")          
        .attr("text-anchor", justify)
        .attr("alignment-baseline", "center")      
        .text(text);           
    }

    function addArrow(x1, y1, x2, y2, style, label){
        svg.append("line")
            .attr("x1", x1)  // Starting point x
            .attr("y1", y1)  // Starting point y
            .attr("x2", x2) // Ending point x
            .attr("y2", y2) // Ending point y
            .attr("stroke", "black")
            .attr("stroke-width", 1)
            .attr("marker-end", "url(#arrowhead)")
            .attr("class", style);

        const offset = 20; // Distance from the arrow tip
        const angle = Math.atan2(y2 - y1, x2 - x1);  // Angle of the line

        const arrowSize = 8;
        // Calculate triangle points based on the angle
        const arrowX1 = x2 - arrowSize * Math.cos(angle - Math.PI / 6);
        const arrowY1 = y2 - arrowSize * Math.sin(angle - Math.PI / 6);
        const arrowX2 = x2 - arrowSize * Math.cos(angle + Math.PI / 6);
        const arrowY2 = y2 - arrowSize * Math.sin(angle + Math.PI / 6);

        // Append the triangle as a polygon
        svg.append("polygon")
            .attr("points", `${x2},${y2} ${arrowX1},${arrowY1} ${arrowX2},${arrowY2}`)
            .attr("class", style);

        const labelX = x2 + offset * Math.cos(angle+3*Math.PI/6);
        const labelY = y2 + offset * Math.sin(angle+3*Math.PI/6);

        svg.append("text")
            .attr("x", labelX)
            .attr("y", labelY)
            .attr("dy", ".35em")
            .text(label)
            .attr("text-anchor", "middle")
            .attr("alignment-baseline", "center")  
            .attr("class", style);
    }

    var cung = {
        "Dần": [1, 4],
        "Mão": [1, 3],
        "Thìn": [1, 2],
        "Tỵ": [1, 1],
        "Ngọ": [2, 1],
        "Mùi": [3, 1],
        "Thân": [4, 1],
        "Dậu": [4, 2],
        "Tuất": [4, 3],
        "Hợi": [4, 4],
        "Tý": [3, 4], 
        "Sửu": [2, 4], 
    };

    var up = cell_height/16;
    var left = cell_width*0.02;
    var down = 15*cell_height/16;
    var stepy = cell_height*0.0545;
    var right = cell_width*0.98;
    var stepx = cell_width/7;
    var middle_left = cell_width*0.05;
    var middle_right = cell_width*0.95;

    function drawCell(data, loaiLaSo = loaiLaSo){
        var soSaoChinh = 0;
        var soSaoTot = 0;
        var soSaoXau = 0;
        var saohoaText = '';
        var saos = (loaiLaSo == 3)?data.cungSao.slice().reverse():data.cungSao;
        for(let sao of saos){
            if(sao.saoLoai == 1){
                soSaoChinh += 1;
                chinhTinhText = sao.saoTen;
                if(sao.saoDacTinh !== null){
                    chinhTinhText += " (" + sao.saoDacTinh + ")" ;
                } 
                addText(
                    chinhTinhText, 
                    (cung[data.cungTen][0]-1)*cell_width+cell_width/2, 
                    (cung[data.cungTen][1]-1)*cell_height+up+(soSaoChinh+0.5)*stepy,
                    sao.cssSao + " bold"
                );
            }
            if(sao.vongTrangSinh == 1){
                addText(sao.saoTen, (cung[data.cungTen][0]-1)*cell_width+cell_width/2, (cung[data.cungTen][1]-1)*cell_height+down, "small bold");
            }
            if(loaiLaSo != 3){
                if(sao.vongTrangSinh === 0 && sao.saoLoai !==1 && sao.saoLoai < 10){
                    var saoTotText = '';
                    if(loaiLaSo == 1){
                        saoTotText = sao.saoTen;
                    }
                    else if(loaiLaSo == 2){
                        saoTotText = sao.tenNamPhai;
                    }
                    if(sao.saoDacTinh !== null){
                        saoTotText += " (" + sao.saoDacTinh + ")" ;
                    }
                    if(sao.saoLoai != 9 || loaiLaSo == 2){
                        soSaoTot += 1;
                        addText(
                            saoTotText,  
                            (cung[data.cungTen][0]-1)*cell_width+middle_left, (cung[data.cungTen][1]-1)*cell_height+up+(soSaoTot*0.9+3)*stepy, 
                            'small ' + sao.cssSao, 
                            'start'
                        );
                    }
                }
                if(sao.vongTrangSinh === 0 && sao.saoLoai !==1 && sao.saoLoai > 10){
                    var saoXauText = '';
                    if(loaiLaSo == 1){
                        saoXauText = sao.saoTen;
                    }
                    else if(loaiLaSo == 2){
                        saoXauText = sao.tenNamPhai;
                    }
                    if(sao.saoDacTinh !== null){
                        saoXauText += " (" + sao.saoDacTinh + ")" ;
                    }
                    if(sao.saoLoai != 21 || loaiLaSo == 2){
                        soSaoXau += 1;
                        addText(
                            saoXauText,
                            (cung[data.cungTen][0]-1)*cell_width+middle_right, (cung[data.cungTen][1]-1)*cell_height+up+(soSaoXau*0.9+3)*stepy, 
                            'small ' + sao.cssSao, 
                            'end');
                    }
                }
            }
            else{
                const saoIDs = [57, 58, 61, 62];
                const hoaIDs = [92, 93, 94, 95];
                const hoaChu = ['Ⓒ', 'Ⓑ', 'Ⓐ', 'Ⓓ']
                if(saoIDs.includes(sao.saoID)){
                    soSaoChinh += 1;
                    chinhTinhText = sao.saoTen;
                    if(sao.saoDacTinh !== null){
                        chinhTinhText += " (" + sao.saoDacTinh + ")" ;
                    } 
                    addText(
                        chinhTinhText, 
                        (cung[data.cungTen][0]-1)*cell_width+cell_width/2, 
                        (cung[data.cungTen][1]-1)*cell_height+up+(soSaoChinh+0.5)*stepy,
                        sao.cssSao + " bold"
                    );
                }
                if(hoaIDs.includes(sao.saoID)){
                    saohoaText += hoaChu[sao.saoID-92];
                }
            }
        }

        if(loaiLaSo == 3){
            var chu = ['A', 'B', 'C', 'D'];
            var viTri = {
                1: 0,
                2: 0,
                3: 0,
                4:1,
                5:1,
                6:2,
                7:2,
                8:2,
                9:2,
                10:3,
                11:3,
                12:0,
            }
            var dau = [
                [0.5, -1],
                [-0.5, -1],
                [-1, -1],
                [-1, -0.5], 
                [-1, 0.5],
                [-1, 1],
                [-0.5, 1], 
                [0.5, 1],
                [1, 1],
                [1, 0.5],
                [1, -0.5],
                [1, -1]
            ]
            var x1, y1, x2, y2;
            if(viTri[data.cungSo] == 0){
                x1 = (cung[data.cungTen][0]-1)*cell_width + cell_width/2;
                y1 = (cung[data.cungTen][1]-1)*cell_height + cell_height*5/6;
                x2 = (cung[data.cungTen][0]-1)*cell_width + cell_width/2;
                y2 = (cung[data.cungTen][1]-1)*cell_height + cell_height*7/6;
            }
            if(viTri[data.cungSo] == 1){
                x1 = (cung[data.cungTen][0]-1)*cell_width + cell_width/6;
                y1 = (cung[data.cungTen][1]-1)*cell_height + cell_height/2;
                x2 = (cung[data.cungTen][0]-1)*cell_width - cell_width/6;
                y2 = (cung[data.cungTen][1]-1)*cell_height + cell_height/2;
            }
            if(viTri[data.cungSo] == 2){
                x1 = (cung[data.cungTen][0]-1)*cell_width + cell_width/2;
                y1 = (cung[data.cungTen][1]-1)*cell_height + cell_height/6;
                x2 = (cung[data.cungTen][0]-1)*cell_width + cell_width/2;
                y2 = (cung[data.cungTen][1]-1)*cell_height - cell_height/6;
            }
            if(viTri[data.cungSo] == 3){
                x1 = (cung[data.cungTen][0]-1)*cell_width + cell_width*5/6;
                y1 = (cung[data.cungTen][1]-1)*cell_height + cell_height/2;
                x2 = (cung[data.cungTen][0]-1)*cell_width + cell_width*7/6;
                y2 = (cung[data.cungTen][1]-1)*cell_height + cell_height/2;
            }
            let lyTamText = '';
            let huongTamText = '';
            for(const caigido of data.lyTamID){
                lyTamText += ' ' + chu[caigido];
            }
            for(const caigido of data.huongTamID){
                huongTamText += ' ' + chu[caigido];
            }
            if(data.lyTamID.length > 0){
                addArrow(x1, y1, x2, y2, "arrow", lyTamText);
            }
            if(data.huongTamID.length > 0){
                x2 = width/2 + cell_width*dau[data.cungSo-1][0];
                y2 = height/2 - cell_height*dau[data.cungSo-1][1];
                cungDoi = (data.cungSo - 1 + 6)%12;
                x1 = width/2 + cell_width*dau[cungDoi][0];
                y1 = height/2 - cell_height*dau[cungDoi][1];
                addArrow(x1, y1, x2, y2, "arrow", huongTamText);
            }
            addText(saohoaText, (cung[data.cungTen][0]-0.5)*cell_width, (cung[data.cungTen][1]-0.5)*cell_height, "hoaChu", "middle");
        }

        var cungChuText = data.cungChu + String(data.cungThan?"<Thân>":"");

        addText(data.canDiaBanTen + data.cungTen, (cung[data.cungTen][0]-1)*cell_width+left, (cung[data.cungTen][1]-1)*cell_height+up, "small bold", "start");
        // addText(data.cungTieuHan, (cung[data.cungTen][0]-1)*cell_width+left, (cung[data.cungTen][1]-1)*cell_height+down-stepy, "smaller");
        addText(data.luuDaiHan, (cung[data.cungTen][0]-1)*cell_width+left, (cung[data.cungTen][1]-1)*cell_height+down, "small bold", "start");
        addText(data.luuTieuHan, (cung[data.cungTen][0]-1)*cell_width+right, (cung[data.cungTen][1]-1)*cell_height+down, "small bold", "end");
        addText(data.cungDaiHan, (cung[data.cungTen][0]-1)*cell_width+right, (cung[data.cungTen][1]-1)*cell_height+up, "small bold", "end");
        addText(cungChuText, (cung[data.cungTen][0]-1)*cell_width+cell_width/2, (cung[data.cungTen][1]-1)*cell_height+up, "small bold");
    }

    var tb = laso['thienBan'];
    var data = laso['thapNhiCung'];
    var canNam = tb.canNam;
    var chieu = tb.gioiTinh*tb.amDuongNamSinhId;
    var chiNam = tb.chiNam;

    var tuan = 0;
    var triet = 0;

    for(let i=1; i<13; i++){
        cell = data[i];
        drawCell(cell, loaiLaSo);
        let start = (24+(i - chiNam))%12+1; 
        let tuoiText = start;
        for(let j = 1; j < 9; j++){
            tuoiText += ", " + (start + 12*j);
        }
        addText(tuoiText, (cung[cell.cungTen][0]-1)*cell_width+cell_width/2, (cung[cell.cungTen][1]-1)*cell_height+down-stepy, "smaller blue bold");
        if('tuanTrung' in cell){
            tuan = i;
        }
        if('trietLo' in cell){
            triet = i;
        }
    }

    vitriTuanTriet = {
        2: [width/2, 0.75*height],
        4: [width/8, 0.75*height],
        6: [width/8, 0.25*height],
        8: [width/2, 0.25*height],
        10: [7*width/8, 0.25*height],
        12: [7*width/8, 0.75*height]
    }

    rect_width = 1.5*cell_width/8;
    rect_height = 1.2*cell_height/20;
    if(tuan != triet){
        svg.append("rect")
        .attr("x", vitriTuanTriet[triet][0] - rect_width/2)
        .attr("y", vitriTuanTriet[triet][1] - rect_height/2)
        .attr("width", rect_width)
        .attr("height", rect_height)
        .attr("class", "rect-style");
        svg.append("rect")
        .attr("x", vitriTuanTriet[tuan][0] - rect_width/2)
        .attr("y", vitriTuanTriet[tuan][1] - rect_height/2)
        .attr("width", rect_width)
        .attr("height", rect_height)
        .attr("class", "rect-style");
        addText("Triệt", vitriTuanTriet[triet][0], vitriTuanTriet[triet][1], "small bold tuantriet", "middle");
        addText("Tuần", vitriTuanTriet[tuan][0], vitriTuanTriet[tuan][1], "small bold tuantriet", "middle");
    }
    else{
        svg.append("rect")
        .attr("x", vitriTuanTriet[tuan][0] - rect_width)
        .attr("y", vitriTuanTriet[tuan][1] - rect_height/2)
        .attr("width", rect_width*2)
        .attr("height", rect_height)
        .attr("class", "rect-style");
        addText("Tuần - Triệt", vitriTuanTriet[triet][0], vitriTuanTriet[triet][1], "small bold tuantriet", "middle");
    }
    
    

    var left1 = cell_width*1.25;
    var left2 = cell_width*1.8;
    var up1 = cell_height*1.4;
    var stepy1 = cell_width/10;
    var stepx1 = cell_width/6;

    var thienBanText = [
        ["Họ tên", 0, tb.ten, ""],
        ["Năm", 1, tb.namDuong, tb.canNamTen + " " + tb.chiNamTen],
        ["Tháng", 2, tb.thangDuong, tb.canThangTen + " " + tb.chiThangTen],
        ["Ngày", 3, tb.ngayDuong, tb.canNgayTen + " " + tb.chiNgayTen],
        ["Giờ", 4, tb.gioSinh, ""],
        ["Năm xem", 6, tb.namxem, ""],
        ["Tuổi", 7, tb.tuoi, ""],
        ["Âm Dương", 9, tb.amDuongNamSinh + " " + tb.namNu, ""],
        ["Mệnh", 10, tb.banMenh, ""],
        ["Cục", 11, tb.tenCuc, ""],
        ["Thân chủ", 14, tb.thanChu, ""],
        ["Mệnh chủ", 13, tb.menhChu, ""],
        [tb.amDuongMenh, 16, ""],
        [tb.sinhKhac, 17, ""]
    ]
    addText('LÁ SỐ TỬ VI', width/2, 1.2*height/4, "title blue");
    addText('https://khamthientuhoa.com.vn', width/2, 1.3*height/4, "thienban red");
    addText('Fb/khamthientuhoaminhphuong/', width/4 + stepx1/2, 3*height/4 - 2.2*stepy1, "thienban red nghieng", "start");
    //addText('Fb/khamthientuhoaminhphuong/', width/4 + stepx1/2, 3*height/4 - 1.2*stepy1, "thienban red nghieng", "start");
    for(let i=0; i<thienBanText.length; i++){
        addText(thienBanText[i][0], left1, up1 + thienBanText[i][1]*stepy1, "thienban bold", "start");
        addText(thienBanText[i][2], left2, up1 + thienBanText[i][1]*stepy1, "thienban blue bold", "start");
        addText(thienBanText[i][3], left2 + 2.5*stepx1, up1 + thienBanText[i][1]*stepy1, "thienban blue bold", "start");
    }

    d3.xml("static/bitmap1.svg")  // Replace with the path to your external SVG file
    .then(function(data) {
        const externalSvg = data.documentElement;

        // Option 1: Change the location using x and y attributes
        d3.select(externalSvg)
        .attr("x", 3*width/4 - 115)  // Move the external SVG to x=100
        .attr("y", 3*height/4 - 115)  // Move the external SVG to y=100
        .attr("width", 110)
        .attr("height", 110)
        .attr("preserveAspectRatio", "xMinYMin meet");

        // Option 2: Use transform to move (this is more flexible)
        // d3.select(externalSvg)
        //   .attr("transform", "translate(100, 100)");  // Moves the external SVG by (100, 100)

        // Append the external SVG to the parent SVG
        svg.node().appendChild(externalSvg);
    })
    .catch(function(error) {
        console.log("Error loading external SVG: ", error);
    });
    
    // // Define the zoom behavior
    // const zoom = d3.zoom()
    //     .scaleExtent([0.5, 10]) // Set the scale limits (min and max zoom levels)
    //     .translateExtent([[0,0], [width, height]])
    //     .on("zoom", function (event) {
    //         svg.attr("transform", event.transform); // Apply the zoom transformation to the inner `g` element
    //     });

    // // Apply zoom behavior to the SVG
    // chart_svg.call(zoom);

    // const resetButton = document.getElementById("resetButton");
    // resetButton.addEventListener("click", function() {
    //     // Reset the zoom and pan to the initial state
    //     chart_svg.call(zoom.transform, d3.zoomIdentity); // Reset to default zoom and pan
    // });
    if(loaiLaSo == 3){
        const scaleFactor = 0.85;
        const translateX = (width * (1 - scaleFactor)) / 2;
        const translateY = (height * (1 - scaleFactor)) / 2;
        svg.style("transform", `translate(${translateX}px, ${translateY}px) scale(${scaleFactor})`);
    }
}

function zoomIn(){
    scale += 0.1;
    if (scale > 5) scale = 5;
    scaleSVG(scale);
}

function zoomOut(){
    scale -= 0.1;
    if (scale < 0.3) scale = 0.3;
    scaleSVG(scale);
}

function resetZoom(){
    scale = 1;
    scaleSVG(1);
}

function fitToWidth(){
    const chart = d3.select("#chart").node()
    const containerWidth = chart.offsetWidth;
    scale = containerWidth/width*0.95;
    if(scale > 5) scale = 5;
    if(scale < 0.3) scale = 0.3;
    scaleSVG(scale);
}

function fitToHeight(){
   const chart = d3.select("#chart").node()
    const containerHeight = chart.offsetHeight;
    scale = containerHeight/height*0.95;
    if(scale > 5) scale = 5;
    if(scale < 0.3) scale = 0.3;
    scaleSVG(scale);
}

function scaleSVG(factor){
    const svgElement = d3.select("#chart svg");
    svgElement.attr("width", width*factor).attr("height", height*factor);
}

function velaso1(){
    velaso(lasoData, 1);
}

function velaso2(){
    velaso(lasoData, 2);
}

function velaso3(){
    velaso(lasoData, 3);
}

function download(){
    const svgElement = d3.select("#chart svg").node();
    var config = {
        filename: 'laso',
    }
    d3_save_svg.save(svgElement, config);
}

// function print(){
//     const svgElement = d3.select("#chart svg").node();
//     const svgString = preprocess(svgElement).source;
//     const svgHtml = `
//         <html>
//         <head>
//             <title>Print SVG</title>
//         </head>
//         <body onload="window.print()">
//             ${svgString}
//         </body>
//         <script type="text/javascript">
//             window.onfocus=function(){ window.close();}
//         </script>
//         </html>
//     `;

//     console.log(svgHtml);

//     // Open a new window
//     const printWindow = window.open();
//     printWindow.document.write(svgHtml);
//     printWindow.document.close();
// }