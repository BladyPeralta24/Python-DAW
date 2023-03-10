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
                  ;~~,__
   :-....,-------'`-'._.'
    `-,,,  ,       ,'~~'
        ; ,'~.__; /
        :|      :|
        `-'     `-'
"""
        else:
            return f"""
                  ;~~,__
   :-....,-------'`-'._.'
    `-,,,  ,       ,'~~'
        ; ,'~.__; /--.
        :| :|   :|``(;
        `-'`-'  `-'              
"""

class Gato(Animal):
    
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
while j < 1020:
    
    if i == 0:
        i = 1
        os.system('clear')
        print(perro.moverse())
        perro.pata = True
        print(perro.moverse())
    else:
        i = 0
        perro.pata = True
        os.system('clear')
        print(perro.moverse())


# gato = Gato()

# print(gato.hacer_sonido())
















# i = 0
# j = 0
# while( j < 1020):
    
#     if i == 0:
#         i = 1
#         os.system('clear')
#         print("···········\n···········\n···········\n···········\n···········\n···········\n···········\n···········\n")
#     else:
#         i = 0
#         os.system('clear')
#         print("XXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\nXXXXXXXXXXX\n")
#     j += 1