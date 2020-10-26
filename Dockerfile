FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
#RUN pip uninstall -r requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./run.py" ]