# base image
FROM openjdk:8

# directory where you want to the copy the code
# set the current directory to the /src
WORKDIR /src

# copy test file to /src
COPY ./Test.java .

# compile the code while building the image
RUN javac ./Test.java

# run the java class inside the container
CMD java Test
