# Use the official Golang image
FROM golang:1.20

# Set working directory inside the container
WORKDIR /app

# Copy all files
COPY . .

# Build the Go app
RUN go build -o main .

# Expose the port used by the app
EXPOSE 8001

# Run the compiled app
CMD ["./main"]
