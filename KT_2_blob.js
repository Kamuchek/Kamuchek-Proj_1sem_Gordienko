// Вариант 24: Составить программу вычисления функции: y = x - 3 , е с л и X < 2, y = 2x^2 -1 , е с л и X ≥ 2
function calculateY(x) {
    if (x < 2) {
        return x - 3;
    } else {
        return (2 * Math.pow(x, 2)) - 1;
    }
}

// Пример использования функции
var x = 3; // Задайте значение переменной x, для которого нужно вычислить Y
var result = calculateY(x);
console.log("Результат вычисления функции Y: " + result);
