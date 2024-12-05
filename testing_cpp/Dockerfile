# Use an official C++ base image
FROM gcc:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the C++ source file into the container
COPY main.cpp .

# Run g++ to compile the C++ source code
RUN g++ -o main main.cpp

# Command to run the compiled program
CMD ["./main"]
