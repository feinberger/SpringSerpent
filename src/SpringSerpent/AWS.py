'''aws.py: This is the python module for functions relating to amazon web services

This python module is used to interface with the amazon webservices set up for the
Tempomatic Hub. This will configure and connect the device to the Thing and publish
messages as required. 

'''

import json
import time
import os

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


class AWSHandler:
    ''' A class to handle AWS Interaction '''

    def __init__(self):
        ''' AWS Handler initialization '''

        # AWS Parameters
        self.host = None  # AWS Endpoint
        self.port = None  # AWS Port
        self.root_cert = None  # Path to AWS Root CA Certificate
        self.certificate = None  # Path to AWS Thing Device Certificate
        self.private_key = None  # Path to AWS Thing Device Private Key
        self.client_id = None  # Client ID in AWS

        # AWS Variables
        self.aws_mqtt_client = None  # AWS MQTT Client Object

        # Class flags
        self.configured_flag = False  # Indication if  aws handler parameters loaded
        self.aws_initialized = (
            False
        )  # Indication if aws handler mqtt client initialized

    def load_configuration(self):
        ''' Function that parses json configuration file and updates class
        settings/configurations
        '''
        # Variable to keep track of errors
        configure_error = False

        print('Loading AWS Configuration...')

        # Find aws_configuration file

        current_path = os.getcwd()
        system_path = None

        # Search for paths until found root of Spring-Serpent
        while current_path != system_path:
            current_path = os.path.dirname(current_path)
            if os.path.exists(os.path.join(current_path, 'Spring-Serpent')):
                system_path = current_path

        # SpringSerpent needs to be appended to get correct path
        system_path = os.path.join(system_path, 'Spring-Serpent')

        # Find configuration folder
        config_path = os.path.join(system_path, 'configuration')

        # Path for aws_configuration.json
        configuration_file = os.path.join(config_path, 'aws_configuration.json')

        # Open and serialize JSON config file to python dictionary
        with open(configuration_file, 'r') as json_config_file:
            configuration = json.load(json_config_file)

        # Update Host from config file
        if 'Host' in configuration:
            self.host = configuration['Host']
            print(self.host)
        else:
            print('Configuration file is missing Host! Update configuration file!')
            configure_error = True

        # Update Port from config file
        if 'Port' in configuration:
            self.port = int(configuration['Port'])
        else:
            print('Configuration file is missing Port! Update configuration file!')
            configure_error = True

        # Update Root CA from config file
        if 'Root CA' in configuration:
            self.root_cert = configuration['Root CA']
        else:
            print('Configuration file is missing Root CA! Update configuration file!')
            configure_error = True

        # Update Device Certificate from config file
        if 'Device Certificate' in configuration:
            self.certificate = configuration['Device Certificate']
        else:
            print(
                'Configuration file is missing Device Certificate! Update configuration file!'
            )
            configure_error = True

        # Update Device Certificate from config file
        if 'Private Key' in configuration:
            self.private_key = configuration['Private Key']
        else:
            print(
                'Configuration file is missing Private Key! Update configuration file!'
            )
            configure_error = True

        # Update Client ID from config file
        if 'Client ID' in configuration:
            self.client_id = configuration['Client ID']
        else:
            print('Configuration file is missing Client ID! Update configuration file!')
            configure_error = True

        # AWS Handler only configured if no errors loading configuration
        if configure_error:
            self.configured_flag = False
        else:
            self.configured_flag = True

    def initialize_mqtt_client(self):
        ''' This function initializes AWS MQTT Client

            Returns: bool - initialized occured
        '''

        if self.configured_flag:
            # Create mqtt client from AWS IoT SDK
            self.aws_mqtt_client = AWSIoTMQTTClient(self.client_id)

            # Configure aws endpoint from configuration
            self.aws_mqtt_client.configureEndpoint(self.host, self.port)

            # Configure aws credentials from configuration
            self.aws_mqtt_client.configureCredentials(
                self.root_cert, self.private_key, self.certificate
            )

            # MQTT Default Configuration Settings (from AWS IoT Developer Guide Tutorial)
            self.aws_mqtt_client.configureAutoReconnectBackoffTime(1, 32, 20)
            self.aws_mqtt_client.configureOfflinePublishQueueing(-1)
            self.aws_mqtt_client.configureDrainingFrequency(2) 
            self.aws_mqtt_client.configureConnectDisconnectTimeout(10)
            self.aws_mqtt_client.configureMQTTOperationTimeout(5)

            # Connect to AWS IoT
            # TODO: Handle connection issues!
            self.aws_mqtt_client.connect()

            # Not sure if this wait is needed, but example code has it
            time.sleep(2)

            # If no connection exceptions, mqtt IoT client is initialized
            self.aws_initialized = True

            print('AWS Connected')

        else:
            print('AWS Handler not configured, please reload ')

    def send_message(self, topic, payload):
        ''' Sends a payload json message '''

        # Only send message if mqtt client is initialized
        if self.aws_initialized:
            # Empty message dictionary (to be converted to JSON)
            message = {}

            # Add payload to message
            message['Payload'] = payload

            # Convert serialized data into string
            message_string = json.dumps(message)

            # Add topic to device topic
            message_topic = 'spring-serpent/' + topic

            # Publish topic to MQTT client with QoS of 1
            self.aws_mqtt_client.publish(message_topic, message_string, 1)
        else:
            print('AWS is not initialized. Please intialize and re-send!')


if __name__ == '__main__':
    print('AWS Test')

    aws_handler = AWSHandler()
    aws_handler.load_configuration()

    aws_handler.initialize_mqtt_client()

    msg_payload = {}
    msg_payload['Command'] = 'Job Status'
    msg_payload['Part Number'] = '12345'
    msg_payload['Company Name'] = 'GlennCorp'
    msg_payload['Timestamp'] = '10/20/2019 4:16:23'

    aws_handler.send_message('job', msg_payload)
