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
    def __init__(self,start):
        self.start = start
        self.counter = 0
    def generate(self):
        serial = self.start + self.counter
        self.counter += 1
        return serial
    def reset(self):
        self.counter = 0

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.start + self.counter}>"