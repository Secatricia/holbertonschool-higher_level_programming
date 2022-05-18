#!/usr/bin/node
/* prints the number of movies 
where the character “Wedge Antilles” is present*/

const axios = require('axios');
const API_URL = process.argv[2];

axios
  .get(`${API_URL}`)
  .then((response) => {
    let i = 0;
    for (const film of response.data.results) {
      for (const listActors of film.characters) {
        if (listActors.includes('people/18/')) {
          i++;
        }
      }
    }
    console.log(i);
  })
  .catch((error) => {
	console.error(error);
  });
