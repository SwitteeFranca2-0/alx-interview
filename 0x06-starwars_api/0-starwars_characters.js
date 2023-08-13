#!/usr/bin/node
const id = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

async function handleData (data) {
  return await new Promise(function (resolve, reject) {
    request(data, function (err, resp, body) {
      if (err) { return reject(err); }
      try {
        resolve(JSON.parse(body).name);
      } catch (e) {
        reject(e);
      }
    });
  });
}

async function handleChar (infos) {
  for (const info of infos) {
    await handleData(info)
      .then(function (datum) {
        console.log(datum);
      });
  }
}

async function requestUrl () {
  return new Promise(function (resolve, reject) {
    request(url, function (err, resp, body) {
      if (err) { return reject(err); }
      try {
        resolve(JSON.parse(body).characters);
      } catch (e) {
        reject(e);
      }
    });
  });
}

requestUrl()
  .then(function (data) {
    handleChar(data);
  })
  .catch(function (err) {
    console.log(err);
  });
