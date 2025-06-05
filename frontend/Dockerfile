# Development stage
FROM node:18 as development

RUN apt-get update && apt-get install -y \
  libgtk2.0-0 libgtk-3-0 libgbm-dev \
  libnotify-dev libnss3 libxss1 libasound2 \
  libxtst6 xauth xvfb

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]

# Production stage
FROM node:18 as production

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}

RUN npm run build

EXPOSE 80
ENV PORT=80

CMD ["npm", "run", "start"]
