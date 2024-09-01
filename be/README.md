Running dev local:
`poetry run uvicorn be.main:app --reload`

Build image: 
`docker build -t backend`

After first build ^ you can target only dev stages like this: 
`docker build -t backend --target development .`
