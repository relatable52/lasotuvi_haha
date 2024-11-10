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
    const wrapper = radio.closest('.gender_btn_wrapper');

    // Remove the selected class from all containers
    wrapper.querySelectorAll('.radio_btn').forEach(container => {
        container.classList.remove('selected');
    });

    // Add the selected class to the clicked radio button's parent label
    radio.parentElement.classList.add('selected');
}

function toggle(){
    var formContainer = document.getElementById('form-container');
    formContainer.classList.toggle('hide');

    var chartContainer = document.getElementById('laso');
    chartContainer.classList.toggle('hide');
}

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
                    lasoData = thienBandiaBan;
                    lapLaSo(lasoData);
                    $("#velaso1").click(velaso1);
                    $("#velaso2").click(velaso2);
                    $('#velaso3').click(velaso3)
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
            velaso(laso, 1);
        }
    }
)