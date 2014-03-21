Apertium
GSOC'14
Coding Challenge 
=========================
'''
Created by Ayushi
'''

IRC nick: Ayushi
mail: ayushi10026@iiitd.ac.in

The aim is to create 2 programs such that: 

1. Prog1 - Take a sentence as input and create all possible candidates by reduction of the given words such that the letters with frequency >=3 is reduced to half their frequency.

Usage: echo 'Helllooo!!!' | python Prog1.py

Output: 
^Helllooo/Helloo/Hello/Helo$
^!!!/!!!$

2. Prog2 - Take all the output candidates from Prog1.py and reduce them to their most apt word by mapping to a morphological dictionary(en only, for now). 

Usage : echo 'Helllooo!!!' | python Prog1.py | python Prog2.py

Output: 
 
^Hello$
^!!!$
