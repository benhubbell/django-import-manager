`docker-compose -f docker-compose.dev.yml up -d --build`
`docker exec -it <container-id> psql -U dim_dev_user -d dim_dev_database --password`