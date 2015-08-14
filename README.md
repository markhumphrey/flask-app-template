# mhumphrey/flask-app-template

This is an evolving base template for my flask apps. This includes a Dockerfile to provide a runtime environment.

I used this as a starting point:
https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications

Following the current recommendation for templates located in blueprint dirs:
http://flask.pocoo.org/docs/0.10/blueprints/#templates

[`markhumphrey/flask-app-template`](https://index.docker.io/u/markhumphrey/flask-app-template) is a [docker](https://docker.io) image for and extended version of the [Flask microframework](http://flask.pocoo.org/) hello world application.

It is based on [`mhumphrey/python-app`](https://index.docker.io/u/markhumphrey/python-app) base image and listen on port `8080`.

## Usage

- Run the following command

        docker run -p 8080 google/flask-app-template
