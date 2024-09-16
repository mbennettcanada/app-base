# Base app example polarops

# Backend setup (How I did this the first time)
1. Install Conda and poetry `pipx install poetry`
2. Create conda project `conda create --name backend python=3.11`
3. Activate it `conda activate backend`
4. New Poetry project. `poetry new be`
5. Add deps `poetry add fastapi uvicorn sqlalchemy psycopg2` 

To update python in conda, activate then: `conda update python`


# Frontend setup (How I did this the first time)
1. `npx create-react-app fe`
2. `cd fe`
3. `npm install axios react-router-dom`
4. `npm audit fix --force`

Then followed this pretty close: https://dev.to/oyedeletemitope/login-authentication-with-react-and-fastapi-397b

until I got to the part that he stored plaintext passwords, the switched to following this: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-pyjwt 