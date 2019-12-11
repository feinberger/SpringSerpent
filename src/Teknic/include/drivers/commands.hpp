#ifndef __COMMANDS_HPP_INCLUDED__
#define __COMMANDS_HPP_INCLUDED__

#include "../teknic/pubSysCls.h"
#include "../zmq/zhelpers.hpp"

// System Definitions
#define ERROR (-1)
#define NSEC_PER_SEC (1000000000)
#define NSEC_PER_MSEC (1000000)
#define NSEC_PER_MICROSEC (1000)
#define MSEC_PER_SEC (1000

using namespace sFnd;

void sendStatus(INode &zmotor, zmq::socket_t &publisher);

void determineCommand(std::string message, INode &zMotor);

#endif