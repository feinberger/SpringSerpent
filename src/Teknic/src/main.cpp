#include <stdio.h>	
#include <string>
#include <iostream>
#include <thread>

#include "../include/drivers/motors.hpp"
#include "../include/drivers/commands.hpp"
#include "../include/drivers/messaging.hpp"
#include "../include/zmq/zhelpers.hpp"

#include "../include/teknic/pubSysCls.h"
#include "jsoncpp/json/json.h"

using namespace sFnd;

int main(int argc, char const *argv[])
{
    // Create instance of system manager for teknic
    SysManager teknicManager;

    // Open Port to SC-HUB (Motor Controller)
    IPort &motorController = openMotorController(teknicManager);

    // Initialize z-axis motor
    INode &zaxisMotor = openMotor(teknicManager, motorController, ZAXIS_MOTOR);
    double position = zaxisMotor.Motion.PosnMeasured.Value();
    std::cout << std::to_string(position);

    //  Prepare context and socket
    zmq::context_t context (1);
    zmq::socket_t motorServer (context, ZMQ_REP);
    zmq::socket_t motorStatusPublisher (context, ZMQ_PUB);

    // Initialize motor status publisher
    initalizeMotorStatusPublisher(motorStatusPublisher, 5556);

    // Initialize server
    initalizeMotorServer(motorServer, 5555);

    // Start Command Processing Thread
    std::thread statusThread(sendStatus, std::ref(zaxisMotor), std::ref(motorStatusPublisher));

    // Create variables for server commands
    std::string receivedMsg;

    while(1)
    {
        // Wait for commands from main client
        receivedMsg = s_recv(motorServer);
        std::cout << receivedMsg << std::endl;

        // Send confirmation receipt
        s_send(motorServer, "Success");

        // Parse message
        determineCommand(receivedMsg, zaxisMotor);
        double position = zaxisMotor.Motion.PosnMeasured.Value();
        std::cout << std::to_string(position);

    }
    statusThread.join(); 

    return 0;
}
