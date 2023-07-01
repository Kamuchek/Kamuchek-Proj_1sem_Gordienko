// Вариант 23: Дан номер месяца — целое число в диапазоне 1-12 (1 — январь, 2 — февраль и т. д.). Определить количество дней в этом месяце для невисокосного года.
function getDaysInMonth(month) {
    var days;

    switch (month) {
        case 2: // Февраль
            days = 28;
            break;
        case 4: // Апрель
        case 6: // Июнь
        case 9: // Сентябрь
        case 11: // Ноябрь
            days = 30;
            break;
        default: // Все остальные месяцы
            days = 31;
            break;
    }

    return days;
}

// Пример
var month = 7; // Номер месяца

var daysInMonth = getDaysInMonth(month);
console.log("Количество дней в указанном месяце: " + daysInMonth);
