# rocket-crafting-server-py
## Alias RCS-Py-Sock

### Communication: webSockets
### Database:      MongoDB
### Programming Languages: Python, JavaScript

## Install:

```bash
python -m venv env
source env/bin/activate

python -m pip install "pymongo[srv]"
python -m pip install python-dateutil
python -m pip install pycryptodome
```

If you have any error log like `missing module`, just install it.

## Documentation for websock RCS-Py-Sock

## - Web app part

Same shema also used in visual-ts game engine && Rest api RCS variant(Node.js).
Used online free service https://cloud.mongodb.com and MongoDB Compass windows desktop help tool.


### - Route : `register`

Client request:
```js
var data = {
    action: "REGISTER",
    userRegData: {
        password: byId('password').value,
        email: byId('email').value
    }
};
socket.send(JSON.stringify(data));
```

```js
msgFromCLient.action === "REGISTER";
msgFromCLient.data.userRegData.email & password;
```

- Response with:

```js
 "USER_REGISTERED" or "USER_ALREADY_REGISTERED"
```

After "USER_REGISTRED" Server send validation code to the user email and sock emit data ->

Client request:
```js
var data = {
  action: "CONFIRMATION",
  userRegData: {
    token: byId("token").value,
    email: byId("email").value,
  },
};
socket.send(JSON.stringify(data));
```

Confirmation code response:
```js
  {"message": "Confirmation done.", "rocketStatus": "USER_CONFIRMED"}
```

### - Python app part [wip]

## Why to use RCS-PYSOCK

### GPTCHAT source
Why Websockets?

Websockets are a valuable technology for web development because they enable real-time, full-duplex communication between a client (such as a web browser) and a server. Here are several reasons why websockets are useful:

Real-time Updates: Websockets allow servers to push updates to clients instantly without the client needing to constantly poll the server for new information. This makes them ideal for applications where real-time data updates are critical, such as chat applications, multiplayer games, stock tickers, or live sports scores.

Efficiency: Unlike traditional HTTP requests which are stateless and require a new connection for each request/response cycle, websockets maintain a persistent connection. This reduces overhead, as there's no need to repeatedly establish connections, send headers, or manage cookies for each interaction.

Bi-directional Communication: Websockets support bidirectional communication, meaning both the client and server can send messages to each other at any time. This allows for more interactive and responsive applications compared to one-way communication methods like HTTP polling or long-polling.

Lower Latency: By maintaining an open connection, websockets reduce latency compared to traditional polling methods. Updates are delivered instantly when they are available, rather than waiting for the next scheduled poll.

Scalability: Websockets can be scaled efficiently because they maintain persistent connections, reducing the need for servers to handle frequent new connection requests. This makes them suitable for handling large numbers of concurrent users or devices.

Support for Complex Applications: Websockets support complex use cases where immediate and synchronized communication between multiple clients is necessary, such as collaborative editing tools, online auctions, or real-time analytics dashboards.

Cross-Domain Communication: Websockets can facilitate cross-domain communication securely, as they adhere to the same-origin policy by default. This allows for integration with APIs and services hosted on different domains.

Overall, websockets provide a powerful mechanism for building modern, interactive web applications that require real-time updates and responsive user experiences. They are well-suited for applications where immediate data synchronization and minimal latency are priorities.


Why MongoDB?

MongoDB is chosen by many developers and organizations for several compelling reasons:

Flexible Schema Design: MongoDB is a NoSQL database that uses a flexible schema model known as BSON (Binary JSON). Unlike traditional relational databases, MongoDB does not enforce a strict schema, allowing developers to store and manage heterogeneous data structures easily. This flexibility is particularly useful in agile development environments where schema changes are frequent.

Scalability: MongoDB is designed to scale horizontally by distributing data across multiple nodes in a cluster. This horizontal scaling capability enables MongoDB to handle large volumes of data and high throughput applications effectively. It supports sharding, which allows data to be partitioned across multiple servers, and replication for high availability and fault tolerance.

Performance: MongoDB's architecture and storage format (BSON) are optimized for performance. It supports indexes, including compound indexes and geospatial indexes, which improve query performance. MongoDB also provides aggregation framework for performing complex aggregations and computations within the database, reducing the need for data processing on the application side.

Document-Oriented Storage: MongoDB stores data in JSON-like documents (BSON), which map naturally to modern application objects. This document-oriented approach eliminates the need for Object-Relational Mapping (ORM) tools and simplifies data retrieval and manipulation. Documents can be nested, making it easier to represent complex hierarchical relationships.

Rich Query Language: MongoDB provides a powerful query language that supports a wide range of queries, including CRUD operations (Create, Read, Update, Delete), aggregation pipelines, text search, geospatial queries, and more. This flexibility allows developers to express complex queries and retrieve data efficiently.

Community and Ecosystem: MongoDB has a large and active community of developers, which contributes to its ecosystem of libraries, frameworks, and tools. It is well-supported across various programming languages and platforms, making it easier for developers to integrate MongoDB into their applications.

Cloud-Native: MongoDB Atlas, the official fully managed cloud database service for MongoDB, provides automated backups, scaling, and monitoring, making it easy to deploy and manage MongoDB clusters in the cloud. This cloud-native approach reduces operational overhead and allows developers to focus more on building applications.

Use Cases: MongoDB is suitable for a wide range of use cases, including content management, real-time analytics, mobile applications (offline sync), IoT (Internet of Things), catalog and product data management, user profiles, and more. Its flexibility, scalability, and performance characteristics make it versatile for both operational and analytical workloads.

In summary, MongoDB's flexibility, scalability, performance, document-oriented storage, rich query capabilities, community support, cloud-native features, and broad range of use cases make it a popular choice for modern application development.

