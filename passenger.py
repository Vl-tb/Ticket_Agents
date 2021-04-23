"""
Used to store and manage information related to an airline passenger.
"""

class Passenger :
    """
    Creates a passenger object.
    """
    def __init__( self, idNum, arrivalTime ):
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    def idNum( self ) :
        """
        Gets the passenger's id number.
        """
        return self._idNum

    def timeArrived( self ) :
        """
        Gets the passenger's arrival time.
        """
        return self._arrivalTime
        