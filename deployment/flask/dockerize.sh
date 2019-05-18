#docker container rm seg_app
#docker container rm mongo
#docker image rm amezroui/seg_app
docker run -p 27017:27017 -e GRANT_SUDO=yes --user root --name mongo -d mongo:4.0.9-xenial
docker build -t amezroui/seg_app . 
docker run -p 5000:5000 -e GRANT_SUDO=yes --user root --name seg_app -v /Users/anass/workspace/seg_app/deployment/flask:/app --link mongo:mongo_link amezroui/seg_app