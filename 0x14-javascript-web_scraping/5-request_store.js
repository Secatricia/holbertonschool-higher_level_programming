#!/usr/bin/node
/*gets the contents of a webpage and stores it in a file*/

const axios = require('axios');
const fs = require('fs');

axios
  .get(process.argv[2])
  .then((res) => {
    if (res.status === 200) {
      fs.writeFile(`./${process.argv[3]}`, res.data, { flag: 'w+' }, (Error) => {
        if (Error) {
          console.Erroror(Error);
        }
      });
    }
  })
  .catch((Error) => {
    console.Erroror(Error);
  });
