function celsiusToFahrenheit(celsius) {
  return celsius * (9 / 5) + 32;
}

console.log(celsiusToFahrenheit(0)); // 32
console.log(celsiusToFahrenheit(100)); // 212

function average(numbers) {
  sum = 0;
  for (let number of numbers) {
    sum += number;
  }
  return sum / numbers.length;
}
console.log(average([10, 20, 30]));
