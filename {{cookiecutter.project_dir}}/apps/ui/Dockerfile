FROM node:16-alpine3.14 as build

ENV YARN_VERSION 1.22.5

RUN apk update

RUN apk add --no-cache --virtual .build-deps-yarn curl \
    && curl -fSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
    && tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \
    && ln -snf /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \
    && ln -snf /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \
    && rm yarn-v$YARN_VERSION.tar.gz \
    && apk del .build-deps-yarn

RUN apk add nginx

COPY ./nginx/nginx.conf /etc/nginx/http.d/default.conf

FROM build as react-app
# set working directory
WORKDIR /app

# install app dependencies
COPY package.json ./
COPY . ./
RUN npm install && npm run build

FROM build

# set working directory
WORKDIR /app

RUN npm install express cors http http-proxy-middleware

COPY server.js ./

COPY --from=react-app /app/build /usr/share/nginx/html

CMD [ "sh", "-c", "nginx && node /app/server.js" ]
