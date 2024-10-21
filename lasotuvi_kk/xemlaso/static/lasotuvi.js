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
        yearRange: "1900:2024"   // Year range for selection
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
        .attr("fill", "rgb(230, 230, 200)");

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

    function addText(text, x, y){
        svg.append("text")
        .attr("x", x)    
        .attr("y", y)   
        .attr("dy", ".35em")          
        .attr("text-anchor", "middle")
        .style("font-size", "12px")   
        .style("fill", "black")       
        .text(text);           
    }

    function drawCell(data, canNam, i){
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

        var can = [
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
        ];

        var canTen = can[(canNam%5*2 + i)%10];
        addText(canTen + data.cungTen, (cung[data.cungTen][0]-1)*cell_width+cell_width/6, (cung[data.cungTen][1]-1)*cell_height+cell_height/12);
        addText(data.cungTieuHan, (cung[data.cungTen][0]-1)*cell_width+cell_width/6, (cung[data.cungTen][1]-1)*cell_height+11*cell_height/12);
        addText(data.cungDaiHan, (cung[data.cungTen][0]-1)*cell_width+7*cell_width/8, (cung[data.cungTen][1]-1)*cell_height+cell_height/12);
        var menh = data.cungChu.toLowerCase().split(' ').map(
            (word, index) => {
                return word.charAt(0).toUpperCase() + word.slice(1);
            }
        ).join(' ')
        addText(menh, (cung[data.cungTen][0]-1)*cell_width+cell_width/2, (cung[data.cungTen][1]-1)*cell_height+cell_height/12);
        addText("Lá số tử vi", width/2, 1.1*height/4);
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
