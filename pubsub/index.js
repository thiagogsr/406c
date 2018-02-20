const PubSub = require(`@google-cloud/pubsub`);

function createTopic (topicName) {
  const pubsub = new PubSub();

  pubsub
    .createTopic(topicName)
    .then(results => {
      const topic = results[0];
      console.log(`Topic ${topic.name} created.`);
    })
    .catch(err => {
      console.error('ERROR:', err);
    });
}

function publishMessage (topicName, data) {
  const pubsub = new PubSub();
  const dataBuffer = Buffer.from(data);

  pubsub
    .topic(topicName)
    .publisher()
    .publish(dataBuffer)
    .then(results => {
      const messageId = results[0];
      console.log(`Message ${messageId} published.`);
    })
    .catch(err => {
      if(err.message.indexOf("Resource not found") !== -1) {
        createTopic(topicName)
        publishMessage(topicName, data)
      }
    });
}

exports.createTopic = createTopic
exports.publishMessage = publishMessage
