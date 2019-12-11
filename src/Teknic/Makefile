# This is the main makefile for the teknic code application.
# This combined with the other makefile to create and run the
# application code

include ./src/sources.mk

# Target
TARGET = teknic

# Determine which platform (HOST or RPI)
ifeq ($(PLATFORM),HOST)
	CC = g++
else ifeq ($(PLATFORM),RPI)
	CC = arm-linux-gnueabihf-g++
else
	CC = g++
endif

#Build Executable
.PHONY: build
build: compile-all 
	$(CC) $(addprefix $(BUILD_DIR), $(OBJECTS)) $(LIBRARIES) -o $(BUILD_DIR)$(TARGET).out

#Create object files for all sources in project
.PHONY: compile-all
compile-all: $(OBJECTS)

#Clean (remove files)
.PHONY: clean
clean:
	cd $(BUILD_DIR) && rm -rf *.o *.asm *.i *.map *.out *.elf *.dep

#Build object file (.o) from a .c file
%.o : $(SOURCE_DIR)%.cpp
	$(CC) -c $< -o $(BUILD_DIR)$@ $(CPPFLAGS) $(INCLUDES)