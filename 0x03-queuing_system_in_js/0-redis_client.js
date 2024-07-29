import redis from 'redis';

const client = redis.createClient({
  url: 'redis://127.0.0.1:7764',
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
