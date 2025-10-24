Docker Volumes Hands-on Guide
Overview

Docker volumes provide persistent storage for containers.
Without volumes, all data inside a container is lost when the container is removed.

There are 3 types of volumes:

Anonymous Volume – auto-generated, temporary.

Named Volume – user-defined, reusable.

Bind Mount – maps a host folder directly into the container.

1️⃣ Anonymous Volumes
Description

Created automatically by Docker when you use -v /path without naming the volume.

Data persists after container removal, but hard to reuse.

Hands-on Example
Step 1: Create a simple logger script
mkdir -p ~/docker/volumes/anon
cd ~/docker/volumes/anon

nano logger.sh


Add:

#!/bin/sh
while true; do
  echo "Timestamp: $(date)" >> /data/log.txt
  sleep 5
done


Make it executable:

chmod +x logger.sh

Step 2: Create Dockerfile
FROM alpine
WORKDIR /app
COPY logger.sh .
CMD ["./logger.sh"]


Build the image:

docker build -t logger-anon .

Step 3: Run container with anonymous volume
docker run -d --name log-anon -v /data logger-anon

Step 4: Inspect volume
docker volume ls
docker inspect <volume_id>
docker exec -it log-anon cat /data/log.txt

Step 5: Remove container
docker rm -f log-anon
docker volume prune   # optional: clean unused volumes
----------------------------------------------------------------- 
2️⃣ Named Volumes
Description

User-defined name, easy to reuse across containers.

Stored in Docker-managed location: /var/lib/docker/volumes/<name>/_data

Hands-on Example
Step 1: Create a named volume
docker volume create appdata

Step 2: Run container using it
docker run -d --name nginx1 -v appdata:/usr/share/nginx/html -p 8080:80 nginx

Step 3: Add file inside container
docker exec -it nginx1 /bin/sh -c 'echo "Hello from Named Volume!" > /usr/share/nginx/html/index.html'

Step 4: Test persistence

Remove container:

docker rm -f nginx1


Re-run using same volume:

docker run -d --name nginx2 -v appdata:/usr/share/nginx/html -p 8081:80 nginx


Open browser: http://<EC2-IP>:8081 → file still exists ✅
---------------------------------------------------------------------- 

3️⃣ Bind Mounts
Description

Maps a host folder directly to a container folder.

Changes on host reflect instantly in container.

Hands-on Example
Step 1: Create host folder
mkdir -p ~/docker/webdata
echo "Hello from Host!" > ~/docker/webdata/index.html

Step 2: Run container using bind mount
docker run -d --name nginx-bind \
  -v ~/docker/webdata:/usr/share/nginx/html \
  -p 8082:80 nginx

Step 3: Test live changes

Edit file on host:

echo "Updated content without rebuild!" > ~/docker/webdata/index.html


Refresh browser: content updates instantly ✅

🔹 Inspecting Volumes

List all volumes:

docker volume ls


Inspect a volume:

docker volume inspect <volume_name_or_id>


Remove unused volumes:

docker volume prune
-------------------------------------------------------------------- 
🔹 Volume Paths
Type	Host Storage Path
Anonymous	/var/lib/docker/volumes/<hash>/_data
Named	/var/lib/docker/volumes/<name>/_data
Bind Mount	Whatever host folder you specify (/home/...)
-------------------------------------------------------------------- 
✅ Key Takeaways

Anonymous Volume – easy, auto-generated, temporary.

Named Volume – reusable, good for DBs, persistent data.

Bind Mount – live sync between host and container, good for development.

Volumes persist data even if containers are removed.

Use docker volume inspect to find where data is stored.
