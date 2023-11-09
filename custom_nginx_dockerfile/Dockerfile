# Use the Nginx image from Docker Hub as the base image
FROM nginx

# Remove the default Nginx HTML file
RUN rm /usr/share/nginx/html/index.html

# Copy the custom HTML file into the Nginx server directory
COPY ./index.html /usr/share/nginx/html/index.html

# Expose port 80 to the outside once the container has launched
EXPOSE 80

# Start Nginx when the container has provisioned
CMD ["nginx", "-g", "daemon off;"]
