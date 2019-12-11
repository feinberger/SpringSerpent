#Makefile addition for SOURCES
#This is an additional makefile to help clean up and organize

#location of sourcefiles
SOURCE_DIR = ./src/

#location of includes
INCLUDE_DIR = ./include/

#libraries
LIBRARIES = -lsFoundation20 -lzmq -ljsoncpp -lpthread

#build directory
BUILD_DIR = ./build/

#Source files
SOURCES = main.cpp motors.cpp commands.cpp messaging.cpp

INCLUDES = -I$(INCLUDE_DIR)drivers  -I$(INCLUDE_DIR)teknic  -I$(INCLUDE_DIR)zmq

# Object build rule
OBJECTS := $(SOURCES:.cpp=.o)