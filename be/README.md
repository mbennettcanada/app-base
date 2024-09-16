Running dev local:
`poetry run uvicorn be.main:app --reload`

Build image: 
`docker build -t backend`

After first build ^ you can target only dev stages like this: 
`docker build -t backend --target development .`

We could then get a shell inside the container with:
`docker run -it backend bash`

Run that locally like this: 
`docker run -it -p 8000:8000 backend`

Docker commands:
`docker ps`
`docker image ls`
`docker image rm -f`
`docker system prune` SUPER handy
