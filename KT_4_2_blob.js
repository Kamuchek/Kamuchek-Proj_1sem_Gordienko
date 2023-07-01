// Вариант 24: Составить программу вычисления функции y = n∑i=1 (4bi^2)/(1+I cosi)
function calculateY(n, b) {
    var sum = 0;

    for (var i = 1; i <= n; i++) {
        var term = (4 * b * Math.pow(i, 2)) / (1 + i * Math.cos(i));
        sum += term;
    }

    return sum;
}

// Пример
var n = 5; // Количество итераций
var b = 2; // Коэффициент

var result = calculateY(n, b);
console.log("Результат вычисления функции Y: " + result);
