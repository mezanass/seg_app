docker container rm seg_app_env
docker image rm amezroui/seg_app
# docker run -p 27017:27017 --name mongo_env -d mongo:4.0.9-xenia
docker build -t amezroui/seg_app . 
docker run -p 5000:5000 -e GRANT_SUDO=yes --user root --name seg_app_env -v /Users/anass/flask_test:/app --link mongo_env:mongo_link amezroui/seg_app