const currentYear = new Date().getFullYear();

const yearSelect = document.getElementById('year-select');
const monthSelect = document.getElementById('month-select');
const daySelect = document.getElementById('day-select');

var amLich = document.querySelector('input[name="amLich"]:checked').value;
var selectedCalendar = (amLich === "on")?"lunar":"gregorian";

document.getElementById('amlich').addEventListener('change', initializeDatePicker);
document.getElementById('duonglich').addEventListener('change', initializeDatePicker);

yearSelect.addEventListener('change', onYearChange);
monthSelect.addEventListener('change', onMonthChange);

initializeDatePicker();

function initializeDatePicker() {
    amLich = document.querySelector('input[name="amLich"]:checked').value;
    selectedCalendar = (amLich === "on")?"lunar":"gregorian";
    populateYears();
    if (selectedCalendar === "gregorian") {
        populateGregorianMonths();
        populateDaysGregorian();
    } else {
        populateLunarMonths();
        populateDaysLunar();
    }
}

function onYearChange(){
    if (selectedCalendar === "gregorian") {
        populateGregorianMonths();
        populateDaysGregorian();
    } else {
        populateLunarMonths();
        populateDaysLunar();
    }
}

function onMonthChange(){
    if (selectedCalendar === "gregorian") {
        populateDaysGregorian();
    } else {
        populateDaysLunar();
    }
}

function populateYears() {
    yearSelect.innerHTML = '';
    
    const years = lunarData.map(year => parseInt(year['Gregorian year']));
    const canchi = lunarData.map(year => year['Chinese year']);

    for(let index = 0; index < years.length; index++){
        const option = document.createElement('option');
        option.value = years[index];
        option.textContent = years[index];
        if(selectedCalendar === 'lunar'){
            option.textContent += " " + canchi[index];
        }
        if (years[index] === currentYear) option.selected = true;
        yearSelect.appendChild(option);
    }
}

// Populate Gregorian months
function populateGregorianMonths() {
    monthSelect.innerHTML = '';
    daySelect.innerHTML = '';

    for (let i = 1; i <= 12; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = `Tháng ${i}`;
        if (i == 1) option.selected = true;
        monthSelect.appendChild(option);
    }
}

// Populate Lunar months based on selected year data
function populateLunarMonths() {
    monthSelect.innerHTML = '';
    daySelect.innerHTML = '';

    let theyear = yearSelect.value;
    let yearData = lunarData.find(y => y['Gregorian year'] === theyear);
    
    yearData.Months.forEach((monthData, index) => {
        const option = document.createElement('option');
        option.value = index+1;
        option.textContent = monthData.month;
        if (index == 0) option.selected = true;
        monthSelect.appendChild(option);
    });
}

function getDaysInMonth(year, month) {
    return new Date(year, month, 0).getDate();
}

function populateDaysGregorian() {
    daySelect.innerHTML = '';

    let theyear = yearSelect.value;
    let themonth = monthSelect.value;

    let daysInMonth = getDaysInMonth(theyear, themonth);

    for (let day = 1; day <= daysInMonth; day++) {
        const option = document.createElement('option');
        option.value = `${day}/${themonth}/${theyear}`;
        option.textContent = day;
        if (day == 1) option.selected = true;
        daySelect.appendChild(option);
    }
}

// Populate days for Lunar month based on selected month data
function populateDaysLunar() {
    daySelect.innerHTML = '';

    theyear = yearSelect.value;
    themonth = monthSelect.value;

    let monthData = lunarData.find(y => y['Gregorian year'] === theyear).Months[themonth-1];
    let start_date = monthData.start_date;

    for (let day = 1; day <= monthData.number_of_days; day++) {
        const option = document.createElement('option');
        option.value = calculateLunarDate(start_date, day, theyear);
        option.textContent = day;
        if (day == 1) option.selected = true;
        daySelect.appendChild(option);
    }
}

function calculateLunarDate(startdate, day, year){
    let [startMonth, startDay] = startdate.split('-').map(Number);
    let startYear = year;
    if (startMonth > 12){
        startMonth = 1;
        startYear ++;
    }
    let date = new Date(startYear, startMonth - 1, startDay + day - 1);
    let tday = date.getDate().toString().padStart(2, '0');
    let tmonth = (date.getMonth() + 1).toString().padStart(2, '0'); // Months are 0-based
    let tyear = date.getFullYear();
    
    return `${tday}/${tmonth}/${tyear}`;
}


