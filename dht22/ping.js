var sensor = require('node-dht-sensor');

const sensorType = 22;
const sensorPin = 23;

sensor.read(sensorType, sensorPin, function(err, temperature, humidity) {
  if (!err) {
    console.log('temp: ' + temperature.toFixed(1) + '°C, ' +
                'humidity: ' + humidity.toFixed(1) + '%'
    );
  }
});
