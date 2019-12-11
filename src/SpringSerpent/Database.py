'''Database.py: This is the python module for Database Functions

This python module is used to interface with the database and ORM that is
used to store the spring jobs. This contains function that create and 
configure the sqlalchemy ORM and the job database table used to store the
spring info.

'''

import os

from sqlalchemy import (Column, Float, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Base that used as a base for Database Object Classes
Base = declarative_base()


class JobDatabase:
    ''' A class to handle ORM jobs (springs) database '''

    def __init__(self):
        ''' init function for job database'''

        self.database_path = None
        self.session = None
        self.engine = None
        self.users_database = None

    def create_database(self):
        ''' function that finds correct path and creates database'''

        current_path = os.getcwd()
        system_path = None

        # Search for paths until found root of Spring-Serpent
        while current_path != system_path:
            current_path = os.path.dirname(current_path)
            if os.path.exists(os.path.join(current_path, 'Spring-Serpent')):
                system_path = current_path

        # SpringSerpent needs to be appended to get correct path
        system_path = os.path.join(system_path, 'Spring-Serpent')

        # Find database folder
        database_path = os.path.join(system_path, 'database')

        # Path for users.db
        jobs_database_file = os.path.join(database_path, 'jobs.db')

        # jobs_database_file = ':memory:'
        self.users_database = f'sqlite:///{jobs_database_file}'

    def create_engine(self):
        ''' function that creates the sqlalchemy orm engine'''
        # Create Database Engine
        self.engine = create_engine(self.users_database, echo=False)
        Base.metadata.create_all(self.engine)

    def create_session(self):
        ''' function that creates the sqlalchemy orm session'''
        # Create Database Session
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()


class Job(Base):
    ''' A class to provide an object structure for a Job Table '''

    # Table Name
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    part_number = Column(String)
    company_name = Column(String)
    spring_constant = Column(String)
    spring_length = Column(String)
    spring_type = Column(String)
    spring_wind_direction = Column(String)
    arbor_size = Column(String)
    wire_diameter = Column(String)
    feed_distance = Column(String)
    start_dead_turns = Column(String)
    live_turns = Column(String)
    live_turn_spacing = Column(String)
    end_dead_turns = Column(String)

    def __init__(self, part_number, company_name, spring_constant, spring_length, spring_type, spring_wind_direction,
                 arbor_size, wire_diameter, feed_distance, start_dead_turns, live_turns, live_turn_spacing,
                 end_dead_turns):
        ''' init function for creating an entry for a job'''
        self.part_number = part_number
        self.company_name = company_name
        self.spring_constant = spring_constant
        self.spring_length = spring_length
        self.spring_type = spring_type
        self.spring_wind_direction = spring_wind_direction
        self.arbor_size = arbor_size
        self.wire_diameter = wire_diameter
        self.feed_distance = feed_distance
        self.start_dead_turns = start_dead_turns
        self.live_turns = live_turns
        self.live_turn_spacing = live_turn_spacing
        self.end_dead_turns = end_dead_turns

    def __repr__(self):
        return f"<Job {self.part_number} - ({self.company_name})>"


# Create global job database instance
JobDatabase = JobDatabase()


def configure_database():
    ''' function for starting up the database'''
    print("Configuring Database...")
    JobDatabase.create_database()
    JobDatabase.create_engine()
    JobDatabase.create_session()


if __name__ == '__main__':
    # Create and configure database
    configure_database()
