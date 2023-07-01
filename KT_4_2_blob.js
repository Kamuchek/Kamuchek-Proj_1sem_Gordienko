// Вариант 24: Составить программу вычисления функции y = n∑i=1 (4bi^2)/(1+I cosi)
function calculateY(n, b) {
    let sum = 0;

    for (let i = 1; i <= n; i++) {
        let term = (4 * b * Math.pow(i, 2)) / (1 + i * Math.cos(i));
        sum += term;
    }

    return sum;
}

// Пример
let n = 5; // Количество итераций
let b = 2; // Коэффициент

let result = calculateY(n, b);
console.log("Результат вычисления функции Y: " + result);
