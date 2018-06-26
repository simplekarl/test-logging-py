from docker.sltc.local/python

WORKDIR /app/
ADD requirements.txt /app/

RUN pip install -r requirements.txt

ADD . /app/

CMD python3 loggingtest.py