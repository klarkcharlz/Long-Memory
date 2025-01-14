#!/bin/bash

# Запуск всех контейнеров с помощью Docker Compose
mkdir www
mkdir www/media
mkdir www/static
mkdir postgresql
cd frontend/long_memory/
npm install
npm run build
cd ../..
cp frontend/long_memory/build/static www/static
docker-compose up -d
