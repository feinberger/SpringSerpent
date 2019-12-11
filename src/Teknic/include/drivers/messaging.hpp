#ifndef __MESSAGING_HPP_INCLUDED__
#define __MESSAGING_HPP_INCLUDED__

#include "../zmq/zhelpers.hpp"

/*!
 * @brief Function to open the client socket for receiving commands
 *
 * This function intializes the zmq client socket that will receive
 * commands from the main controller
 * 
 * @param port port number to connect to server
 *
 * @return void
*/
void initalizeMotorServer(zmq::socket_t &server, int port);

/*!
 * @brief Function to open the client socket for receiving commands
 *
 * This function intializes the zmq client socket that will receive
 * commands from the main controller
 * 
 * @param port port number to connect to server
 *
 * @return void
*/
void initalizeMotorStatusPublisher(zmq::socket_t &publisher, int port);

#endif