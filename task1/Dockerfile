# Complete this Dockerfile to launch a Nginx server
FROM ubuntu:latest

#RUN the following commands on startup
RUN apt-get update && apt-get install -y nginx

#Expose port 80
EXPOSE 80

#Add the files
ADD ./index.html /var/www/html/

# Entry point
CMD ["nginx", "-g", "daemon off;"]

# Use bash as the container's entry point
#ENTRYPOINT ["/bin/bash", "-c"]
