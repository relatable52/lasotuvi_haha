const selectElement = document.getElementById('namxem');
const min = 1900;  // Minimum bound
const max = 2100; // Maximum bound

for (let i = min; i <= max; i++) {
    const option = document.createElement('option');
    option.value = i;
    option.text = i;
    if(i==2030){
        option.selected = true;
    }
    selectElement.appendChild(option);
}

function selectRadio(radio) {
    // Remove the selected class from all containers
    document.querySelectorAll('.radio_btn').forEach(container => {
        container.classList.remove('selected');
    });

    // Add the selected class to the clicked radio button's parent label
    radio.parentElement.classList.add('selected');
}

function toggle(){
    var formContainer = document.getElementById('form-container');
    formContainer.classList.toggle('hide')

    var chartContainer = document.getElementById('laso')
    chartContainer.classList.toggle('hide')
}

$(function() {
    $("#date-picker").datepicker({
        dateFormat: "dd/mm/yy",  // Custom date format
        changeMonth: true,       // Dropdown for selecting month
        changeYear: true,        // Dropdown for selecting year
        yearRange: "1900:2100"   // Year range for selection
    });
});

$(document).ready(
    function(){
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
            console.log($('form#lstv').serialize())
        });
        function baoLoi(data) {
            $("#laso").addClass("anlaso");
            alert("Có lỗi, không thể lấy được lá số.");
        }
        function lapLaSo(laso) {
            console.log(laso);
            velaso(laso);
        }
    }
)

function velaso(laso){
    // Define the SVG canvas dimensions
    const width = 584;
    const height = 804;
    const cell_width = width/4;
    const cell_height = height/4;

    // Create the SVG container
    document.getElementById("chart").innerHTML = '';
    const chart_svg = d3.select("#chart")
        .append("svg")
        .attr("width", width)
        .attr("height", height);
    
    const svg = chart_svg.append("g");

    svg.append("rect")
        .attr("x", 0)
        .attr("y", 0)
        .attr("width", width)
        .attr("height", height)
        .attr("fill", "rgb(230, 230, 200)")
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

    function drawCell(data){
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
        
        up = cell_height/14;
        left = cell_width/7;
        down = 13*cell_height/14;
        stepy = cell_height/14;
        right = 6*cell_width/7;
        stepx = cell_width/7;
        middle_left = cell_width*0.05;
        middle_right = cell_width*0.55;

        soSaoChinh = 0;
        soSaoTot = 0;
        soSaoXau = 0;
        for(let sao of data.cungSao){
            if(sao.vongTrangSinh == 1){
                addText(sao.saoTen, (cung[data.cungTen][0]-1)*cell_width+cell_width/2, (cung[data.cungTen][1]-1)*cell_height+down, "small");
            }
            if(sao.saoLoai == 1){
                soSaoChinh += 1;
                chinhTinhText = sao.saoTen;
                if(sao.saoDacTinh !== null){
                    chinhTinhText += " (" + sao.saoDacTinh + ")" ;
                } 
                addText(
                    chinhTinhText, 
                    (cung[data.cungTen][0]-1)*cell_width+cell_width/2, 
                    (cung[data.cungTen][1]-1)*cell_height+up+soSaoChinh*stepy,
                    sao.cssSao
                );
            }
            if(sao.vongTrangSinh === 0 && sao.saoLoai !==1 && sao.saoLoai < 10){
                soSaoTot += 1;
                saoTotText = sao.saoTen;
                if(sao.saoDacTinh !== null){
                    saoTotText += " (" + sao.saoDacTinh + ")" ;
                }
                addText(
                    saoTotText,  
                    (cung[data.cungTen][0]-1)*cell_width+middle_left, (cung[data.cungTen][1]-1)*cell_height+up+(soSaoTot*0.9+2.4)*stepy, 
                    'small ' + sao.cssSao, 
                    'start'
                );
            }
            if(sao.vongTrangSinh === 0 && sao.saoLoai !==1 && sao.saoLoai > 10){
                soSaoXau += 1;
                saoXauText = sao.saoTen;
                if(sao.saoDacTinh !== null){
                    saoXauText += " (" + sao.saoDacTinh + ")" ;
                }
                addText(
                    saoXauText,
                    (cung[data.cungTen][0]-1)*cell_width+middle_right, (cung[data.cungTen][1]-1)*cell_height+up+(soSaoXau*0.9+2.4)*stepy, 
                    'small ' + sao.cssSao, 
                    'start');
            }
        }

        addText(data.canDiaBanTen + data.cungTen, (cung[data.cungTen][0]-1)*cell_width+left, (cung[data.cungTen][1]-1)*cell_height+up, "small");
        addText(data.cungTieuHan, (cung[data.cungTen][0]-1)*cell_width+left, (cung[data.cungTen][1]-1)*cell_height+down-stepy, "small");
        addText(data.luuDaiHan, (cung[data.cungTen][0]-1)*cell_width+left, (cung[data.cungTen][1]-1)*cell_height+down, "small");
        addText(data.luuTieuHan, (cung[data.cungTen][0]-1)*cell_width+right, (cung[data.cungTen][1]-1)*cell_height+down, "small");
        addText(data.cungDaiHan, (cung[data.cungTen][0]-1)*cell_width+right, (cung[data.cungTen][1]-1)*cell_height+up, "small");
        addText(data.cungChu, (cung[data.cungTen][0]-1)*cell_width+cell_width/2, (cung[data.cungTen][1]-1)*cell_height+up, "small bold");
        addText('Lá số tử vi', width/2, 1.1*height/4, "title");
    }

    var tb = laso['thienBan'];
    var data = laso['thapNhiCung'];
    var canNam = tb.canNam;

    for(i=1; i<13; i++){
        cell = data[i]
        drawCell(cell, canNam, i);
    }
    
    // Define the zoom behavior
    const zoom = d3.zoom()
        .scaleExtent([0.5, 10]) // Set the scale limits (min and max zoom levels)
        .on("start", function() {
            // Change cursor to grabbing when zooming starts
            d3.select("#chart").classed("grabbing", true);
        })
        .on("zoom", function (event) {
            svg.attr("transform", event.transform); // Apply the zoom transformation to the inner `g` element
        })
        .on("end", function() {
            // Revert to grab cursor when zooming ends
            d3.select("#chart").classed("grabbing", false);
        });

    // Apply zoom behavior to the SVG
    chart_svg.call(zoom);

    const resetButton = document.getElementById("resetButton");
    resetButton.addEventListener("click", function() {
        // Reset the zoom and pan to the initial state
        chart_svg.call(zoom.transform, d3.zoomIdentity); // Reset to default zoom and pan
    });
}
