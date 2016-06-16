import fileinput
import sys
from pip._vendor.distlib.compat import raw_input

def start():
    text = raw_input("String to prepend?")
    for line in fileinput.input([sys.argv[1]], inplace=True):
        final = '{t}'.format(t=text) + '{l}'.format(l=line)
        sys.stdout.write(final)
       
start()
            