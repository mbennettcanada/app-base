# Database Setup
## Install Postgres
`sudo apt update`
`sudo apt install postgresql postgresql-contrib`
`sudo systemctl start postgresql`

## Setup DB 
1. `sudo -i -u postgres && psql`
2. `create database app;`
3. `create user app with encrypted password 'repl@c3me';`
4. `grant all privileges on database app to app;`
5. `ALTER DATABASE app OWNER TO app;`

## Change password:
`ALTER USER app WITH PASSWORD 'replac3M3';`


## Allow remote connections
`vim /etc/postgresql/16/main/postgresql.conf`
change to `listen_addresses = '*'`
Then
`sudo vim /etc/postgresql/16/main/pg_hba.conf`
change to 

```
# IPv4 local connections:
host    all             all             0.0.0.0/0            scram-sha-256
```
Then
`sudo systemctl restart postgresql`

## Errors
ERROR:  template database "template1" has a collation version mismatch
fix: `ALTER DATABASE template1 REFRESH COLLATION VERSION;`