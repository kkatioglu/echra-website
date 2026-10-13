FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY *.html /usr/share/nginx/html/
COPY style.css echra-logo.png /usr/share/nginx/html/
EXPOSE 8080
