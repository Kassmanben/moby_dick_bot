const fs = require('fs'),
      Twitter = require('twitter'),
      dotenv = require('dotenv'),
      filename = 'tweets.txt';

dotenv.config();
const config = {
  consumer_key: process.env.CONSUMER_KEY,
  consumer_secret: process.env.CONSUMER_SECRET,
  access_token_key: process.env.ACCESS_TOKEN_KEY,
  access_token_secret:  process.env.ACCESS_TOKEN_SECRET
};

const T = new Twitter(config);

//Read in the file from above, and act on the data once it's been loaded
fs.readFile(filename, 'utf8', function(err, data){
  if (err) throw err;
    let tweets = data.split('\n');

    //Fetch an random and even-numbered index, since our tweets take up two lines
    const i = Math.floor(Math.random() * Math.floor(tweets.length/2))*2;

    //Construct status using two lines
    const status = tweets[i] + "\n" + tweets[i+1];
    T.post('statuses/update', {status: status},  function(error, tweet) {
      if(error) {
          console.log(error);
          throw error;
      }
    });
});