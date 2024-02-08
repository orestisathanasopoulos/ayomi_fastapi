FROM node:20-alpine as build

WORKDIR /ayomi-calculator

COPY pnpm-lock.yaml package.json ./

RUN npm install -g pnpm

RUN pnpm i 

COPY . .

RUN pnpm run build

EXPOSE 5173
EXPOSE 4173

CMD [ "pnpm" , "preview"]