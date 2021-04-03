FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]