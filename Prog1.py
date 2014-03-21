'''
Created on Mar 20, 2014

@author: Dell
'''

import sys
import pprint 
import re


def create_candidates(token):
    '''Create all possible candidates for the given token'''
    letters_dict={}
    result = '^'
    i=0
    l=len(token)
    while (i<l):
        letter=token[i]
        if (letter in letters_dict):
            letters_dict[letter]+= 1
           
        else:
            letters_dict[letter]=1 
        i += 1         
    pprint(letters_dict)
    dict_len=len(letters_dict.keys())
    
    for x in letters_dict: 
        while (letters_dict.get(x)>1):
            print()
            if ((letters_dict.get(x)%2)!=0):
                letters_dict.get(x)= (letters_dict.get(x)/2) +1
            else: 
                letters_dict.get(x)= letters_dict.get(x)/2    
#     while (l!=dict_len):
#         count=0
#         for x in letters_dict:
#             #i=0
#             count=letters_dict.get(x)
#             
            
                
    return -1


    
    
def main():
    for line in sys.stdin.readlines():
        words = line.split('^[a-zA-Z0-9]')
        if (len(words)!=0):
            for term in words: 
                create_candidates(term)
        else: 
            continue

if __name__=='__main__':
    main() 
        
