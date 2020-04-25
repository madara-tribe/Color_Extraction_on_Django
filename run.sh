#!/bin/sh
python color_cluster/manage.py migrate
python color_cluster/manage.py runserver
