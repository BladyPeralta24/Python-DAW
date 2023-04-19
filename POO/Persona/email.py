from abc import abstractmethod
import re

class Email():
  
    @abstractmethod
    def validar(email):       
        return re.match("[a-z]+@[a-z]+\..{2,3}" , email)