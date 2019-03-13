from alpine:latest

RUN apk add --no-cache python3-dev \
	&& pip3 install --upgrade pip

WORKDIR /todo

COPY . /todo

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["python manage.py"]
