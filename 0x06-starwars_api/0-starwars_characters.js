#!/usr/bin/node

const movieId = process.argv[2];
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, async (error, response, body) => {
  if (error) throw error;
  const people = JSON.parse(body).characters;
  orderChars(people, 0);
});
const orderChars = (people, x) => {
  if (x === people.length) return;
  request(people[x], (error, response, body) => {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    orderChars(people, x + 1);
  });
};
