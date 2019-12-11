#include <iostream>
#include <sstream>

#include "../include/zmq/zhelpers.hpp"
#include "../include/drivers/messaging.hpp"

void initalizeMotorServer(zmq::socket_t &server, int port)
{
    // Command
    std::string msg;

    // Create address
    std::string address;
    std::stringstream ss;

    address = "tcp://*:" + std::to_string(port);

    std::cout << address << std::endl;
    server.bind(address);
    
    // Wait for connect request from client
    msg = s_recv(server);

    std::cout << msg << std::endl;

    // Send Success Message after receiving
    s_send(server, "Success");
}

void initalizeMotorStatusPublisher(zmq::socket_t &publisher, int port)
{
    // Command
    std::string msg;

    // Create address
    std::string address;
    std::stringstream ss;

    address = "tcp://*:" + std::to_string(port);

    std::cout << address << std::endl;
    publisher.bind(address);
}