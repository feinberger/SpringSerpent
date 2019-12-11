#include <thread>
#include <iostream> 
#include <time.h>
#include <string.h>

#include "../include/drivers/commands.hpp"
#include "../include/drivers/motors.hpp"
#include "jsoncpp/json/json.h"

void sendStatus(INode &zmotor, zmq::socket_t &publisher)
{
	struct timespec deadline;		// Deadline for scheduler to re-run
    double rpm, position;
    std::string sendMsg;
    Json::Value payload;
    Json::FastWriter fastwriter;
    s_send(publisher, "Start");

	// Get current time for initial deadline
	clock_gettime(0, &deadline);

    //https://timmurphy.org/2009/09/29/nanosleep-in-c-c/
    while(1)
    {
        // Get z-axis rpm and position data from motor
        if (!zmotor.Motion.MoveIsDone())
        {
            rpm = zmotor.Motion.VelMeasured.Value();
        }
        else
        {
            rpm = 0;
        }
        position = zmotor.Motion.PosnMeasured.Value();
        
        // Pack json msg
        payload["Z RPM"] = std::to_string(rpm);
        payload["Z Position"] = std::to_string(position);
        sendMsg = fastwriter.write(payload);

		// Sleep until absolute deadline
		clock_nanosleep(0, TIMER_ABSTIME, &deadline, NULL);
        s_send(publisher, sendMsg);

		// Increment deadline by 100ms to create a systick
		// Add second if nanoseconds overflows
		if(deadline.tv_nsec >= (NSEC_PER_SEC - 10*NSEC_PER_MSEC))
		{
			deadline.tv_nsec = (100*NSEC_PER_MSEC) - (NSEC_PER_SEC - deadline.tv_nsec);
			deadline.tv_sec += 1;
		}
		else
		{
			deadline.tv_nsec += 100 * NSEC_PER_MSEC;
		}
    }
}

void determineCommand(std::string message, INode &zMotor)
{
    Json::Reader reader = {};
    Json::Value obj;
    Json::Value payload, command, position;

    // Parse JSON msg
    reader.parse(message, obj);

    // Get Payload
    payload = obj["Payload"];

    // Determine Command
    command = payload["Command"];

    // Determine command
    if (command.asString() == "Home Z")
    {
        std::cout << "Home Z Axis" << std::endl;
        homeMotor(zMotor);
    }
    else if (command.asString() == "Move Z")
    {
        position = payload["Position"];
        std::cout << "Move Z Axis " << position.asString() << " Counts" << std::endl;
        moveMotor(zMotor, position.asInt());
    }
}
