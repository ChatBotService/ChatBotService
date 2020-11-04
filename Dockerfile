FROM python:3-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
#RUN pip uninstall -r requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080
CMD [ "python", "./run.py" ]