# Author: Sakthi Santhosh
# Created on: 08/09/2023
FROM python:3.11-alpine3.17 AS build

COPY ./requirements.txt /

RUN pip3 install -q -r /requirements.txt

FROM python:3.11-alpine3.17 AS final

WORKDIR /app/

COPY --from=build /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY ./ ./

EXPOSE 5000/tcp

ENTRYPOINT ["python3", "./run.py"]
