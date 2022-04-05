#!/usr/bin/node

if (parseInt(process.argv[2])) {
<<<<<<< HEAD
  console.log('My number: ', parseInt(process.argv[2]));
} else if (parseInt(process.argv[2]) === 0) {
  console.log('My number: 0');
} else {
  console.log('Not a number');
=======
	console.log('My number: ' , parseInt(process.argv[2]));
}
else if(parseInt(process.argv[2]) == 0){
	console.log('My number: 0');
}
else {
	console.log('Not a number');
>>>>>>> adfd7f7321f0676258dfbf66ca145696431d6d42
}
