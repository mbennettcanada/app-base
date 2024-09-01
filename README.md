# Base app example polarops

# Backend setup (How I did this the first time)
1. Install Conda and poetry `pipx install poetry`
2. Create conda project `conda create --name backend python=3.11`
3. Activate it `conda activate backend`
4. New Poetry project. `poetry new be`
5. Add deps `poetry add fastapi uvicorn sqlalchemy psycopg2` 

To update python in conda, activate then: `conda update python`
