import configparser
import inspect

config = None

class MyError():

  def __init__(self, et):
    self.config = configparser.RawConfigParser()
    self.config.read('ErrorMessages.properties')
    self.errorType = et

  def newError(self, optkey, key, **data):
    message = ''
    if optkey:
      return(key)
    if(key):
      message = self.config.get(self.errorType, key)
    if(data):
      for key, value in data.items():
        message = message + ", " f"{key}: {value}"
    return message

      

    


# le = MyError('LexerErrors')

# print(le.newError('ERR-LEX-001'))
