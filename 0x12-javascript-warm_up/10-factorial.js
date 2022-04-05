#!/usr/bin/node

<<<<<<< HEAD
function factorial (n) {
  if (n > 1) {
    return (n * factorial(n - 1));
  }
  return 1;
}

console.log(factorial(Number(process.argv[2])));
=======
function factorial(n) {
	if (n == 0) {
		return 1;
	}
	return n * factorial(n - 1);
}
console.log(factorial(process.argv[2]));
>>>>>>> adfd7f7321f0676258dfbf66ca145696431d6d42
