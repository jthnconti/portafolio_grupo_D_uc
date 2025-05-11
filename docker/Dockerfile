FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install -g gh-pages && npm install
COPY . .
CMD ["npx", "gh-pages", "-d", ".", "-r", "https://x-access-token:$PERSONAL_TOKEN@github.com/jthnconti/portafolio_grupo_D_uc.git"]
