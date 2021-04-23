"""
Implementation of the main simulation class.
"""

from array import Array
from llistqueue import Queue
from agent import TicketAgent
from passenger import Passenger
import random
random.seed(4500)

class TicketCounterSimulation :
    """
    Create a simulation object.
    """
    def __init__( self, numAgents, numMinutes, betweenTime, serviceTime ):
        """
        Parameters supplied by the user.
        """
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

# Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array( numAgents )
        for i in range( numAgents ) :
            self._theAgents[i] = TicketAgent(i+1)

# Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    def run( self ):
        """
        Run the simulation using the parameters supplied earlier.
        """
        for curTime in range(self._numMinutes + 1) :
            self._handleArrival( curTime )
            self._handleBeginService( curTime )
            self._handleEndService( curTime )

    def _handleArrival(self, curTime ):
        """
        Makes changes according to 1st rule.
        """
        prob_number = random.random()
        if prob_number <= self._arriveProb:
            self._numPassengers += 1
            passenger = Passenger(self._numPassengers, curTime)
            self._passengerQ.enqueue(passenger)
            print(f"Time {curTime}: Passenger {self._numPassengers} arrived.")

    def _handleBeginService(self, curTime):
        """
        Makes changes according to 2nd rule.
        """
        for agent in self._theAgents:
            if (not self._passengerQ.isEmpty() and
                agent.isFree()):
                passenger = self._passengerQ.dequeue()
                self._totalWaitTime += (curTime - passenger._arrivalTime)
                agent.startService(passenger, curTime + self._serviceTime)
                print(f"Time {curTime}: Agent {agent._idNum} started serving p\
assenger {passenger._idNum}.")
                
    def _handleEndService(self, curTime):
        """
        Makes changes according to 3rd rule.
        """
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                passenger = agent.stopService()
                print(f"Time {curTime}: Agent {agent._idNum} stopped serving p\
assenger {passenger._idNum}.")

    def printResults( self ):
        """
        Print the simulation results.
        """
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float( self._totalWaitTime ) / numServed
        print( "" )
        print( "Number of passengers served = ", numServed )
        print( "Number of passengers remaining in line = %d" %
        len(self._passengerQ) )
        print( "The average wait time was %4.2f minutes." % avgWait )

# The remaining methods that have yet to be implemented.
# def _handleArrive( curTime ): # Handles simulation rule #1.
# def _handleBeginService( curTime ): # Handles simulation rule #2.
# def _handleEndService( curTime ): # Handles simulation rule #3.

if __name__ == "__main__":
    sim = TicketCounterSimulation(2, 100, 2, 3)
    sim.run()
    sim.printResults()
    