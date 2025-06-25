# Use OpenJDK image
FROM public.ecr.aws/docker/library/openjdk:17-alpine



WORKDIR /app

# Copy compiled class to container
COPY src/Main.java /app/Main.java


# Compile the Java program
RUN javac Main.java

# Run the Java app
CMD ["java", "Main"]
