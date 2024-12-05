# Use the official Node.js image as the base
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /myapp

# Copy the JavaScript file and data file into the container
COPY ./app.js .
COPY ./data.txt .

# Specify the command to run the JavaScript application
CMD ["node", "app.js"]
