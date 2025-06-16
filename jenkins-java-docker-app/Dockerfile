# Use OpenJDK image
FROM openjdk:17-alpine

# Copy compiled class to container
COPY Main.java /app/Main.java

WORKDIR /app

# Compile the Java program
RUN javac Main.java

# Run the Java app
CMD ["java", "Main"]
