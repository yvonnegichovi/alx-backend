# 0x03. Queuing System in JS

## Back-end | JavaScript | ES6 | Redis | NodeJS | ExpressJS | Kue

**Weight:** 1

**Project Start:** Jul 29, 2024, 6:00 AM  
**Project End:** Aug 1, 2024, 6:00 AM  
**Manual QA Review:** Required upon completion

## Resources
- **Read or watch:**
  - [Redis quick start](https://redis.io/topics/quickstart)
  - [Redis client interface](https://redis.io/topics/client-side-caching)
  - [Redis client for Node JS](https://github.com/NodeRedis/node-redis)
  - [Kue (deprecated but still used in the industry)](https://github.com/Automattic/kue)

## Learning Objectives
By the end of this project, you should be able to:
- Run a Redis server on your machine
- Perform simple operations with the Redis client
- Use a Redis client with Node JS for basic operations
- Store hash values in Redis
- Handle async operations with Redis
- Use Kue as a queue system
- Build a basic Express app interacting with a Redis server
- Build a basic Express app interacting with a Redis server and queue

## Requirements
- Code must be compiled/interpreted on **Ubuntu 18.04, Node 12.x, and Redis 5.0.7**
- All files should end with a new line
- A `README.md` file at the root of the project is mandatory
- Code should use the `.js` extension

## Required Files for the Project
- `package.json`
- `.babelrc`

Remember to run `$ npm install` when you have the `package.json`.

## Tasks

### 0. Install a Redis Instance
- **Instructions:**
  1. Download, extract, and compile the latest stable Redis version (higher than 5.0.7):
     ```bash
     $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
     $ tar xzf redis-6.0.10.tar.gz
     $ cd redis-6.0.10
     $ make
     ```
  2. Start Redis in the background:
     ```bash
     $ src/redis-server &
     ```
  3. Verify the server is working:
     ```bash
     $ src/redis-cli ping
     PONG
     ```
  4. Set and get a value using the Redis client:
     ```bash
     127.0.0.1:[Port]> set Holberton School
     OK
     127.0.0.1:[Port]> get Holberton
     "School"
     ```
  5. Kill the server:
     ```bash
     $ kill [PID_OF_Redis_Server]
     ```
  6. Copy `dump.rdb` from the Redis directory into the project root.

- **Repository:**
  - GitHub repository: `alx-backend`
  - Directory: `0x03-queuing_system_in_js`
  - File: `README.md`, `dump.rdb`

### 1. Node Redis Client
- **Instructions:**
  1. Install `node_redis` using npm.
  2. Write a script named `0-redis_client.js` that connects to the Redis server and logs appropriate messages.
  3. Requirements:
     - Use ES6 `import` keyword.

- **Repository:**
  - GitHub repository: `alx-backend`
  - Directory: `0x03-queuing_system_in_js`
  - File: `0-redis_client.js`

### 2. Node Redis Client and Basic Operations
- **Instructions:**
  1. In a file `1-redis_op.js`, copy the code from `0-redis_client.js`.
  2. Add two functions: `setNewSchool` and `displaySchoolValue`.
  3. Use callbacks for operations.

- **Repository:**
  - GitHub repository: `alx-backend`
  - Directory: `0x03-queuing_system_in_js`
  - File: `1-redis_op.js`

### 3. Node Redis Client and Async Operations
- **Instructions:**
  1. In a file `2-redis_op_async.js`, copy the code from `1-redis_op.js`.
  2. Modify `displaySchoolValue` to use ES6 `async/await` with `promisify`.

- **Repository:**
  - GitHub repository: `alx-backend`
  - Directory: `0x03-queuing_system_in_js`
  - File: `2-redis_op_async.js`

### 4. Node Redis Client and Advanced Operations
- **Instructions:**
  1. In a file named `4-redis_advanced_op.js`, use the client to store a hash value.
  2. Use `hset` to store multiple values and `hgetall` to display the stored object.

- **Repository:**
  - GitHub repository: `alx-backend`
  - Directory: `0x03-queuing_system_in_js`
  - File: `4-redis_advanced_op.js`

### 5. Node Redis Client Publisher and Subscriber
- **Instructions:**
  1. Create `5-subscriber.js` to subscribe to a Redis channel.
  2. Create `5-publisher.js` to publish messages to the Redis channel.

- **Repository:**
  - GitHub repository: `alx-backend`
  - Directory: `0x03-queuing_system_in_js`
  - File: `5-subscriber.js`, `5-publisher.js`

### 6. Create the Job Creator
- **Instructions:**
  1. In a file named `6-job_creator.js`, create a Kue queue and add job data.

- **Repository:**
  - GitHub repository: `alx-backend`
  - Directory: `0x03-queuing_system_in_js`
  - File: `6-job_creator.js`

### 7. Create the Job Processor
- **Instructions:**
  1. In a file named `6-job_processor.js`, create a Kue queue and process the jobs.

- **Repository:**
  - GitHub repository: `alx-backend`
  - Directory: `0x03-queuing_system_in_js`
  - File: `6-job_processor.js`

### 8. Track Progress and Errors with Kue: Create the Job Creator
- **Instructions:**
  1. In a file named `7-job_creator.js`, create an array of job data and add them to the Kue queue.

- **Repository:**
  - GitHub repository: `alx-backend`
  - Directory: `0x03-queuing_system_in_js`
  - File: `7-job_creator.js`
