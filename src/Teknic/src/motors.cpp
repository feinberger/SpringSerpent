#include "../include/drivers/motors.hpp"
#include <stdio.h>	
#include <string>
#include <iostream>
#include "../include/teknic/pubSysCls.h"

using namespace sFnd;

IPort &openMotorController(SysManager &teknicManager)
{
    // Variable to store number of available ports
    size_t portCount = 0;

    // Vector list to store available COM ports
	std::vector<std::string> comHubPorts;

    // Find Com Ports
    SysManager::FindComHubPorts(comHubPorts);

    // TODO: Add no ports found error handling

    // Associate all ports with the teknic system manager
    for (portCount = 0; portCount < comHubPorts.size() && portCount < NET_CONTROLLER_MAX; portCount++) {   
        teknicManager.ComHubPort(portCount, comHubPorts[portCount].c_str());
    }

    // Open Port
    teknicManager.PortsOpen(portCount);

    // Motor Controller is first port on teknic manager
    IPort &motorController = teknicManager.Ports(0);

    return motorController;
}

INode &openMotor(SysManager &teknicManager, IPort &motorController, int motorSelection)
{
    // Create a Node object for the motor
    INode &motor = motorController.Nodes(motorSelection);

    // Disable motor for configuration loading
    motor.EnableReq(false);

    // Small delay for loading motor
    teknicManager.Delay(200);

    // Clear any stored alerts on motor
    motor.Status.AlertsClear();

    // Clear node stops on motor
    motor.Motion.NodeStopClear();

    // Re-enable motor for use
    motor.EnableReq(true);

    // Blocking function to wait for motor to be ready
    while (!motor.Motion.IsReady()) {};

    // TODO: Add timeout functionality errors

    return motor;
}

bool homeMotor(INode &motor)
{
    // Check for valid homing configuration
    if (motor.Motion.Homing.HomingValid())
    {
        // Start homing process
        motor.Motion.Homing.Initiate();

        // Wait for homing to complete
        while (!motor.Motion.Homing.WasHomed()) {};

        // TODO: Add homing timeout error handling
        return true;
    }
    else 
    {
        // TODO: Add no homing validation
        return false;
    }
}

bool moveMotor(INode &motor, int32 position_count)
{
    // Clear the rising edge Move done register
    motor.Motion.MoveWentDone();

    //Set the units for Acceleration and velocity to RPM/SEC
    motor.AccUnit(INode::RPM_PER_SEC);
    motor.VelUnit(INode::RPM);

    // Set motor acceleration limit
    motor.Motion.AccLimit = 100000;

    // Set motor velocity limit
    motor.Motion.VelLimit = 100;

    // Move motor
    motor.Motion.MovePosnStart(position_count);

    while (!motor.Motion.MoveIsDone()) {};
}