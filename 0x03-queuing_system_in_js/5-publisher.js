import { createClient } from 'redis';

const publisher = createClient();

//connect to redis server
publisher.on('connect', function () {
    console.log('Redis client connected to the server');
});

publisher.on('error', function(error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

//function to publish message to holberton school channel
function publishMessage(message, time) {
  //message (str): message to be published, time (int): time in milliseconds to wait before sending message
  setTimeout(function () {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
