[*] DOCKER:

1) What & Why?
2) Difference Between Docker & Virtual Machine? [Real-world Example].
==> Lower Layer: HardWare -> Above ->
[*] Docker: Work to Replace top's Application Layer With Docker Container [ Same OS ].

[*] Virtual Machine: Work Direct As Operating System Replace [ Original Applicattion & OS (Kernal) Layer With ] Virtual Machine.

3) Difference Between Docker & KuberNet? [Real-World Example's].
===> 
1) Docker: School Bag which Handle Multiple Item's in it... [Docker].

2) KuberNet: A Big School Bag Shop Which Sell All  Type of Bag Is [ KuberNet ]. 

[*] Pull Image [ DockerHub ]: 
Go -> Search / Select Image and Click copy image.

[#] Command: docker pull img-name
[#] Run Docker: docker run img-id / img-name.

[#] exit: exit from folder. [ Terminal ]
[#] Stop Docker: docker stop container-id.

# Day:2

1) Difference Between Registry & Repository?
     1a) install node js.
     1b) Check version node -v

2) Create Demo Project:
     a) Understand Server / Client Rendering...
     b) npx create-react-app app_name

[*] Remove Unnecessary files: node_modules
     |
    \/
     [*] Create Docker File: Dockerfile
     [*] Write Code:

FROM node   OR    Version: FROM node:22
WORKDIR /myapp
COPY .  .        OR     COPY .  /myapp
RUN npm install
EXPOSE 3000
CMD ["npm", "start"] 
 
[*] Build Image: 
[*] Open Terminal : docker build .
[*] docker image ls

[*] Run & Manage Docker Container:
      [*] docker run iamge-id
      [*] View By: search localhost:3000
      
[*] Explain: docker container in between app not accissible to it's outer enviroment.

[*] Stop this:  
1) View Container: docker ps 
2) docker stop container-id / name
3) repeat 1st step...

[*] Run with outer access:
1) View Image: docker image ls
2) docker run -p 3000:3000 image-id

# Day:3 

[*] Container Management:

*) docker ps [ running container only view ].
*) docker ps -a : check both container
*) docker rm 1-image-name 2-image-name [ remove container ]. [ also get multiple name ]. [also direct from Docker Desktop ].

[*] But every time get start -> stop -> ps -a -> remove is very time consuming so get improve this...

[*] docker run -d --rm -p 3000:3000 img-id
View Using docker ps

[*] Name Our Application:
[*] docker run -d --rm --name "app_name" -p 3000:3000 image-id 

[*] Image Management: 

1) docker image ls
2) docker build -t tag_name:version .
   eg: docker build -t myapp:01 .
3) docker rmi tag_name:version


[*] What if we Update Our Project: 

update project & create new image
[*] docker run -d --rm --name "app" -p 3001: 3000 myapp1:02

[*] run first app also...
[*] Both Run Successs Fully...

[*] Pre-defined Image's:

[*] Docker Hub -> docker pull python -> run -> [ Software is run which create using language not laguage ].

[*] docker run python:latest

[*] you not select version then is cosider latest bi-default.

# Optional: 
[*] Docker Hub -> docker pull ngnix -> run -> but the port is important to get because it run on 8080:80 port bi-default...

[*] docker run -p 8080:80 ngnix:latest
[*] check on browser: localhost://8080

[*] Docker Container With Interactive mode:

*) New Folder: For Python OR Other...
*) Docker File...
*) Python File...
*) cd folder -> docker build .
*) docker run -it img-id
*) docker stop img-id

[*] Share Image's Docker Hub:  
1) Canva to Understand...
2) Create Repository [Public / Private]
3) VS Code Terminal -> docker login -> update detail's
4) copy repo-img push command from hub.
5) paste push command on vs code terminal.

[*] It's not work correct because this name image is not avilable from our side.
[*] push is use for sending data from local -> repo.

#] Create same name img & send
docker build -t repo_img_name:version .

6) run push command.

[*] Change tag is Bi-chance wrong Spealt:
*) docker tag tag_name:version change_name:version

*) push on docker hub...
docker push tag_name:version

[*] Run Our App On Different PC Using Our Image:
1) docker pull image-name:version
2) docker run -p 3000:3000 img_name:version.

[*] Run Successfully As You Can View...

[*] Docker Volume: 
*) New Folder: For Python OR Other...
*) Docker File...
*) Python File...
*) cd folder -> docker build .
*) docker run -it img-id

[*] Run But Get Issue Is Not Save Name continues if repeat run... 

[*] So, Volume Help to store this data in Particluar file: 
docker run -it -v vol_name:/folder OR file_name img_id

[*] docker volume --help
[*] docker volume ls
[*] docker volume inspect vol_name
[*] more...

[*] Mount Binds in Docker:
*) Create JS Program...
*) Create Docker File With Depandancy's...
*) Create Image...
*) Run Container...

& Try to Change & Re-Run File:
[*] It's Same Every Time Not Update Auto Matic & If Create New Then It's Show Updatation's...

Because of this we use the Mount Bind's:
1) Which help to get update data direct on the Same Image.
2) Less Tension to Re-Create New Image Every Time...

docker run --rm -v "[local_path] : [container_path]" [image_id OR image_name]

[*] .dockerignore:
consider / write only important file's on project & Other all add on .dockerignore 
Eg: 1) Dockerfile, 2) .gitignore...

[*] Communication From/To Containers:
1) Container  ---> Internet [www]
2) Container  ---> Local DB
3) Container ----> Container

1-a} Container  ---> Internet [www]: 

*-1) Create Python File...
*-2) Create Docker File...
*-3) Create --> Image --> Run -->

[*] Get Error For Import requests dependancy...

[*] Upgrade the Docker File...
*-*) RUN pip install requests

[*] Create New Image & Run...

1-b} Container ---->Local DB:

*-*) Required:
*-1) MySQL Workbench
*-2) MySQL Server
*-3) pymysql [connector ]-> pip install pymysql
*-4) MySQL Command Line Tools: mysql -u root -p

[*] Set Up Connection Setup: 
1) open my sql workbench...
2) click + icon to create connection.
3) create database using:
***) CREATE database userinfo;
4) next --> Click Database -->Manage Connection --> test connection
5) View all Detail's: it's important in future...

[*] Go to the VS Code:
1) Create Folder [ Store Python File].
2) Create localDB.py file
3) paste the below [ code ] link;
    [*] apply the==> host: host.docker.internal
4) create docker file.
    [*] write dependancy & code.

[*] Docker Command:
1) docker build -t localDBconn .
2) docker images OR docker image ls
3) docker run --rm img_id

[*] Get Error Because our program is related to interaction.

4) docker run -it --rm img_id

1-c} Container ------> Container:
1) go docker hub & Pull mysql image from there...
2) docker run -d --name mysqldb mysql:latest
[*] -d: detach mode [ work detachly ].

[*] docker logs container_name: mysqldb
[*] docker inspect [ container_name ]... 

[*] Get Error / Warning: need env variable:
1) MYSQL_ROOT_PASSWORD
2) MYSQL_ALLOW_EMPTY_PASSWORD
3) MYSQL_RANDOM_ROOT_PASSWORD 

[*] Running: 
docker run -d --env MYSQL_ROOT_PASSWORD="Pass@123PRM" --env MYSQL_DATABASE="userinfo" --name mysqldb mysql

[*] Check IP Address: docker inspect container_name 

Modify Docker File:
[*] RUN pip install cryptography

[*] Run Python LocalDB Code: 
 [*] docker run -it --rm img-id 
 [*] docker run -it --rm --name [name] img-id 


[*] Docker Network:
    [*] Simply Both in Network: mysql & localDB

1) docker network create [Net-Name]
2) docker network ls
3) docker run -d --env MYSQL_ROOT_PASSWORD=["DB_Pass"] --env MYSQL_DATABASE=["DB_name"] --name [Con_name] --network [Net_name] [Img_name]
 
[*] Done With MYSQL Run In Network:

4) docker build -t [tag_name] .
5) docker run -it --rm --network my-net img_id

[*] Increases the Accessebility.
[*] time reducing
[*] easy to understand 
[*] direct target to mysqldb2

[*] Docker Compaose [Single] Container:
configuration file to managge multiple containers running on same machine...

[*] create docker-compose.yml
paste OR Write:
[ 
services:
  mysqldb:
    image: "mysql:latest"
    environment:
      - MYSQL_ROOT_PASSWORD="Pass@123PRM"
      - MYSQL_DATABASE="userinfo"
    container_name: "mysqldb3"
]

[*] Docker Compose with [Multiple] network:
paste OR Write:
[ 
services:
  mysqldb:
    image: "mysql:latest"
    environment:
      - MYSQL_ROOT_PASSWORD="Pass@123PRM"
      - MYSQL_DATABASE="userinfo"
    container_name: "mysqldb3"
  
  mypythonapp: 
     build: ./  
]

[*] Command: docker compose up

[*] check both container is running or not:
as we view python is not running stage...

[*] docker logs [ python_container_name ]

[
   mypythonapp:
     build: ./
     container_name: myapp
     depends_on:
        - 'mysqldb'
]

[*] Command: docker compose up

||
\/

[Documentation]: 
1) healthcheck 
2) enviroment

services:
  mysqldb:
    image: 'mysql-latest'
    enviroment:
      - MYSQL_ROOT_PASSWORD="Pass@123PRM"
      - MYSQL_DATABASE=userinfo
    container_name: mysqldb

/#/ health check container mysqldb on or stop: 
 
    healthcheck:
      test: ['CMD', 'mysqladmin', 'ping', '-h', 'localhost']
      timeout: 20s
      retries: 10

  mypythonapp:
    build: ./
    cotainer_name: myapp

/#/ Dependancy start app after this:
    depends_on: 
       mysqldb:
         connection: service_healthy

/#/ Interactive terminal:
    stdin_open: true
    tty: true
]

[*] Stop Running:

& Run Both Seprate: mysqldb & pythonapp
1) docker-compose run -d [con_name]
2) docker-compose run [pyapp_id]

[*] Stop Running Both & Done With Series: