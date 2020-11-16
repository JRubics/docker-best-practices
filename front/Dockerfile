FROM node:12.19.0-alpine3.12 as builder

WORKDIR /app

COPY package.json yarn.lock ./

RUN set -ex \
	&& apk add --no-cache yarn \
	&& yarn install

COPY ./ ./
RUN yarn run build

# Stage 2
FROM nginx:1.19-alpine

COPY --from=builder /app/dist /app
COPY nginx.conf /etc/nginx/conf.d
RUN rm /etc/nginx/conf.d/default.conf

EXPOSE 80
