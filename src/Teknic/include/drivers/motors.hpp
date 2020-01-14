/*!
	* @file motors.hpp
	* @brief Functions used for Teknic SC Motors
	*
	* This header file contains functions related to teknic motors
	* and the SC Hub
	*
	* @author Glenn Feinberg
	* @date: 12/6/2019
	* @version 1.0
*/

#ifndef __MOTORS_HPP_INCLUDED__
#define __MOTORS_HPP_INCLUDED__


#include <iostream>
#include "../teknic/pubSysCls.h"

using namespace sFnd;

#define ZAXIS_MOTOR 		0
#define SPINDLE_MOTOR 		1

#define ZAXIS_FEED_RATE			500
#define ZAXIS_FEED_MAX_RATE		1000
#define ZAXIS_FEED_MIN_RATE		100

/*!
 * @brief Function to open/initialize motor controller
 *
 * This function opens the port to the SC-HUB (motor controller) by 
 * finding available ports, assigning the port to sys manager, and 
 * returns port of motor controller
 * 
 * @param teknicManager teknic Sys Manager class
 *
 * @return IPort
*/
IPort &openMotorController(SysManager &teknicManager);

/*!
 * @brief Function to open/initialize motor
 *
 * This function opens a node
 * 
 * @param teknicManager teknic Sys Manager class
 * @param motorController Teknic Port Class (SC Hub)
 * @param motorSelection integer for which node number to open
 *
 * @return INode
*/
INode &openMotor(SysManager &teknicManager, IPort &motorController, int motorSelection);


/*!
 * @brief Function to home motor
 *
 * This function homes the given motor
 * 
 * @param motor INode class
 *
 * @return bool
*/
bool homeMotor(INode &motor);

/*!
 * @brief Function to move motor
 *
 * This function moves the motor 
 * 
 * @param motor INode class
 *
 * @return bool
*/
bool moveMotor(INode &motor, int32 position_count);


#endif