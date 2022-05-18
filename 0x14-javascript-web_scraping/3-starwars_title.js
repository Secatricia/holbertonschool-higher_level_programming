#!/usr/bin/node
/* prints the title of a Star Wars movie 
where the episode number matches a given integer*/
const axios = require('axios');

axios
  .get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function () {
    console.log('Error');
  });

  const axios = require('axios');
  const API_URL = process.argv[2];
