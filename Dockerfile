FROM alpine
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    rm -r /root/.cache
COPY ./requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . /app
WORKDIR /app
RUN nosetests /app/tests
CMD python3 phorum/main.py
