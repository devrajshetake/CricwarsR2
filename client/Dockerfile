FROM node:16.15-alpine
WORKDIR /react
COPY package.json .
RUN npm install
COPY . .
RUN npm run build