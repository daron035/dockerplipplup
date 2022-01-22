FROM python:3.9.6-alpine as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

RUN pip install --upgrade pip

COPY . .


COPY ./req.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r req.txt


FROM python:3.9.6-alpine

RUN mkdir -p /home/app

RUN addgroup -S app && adduser -S app -G app

# RUN groupadd app
# RUN useradd -m -g app app -p PASSWORD
# RUN usermod -aG app app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
#RUN mkdir $APP_HOME/static

WORKDIR $APP_HOME

RUN apk update && apk add libpq postgresql postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/req.txt .
RUN pip install --no-cache /wheels/*

COPY ./entrypoint.sh $APP_HOME

COPY . $APP_HOME

RUN chown -R app:app $APP_HOME

USER app
RUN chmod +x /home/app/web/entrypoint.sh

ENTRYPOINT ["/home/app/web/entrypoint.sh"]
