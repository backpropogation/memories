FROM node:8.9.1 AS client

WORKDIR /app/user/

COPY ./client/package.json /app/user/package.json
COPY ./client/yarn.lock /app/user/yarn.lock
RUN yarn install

COPY ./client /app/user/
RUN yarn build

#########################################

FROM python:3.7-slim as server

WORKDIR /app/user

COPY ./server/requirements.txt /app/user/
RUN pip install -r requirements.txt

COPY ./server /app/user

RUN python manage.py collectstatic --no-input

#########################################

FROM nginx:1.13

RUN rm -v /etc/nginx/nginx.conf
COPY ./nginx/nginx.conf ./nginx/very.crt ./nginx/very.key /etc/nginx/


COPY --from=client /app/user/dist /app/user/dist
COPY --from=server /server/static /app/user/dist
