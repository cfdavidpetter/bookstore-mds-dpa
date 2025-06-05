FROM node:18

RUN apt-get update && apt-get install -y \
  libgtk2.0-0 libgtk-3-0 libgbm-dev \
  libnotify-dev libnss3 libxss1 libasound2 \
  libxtst6 xauth xvfb

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD npm run dev