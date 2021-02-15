# build
FROM openjdk:8 AS Stage1
WORKDIR /src
COPY Test.java .
RUN javac Test.java

# execution
FROM alpine
RUN apk add openjdk8-jre
WORKDIR /app
COPY --from=Stage1 /src/Test.class .
CMD java Test
