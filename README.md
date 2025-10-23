Overview

This repository contains multiple hands-on Docker projects demonstrating Docker concepts including images, containers, networking, multi-stage builds, and multi-language applications. These projects are designed for learning and practice.

Projects Included
1️⃣ Static Website

Description: A simple static HTML website served using Nginx Docker image.

Dockerfile Highlights:

Uses nginx:latest base image.

Copies website files to /usr/share/nginx/html.

Exposes port 80.

Usage:

docker build -t static-website .
docker run -d -p 8081:80 static-website


Access: http://localhost:8081
--------------------------------------------------------------------------------------------------------------- 
2️⃣ Node.js + Redis (Networking Example)

Description: Node.js app that counts visits using Redis. Demonstrates default bridge network and custom networks.

Dockerfile Highlights:

Node.js official image.

Installs dependencies via npm install.

Exposes port 3000.

Usage (Custom Network Recommended):

docker network create custom-net
docker run -d --name redis-container --network custom-net redis
docker build -t node-redis-bridge .
docker run -d -p 3000:3000 --name node-app --network custom-net node-redis-bridge


Access: http://localhost:3000

Notes:

Default bridge network requires using container IP.

Custom networks allow using container names directly.
-------------------------------------------------------------------------------------------------------------------------- 
3️⃣ Node.js on Host Network

Description: Node.js app demonstrates host network mode, where the container shares the host’s network stack.

Dockerfile Highlights:

Node.js official image.

Exposes port 5000 (not required in host mode).

Usage:

docker build -t node-host-app .
docker run -d --network host --name node-host node-host-app


Access: http://localhost:5000

Notes:

No port mapping (-p) needed.

Host network mode is Linux only.
------------------------------------------------------------------------------------------------------------------------------- 
4️⃣ Python Flask + MySQL

Description: Flask app connects to MySQL database to fetch data. Demonstrates user-defined bridge network for multi-container communication.

Dockerfile Highlights:

Python 3.10 slim image.

Installs dependencies from requirements.txt.

Exposes port 5000.

Usage:

docker network create custom-net
docker run -d --name mysql-db --network custom-net -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb mysql:5.7
docker build -t flask-mysql-app .
docker run -d -p 5000:5000 --name flask-app --network custom-net flask-mysql-app


Access: http://localhost:5000

Notes:

Flask container can connect to MySQL by container name.

Queries SELECT NOW() by default; can be modified to query custom tables.
