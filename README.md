# Basic REST endpoint w2o

This is a problem that has been solved a million times by a million others so I assume my solution is not really anything different than would be expected.

```
cd deployments && docker-compose up
```

My plan is basically:

- Build a Python webapp with Flask
    - The app should respond with json
    - The app should only listen on a local network port
- Deploy the webapp into a container along with its requirements
- Leave the default Flask app port of 5000
- Write an nginx reverse proxy config with the Flask app as an upstream
    - nginx listens on port 8080
    - providing 2 endpoints for the example
        - "/" responds with just a bogus useraccount info dict
        - "/hello" responds with a HelloWorld message dict
- Deploy nginx into a container with a dependency on the Flask app
- Provide a docker-compose file to stand up the demo
- Provide some manifests to deploy to a Kubernetes cluster

Things I'm not doing here:
- I'm not optimizing the container builds
- I'm not pushing my prebuilt images to dockerhub or an internal docker repo
- no ssl
- no ssl redirects
- no parameters accepted by the endpoints. There are Python libraries for full-blown flask REST interfaces that I'm sure can be implemented for this. I've not specifically used any of them though
- This flask app should probably (definitely) be served in prod with a wsgi backend like uwsgi or gunicorn.
- Theres no redundancy here. More upstreams can be added to the nginx config with more app containers deployed. With this comes the need for a backend to maintain state across all instances.
- uwsgi servers like gunicorn have the ability to provide a dev server that could be served on a different port with a volume mount to the docker host that contains the code for dev testing.
- logging in this current setup is limited to the docker logs or exec-ing into the container to read the logs. More robust solutions such as filebeat exporting to logstash or such would be a useful addition

I've dropped some Kubernetes manifests into this repo as an example only. These are basically just built with Kompose with the docker-compose as input. I did not fully test these but the output looks sane. In testing on a minikube cluster I ran up against the dockerhub image pulling daily limit so that was an unfortunate kink. This was actually the first time I used Kompose. It's tedious to write Kubernetes manifests esp when you're not doing it every day.
