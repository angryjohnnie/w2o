# Basic REST endpoint w2o

This is a problem that has been solved a million times by a million others so I assume my solution is not really anything different than would be expected.

```
deployments/docker-compose up

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

Things I'm not doing here:
- I'm not optimizing the container builds
- I'm not pushing my prebuilt images to dockerhub or an internal docker repo
- no ssl
- no ssl redirects

I've dropped some Kubernetes manifests into this repo as an example only. These are basically just built with Kompose with the docker-compose as input. I did not fully test these but the output looks sane. In testing on a minikube cluster I ran up against the dockerhub image pulling daily limit so that was an unfortunate kink. This was actually the first time I used Kompose. It's tedious to write Kubernetes manifests esp when you're not doing it every day.
