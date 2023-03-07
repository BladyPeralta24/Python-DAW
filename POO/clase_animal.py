from abc import ABC, abstractmethod
import os
class Animal(ABC):
    
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    @abstractmethod
    def moverse(self):
        pass
    

class Perro(Animal):
    
    def __init__(self, pata):
        super().__init__()
        
        self.pata = pata
    
    def hacer_sonido(self):
        return f"""
    / \__
  (    @\___
  /         O
 /   (_____/    Guau!
/_____/   U  
"""
    
    def moverse(self):
        if self.pata:
            return f"""
      .-.   .-.
     /   \ /   \ 
 .-. |    |    | .-.
/   \ \  / \  / /   \s
|   |  '`.-.`'  |   |
 \_.' .-`   `-. '._/
   .-'         '-.
  /               \s
  |               |
   \             /
    '.___...___.'
"""
        else:
            return f"""
                                      .-.   .-.
                                     /   \ /   \ 
                                 .-. |    |    | .-.
                                /   \ \  / \  / /   \s
                                |   |  '`.-.`'  |   |
                                 \_.' .-`   `-. '._/
                                   .-'         '-.
                                  /               \s
                                  |               |
                                   \             /
                                    '.___...___.'
                                    
"""

class Gato(Animal):
    
    def __init__(self, pata):
        super().__init__()
        self.pata = pata
    
    def hacer_sonido(self):
        return f"""
 .       .
 |\_---_/|
/   o_o   \s
|    U    |
\  ._I_.  /     Miauh!
 `-_____-'   
"""

    def moverse(self):
        if self.pata:
            return f"""
                                      .-.   .-.
                                     /   \ /   \ 
                                 .-. |    |    | .-.
                                /   \ \  / \  / /   \s
                                |   |  '`.-.`'  |   |
                                 \_.' .-`   `-. '._/
                                   .-'         '-.
                                  /               \s
                                  |               |
                                   \             /
                                    '.___...___.'
"""
        else:
            return f"""
                                                                          .-.   .-.
                                                                         /   \ /   \ 
                                                                     .-. |    |    | .-.
                                                                    /   \ \  / \  / /   \s
                                                                    |   |  '`.-.`'  |   |
                                                                     \_.' .-`   `-. '._/
                                                                       .-'         '-.
                                                                      /               \s
                                                                      |               |
                                                                       \             /
                                                                        '.___...___.'
                                    
"""






perro = Perro(False)

print(perro.hacer_sonido())

i = 0
j = 0
while (j < 1200):
    if i == 0:
        i = 1
        perro.pata = False
        os.system('clear')
        print(perro.moverse())
    else:
        i = 0
        perro.pata = True
        os.system('clear')
        print(perro.moverse())
        
    j += 1


gato = Gato(False)
print(gato.hacer_sonido())

while (j < 1200):
    if i == 0:
        i = 1
        gato.pata = False
        os.system('clear')
        print(gato.moverse())
    else:
        i = 0
        gato.pata = True
        os.system('clear')
        print(gato.moverse())
        
    j += 1
















""" i = 0
j = 0
while( j < 1020):
  
    if i == 0:
        i = 1
        os.system('clear')
        print("···········\n···········\n···········\n···········\n···········\n···········\n···········\n···········\n")
    else:
        i = 0
        os.system('clear')
        print("XXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\n")
    j += 1 """