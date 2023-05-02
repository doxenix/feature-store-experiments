#!/bin/bash
docker run --name feast-postgres -e POSTGRES_PASSWORD=my_pass -e POSTGRES_DB=orders -p 5432:5432 -d postgres

docker run --name postgres -e POSTGRES_PASSWORD=my_pass -e POSTGRES_DB=orders -p 5433:5432 -d postgres
