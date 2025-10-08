const url = 'https://open-weather13.p.rapidapi.com/fivedaysforcast?latitude=40.730610&longitude=-73.935242&lang=EN';
const options = {
	method: 'GET',
	headers: {
		'x-rapidapi-key': '57744dc8ddmshdd7e8fac9557f49p1eb045jsnb5bdaf410958',
		'x-rapidapi-host': 'open-weather13.p.rapidapi.com'
	}
};

// ,,
const getWeather = (city) => {
    document.getElementById("cityName").innerHTML = city;
  }
  // Example: cityName.innerHTML = 'Hyderabad';

 // to stop reloading used preventDefault()


(async () => {
  try {
const response  = await fetch(url, options);
const result = await response.json();
console.log(result);

// Select DOM elements
const temp = document.getElementById('temp');
const feels_like = document.getElementById('feels_like');
const temp_min = document.getElementById('temp_min');
const temp_max = document.getElementById('temp_max');
const pressure = document.getElementById('pressure');
const sea_level = document.getElementById('sea_level');
const grnd_level = document.getElementById('grnd_level');
const humidity = document.getElementById('humidity');
const temp_kf = document.getElementById('temp_kf');

// Access the correct properties from the API response
// Adjust the property access according to the actual API response structure
// Example assumes result.list[0].main contains the weather data
// Check if the API response has a 'list' property and it contains at least one item
if (result.list && result.list.length > 0) {
  // Get the 'main' object from the first item in the list
  const main = result.list[0].main;
  // Set the innerHTML of each DOM element to the corresponding value from the API
  temp.innerHTML = main.temp;
  feels_like.innerHTML = main.feels_like;
  temp_min.innerHTML = main.temp_min;
  temp_max.innerHTML = main.temp_max;
  pressure.innerHTML = main.pressure;
  sea_level.innerHTML = main.sea_level;
  grnd_level.innerHTML = main.grnd_level;
  humidity.innerHTML = main.humidity;
  temp_kf.innerHTML = main.temp_kf;
} else {
  // If the data is not available, show 'N/A' in each DOM element
  temp.innerHTML = 'N/A';
  feels_like.innerHTML = 'N/A';
  temp_min.innerHTML = 'N/A';
  temp_max.innerHTML = 'N/A';
  pressure.innerHTML = 'N/A';
  sea_level.innerHTML = 'N/A';
  grnd_level.innerHTML = 'N/A';
  humidity.innerHTML = 'N/A';
  temp_kf.innerHTML = 'N/A';
}
// ... and so on for other variables

  } catch (error) {
    console.error(error);
  }
})();

// 
SubmitEvent.addEventListener("click", (e) => {
  e.preventDefault();
  getWeather(city.value)
})


getWeather("Hyderabad");


