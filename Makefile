project:
	django-admin startproject color_cluster
run:
	./run.sh
note:
	jupyter notebook

install:
	pip install -r requirements.txt

build:
	docker build -t django .

drun:
	docker run -p 5000:5000 -it django

stop:
	docker stop $(docker ps -q)
