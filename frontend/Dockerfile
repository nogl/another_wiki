FROM node:16

WORKDIR /app

# Copia el package.json
COPY package.json .

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos
COPY . .

# Cambia a un usuario no privilegiado
RUN chown -R node:node /app
USER node

# Expone el puerto 3000
EXPOSE 3000

# Inicia el servidor usando npx
CMD ["npx", "serve", "public"]
