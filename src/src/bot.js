const tmi = require('tmi.js');

var myArgs = process.argv.slice(2)

const BOT_USERNAME = myArgs[0]
const OAUTH_TOKEN = myArgs[1]
const CHANNEL_NAME = myArgs[2]
const MSG = myArgs[3]

const opts = {
  identity: {
    username: BOT_USERNAME,
    password: OAUTH_TOKEN
  },
  channels: [
    CHANNEL_NAME
  ]
}

function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)) }

const client = new tmi.client(opts);

client.on('message', onMessageHandler);
client.on('connected', (addr, port) => {
    client.action(CHANNEL_NAME, MSG)
});

client.connect();
//client.say(CHANNEL_NAME, MSG)

function onMessageHandler (target, context, msg, self) {
  if (self) { return; }

  const commandName = msg.trim()

  if (commandName === '!test') {
    client.say(target, 'It is 1 message!')
    console.log('Message sent')
  } else {
    console.log(`* Unknown command ${commandName}`)
  }
}