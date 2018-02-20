const sensor = require('node-dht-sensor');
const pubsub = require('../pubsub');

const sensorType = 22;
const sensorPin = 23;
const temperatureTopic = 'home-office-temperature';
const humidityTopic = 'home-office-humidity';

sensor.read(sensorType, sensorPin, function(err, temperature, humidity) {
  if (!err) {
    pubsub.publishMessage(temperatureTopic, temperature.toFixed(1));
    pubsub.publishMessage(humidityTopic, humidity.toFixed(1));
  }
});
