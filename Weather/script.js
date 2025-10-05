const url = 'https://open-weather13.p.rapidapi.com/fivedaysforcast?latitude=40.730610&longitude=-73.935242&lang=EN';
const options = {
	method: 'GET',
	headers: {
		'x-rapidapi-key': '57744dc8ddmshdd7e8fac9557f49p1eb045jsnb5bdaf410958',
		'x-rapidapi-host': 'open-weather13.p.rapidapi.com'
	}
};

(async () => {
  try {
    const response  = await fetch(url, options);
    const result = await response.text();
    console.log(result);
  } catch (error) {
    console.error(error);
  }
})();
