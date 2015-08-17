# mhumphrey/flask-app-template

This is an evolving base template for my flask apps. This includes a Dockerfile to provide a runtime environment.

I used this as a starting point:
https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications

Following the current recommendation for templates located in blueprint dirs:
http://flask.pocoo.org/docs/0.10/blueprints/#templates

I need to look into adding skeleton code for switching between environments (e.g. dev, staging and production):
https://exploreflask.com/configuration.html

Includes skeleton code using Flask, SQLAlchemy and WTForms.

[`markhumphrey/flask-app-template`](https://index.docker.io/u/markhumphrey/flask-app-template) is a [docker](https://docker.io) image for and extended version of the [Flask microframework](http://flask.pocoo.org/) hello world application.

Create a Dockerfile building from python-2.7 base image and listening on port 8088.

Make use of docker extends feature to easily create runnable development and production environments. In the dev environment the source code is
mounted as a read only volume.

https://docs.docker.com/compose/extends/

## Usage

- To build the docker image and launch the service:

docker-compose up web

- To launch a shell on the running docker container

docker-compose run web "/bin/bash"
