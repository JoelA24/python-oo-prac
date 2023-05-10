"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 0):
        """ Create a new generator beginning at 0"""
        self.start = self.next = start

    def __repr__(self):
        """ Represnet what is happening """
        return f"<SerialGenerator start={self.start} next = {self.next}"
    
    def generate(self):
        """ Generate and return the new serial number """

        self.next += 1
        return self.next - 1
    
    def restart(self):
        """ Reset the serial number generator to orginal number """

        self.next = self.start
