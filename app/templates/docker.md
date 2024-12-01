







docker build -t website_image .

docker run -d --name adrianhredhe.com -p 80:80 website_image

Containter
docker container logs adrianhredhe.com
