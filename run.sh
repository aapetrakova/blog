#!/bin/bash

chmod +x includes.sh
./includes.sh

cd tp_project_spring2024

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
