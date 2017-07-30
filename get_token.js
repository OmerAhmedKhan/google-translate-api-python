// JS script to generate google translate token with help of npm package "google-translate-token"
// Unfortunately it is only available in npm package so it need to be execute in JS

const token = require('google-translate-token');

var text = 'Hello';

//get value from console
process.argv.forEach(function (val, index, array) {
  if (index === 2) {
  	text = val;
  }
});

//output value in searilized json string
token.get(text).then(function get_data (data) {
	console.log(JSON.stringify(data));
});