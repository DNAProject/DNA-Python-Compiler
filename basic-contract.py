Cversion = '2.0.0'
from DNA.interop.System.Runtime import Log

def Main(operation, args):
    if operation == 'LogTest':
        return LogTest()
    return False

def LogTest():
    Log('Hello, world!')
    return True
