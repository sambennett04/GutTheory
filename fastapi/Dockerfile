FROM python:3.9

WORKDIR /code

#SETTING the current working directory to code, but what should it really be
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt 

#copy app into container image
COPY ./app /code

CMD ["fastapi", "run", "main.py", "--port", "80"]