FROM node:18-alpine
WORKDIR /app
COPY . .
RUN npm install -g gh-pages
RUN npm install
CMD ["sh", "-c", "npm run deploy"]
