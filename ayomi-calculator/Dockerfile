FROM node:20-alpine

WORKDIR /ayomi-calculator

COPY pnpm-lock.yaml package.json ./

RUN npm install -g pnpm

RUN pnpm i 

COPY . .

RUN pnpm run build

EXPOSE 5173


CMD [ "pnpm" , "dev"]