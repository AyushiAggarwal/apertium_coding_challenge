Apertium <br>
GSOC'14 <br>
Coding Challenge <br>

'''
Created by Ayushi
'''

IRC nick: Ayushi <br>
mail: ayushi10026@iiitd.ac.in

The aim is to create a word repetition generator(Prog1) and a repetition remover(Prog 2):

1. Prog1 - Take a sentence as input and create all possible candidates by reduction of the given words such that the letters with frequency >=3 is reduced to half their frequency.
   Usage: echo 'Helllooo!!!' | python Prog1.py

   Output: 
   ^Helllooo/Helloo/Hello/Helo$ <br>
   ^!!!/!!!$ <br>

2. Prog2 - Take all the output candidates from Prog1.py and reduce them to their most apt word by mapping to a morphological dictionary(en only, for now). 

   Usage : echo 'Helllooo!!!' | python Prog1.py | python Prog2.py
   
   Output: 
   ^Hello$ <br>
   ^!!!$  <br>
