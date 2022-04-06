build:
	cd infra/ && docker build -t iris-ml-image  -f Dockerfile ..

run:
	docker run -it --name iris_model --network host --rm -p 8080:8080 iris-ml-image

rm:
	docker rm -f iris-ml-image
