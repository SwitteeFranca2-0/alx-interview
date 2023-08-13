#!/usr/bin/node
const id = process.argv[2];
const request = require('request-promise');
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

async function handleData (data) {
  for (const info of data) {
    await request(info, function (err, res, body) {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body).characters;
  handleData(data);
});
