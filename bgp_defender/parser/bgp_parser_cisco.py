from pprint import pprint
import re
"""
Holds the BGP Parser object
"""


table = open('cisco-table.txt', 'r')

pattern = re.compile('.[0-9].{1,}')
ip = re.compile('\W\W\s\s[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}\/[0-9]{1,3}')
#prefer = 

for AS in table:
        iptable = ip.findall(AS)
        validation = pattern.findall(AS, 63)    
        #The AS Numbers start on position = 63
        print("    {     ","\n IP Address",iptable,"\n   }   "," \n {  ","\n AS Number",validation,"\n   }  ")  