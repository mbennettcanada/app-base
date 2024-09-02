# Database Setup
## Install Postgres
`sudo apt update`
`sudo apt install postgresql postgresql-contrib`
`sudo systemctl start postgresql`

## Setup DB 
1. `sudo -i -u postgres && psql`

## Allow remote connections
`vim /etc/postgresql/16/main/postgresql.conf`
change to `listen_addresses = '*'`
`sudo systemctl restart postgresql`