# Imagen base liviana con Nginx
FROM nginx:alpine

# Elimina contenido por defecto
RUN rm -rf /usr/share/nginx/html/*

# Copia el contenido del sitio a la ruta pública de Nginx
COPY index.html /usr/share/nginx/html/index.html
COPY bienvenida.html /usr/share/nginx/html/bienvenida.html
COPY data/ /usr/share/nginx/html/data/

# Puerto expuesto (opcional para pruebas locales)
EXPOSE 80

# El contenedor arranca con Nginx en primer plano
CMD ["nginx", "-g", "daemon off;"]
