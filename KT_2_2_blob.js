// вариант 24: Составить программу вычисления функции: y= x+5,еслиX<-4,   y= 7x -1,если -4 ≤ x ≤5,  y= 1-x^2,еслиX>5
function calculateY(x) {
    if (x < -4) {
        return x + 5;
    } else if (x >= -4 && x <= 5) {
        return 7 * x - 1;
    } else {
        return 1 - Math.pow(x, 2);
    }
}

// Пример использования функции
let x = 6; // Задайте значение переменной x, для которого нужно вычислить Y
let result = calculateY(x);
console.log("Результат вычисления функции Y: " + result);
