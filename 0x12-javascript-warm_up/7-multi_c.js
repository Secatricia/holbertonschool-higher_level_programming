#!/usr/bin/node
if (parseInt(process.argv[2])) {
<<<<<<< HEAD
  while (process.argv[2] !== 0) {
    console.log('C is fun');
    process.argv[2] -= 1;
  }
} else {
  console.log('Missing number of occurrences');
=======
	while (process.argv[2] != 0) {
		console.log('C is fun');
		process.argv[2] -= 1;
	}
}
else
{
	console.log('Missing number of occurrences');
>>>>>>> adfd7f7321f0676258dfbf66ca145696431d6d42
}
