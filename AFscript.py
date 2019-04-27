# coding=utf-8
# encoding: utf-8
#!/usr/bin/env python3
import sys
import os

class Automata:
    def __init__(self,Q,E,ft,I,F):
        self.Q = Q
        self.E = E
        self.ft = ft
        self.I = I
        self.F = F

def get_filename():
    if len(sys.argv) != 2:
        print("use: python3 AFscrpit.py <filename.txt>")
        exit(-1)
    else:
        filename = sys.argv[1]
        exists = os.path.isfile(filename)
        if not exists:
            print("FITXER NO EXISTEIX")
            exit(-1)
        return filename

def read_file(file_name):
    f = open(filename, 'r')
    plist = []
    for line in f:
        line = line.rstrip('\n')
        plist.append(line)

    a = Automata(plist[0].split(","),plist[1].split(","), plist[2].split(","),
                 plist[3].split(","), plist[4].split(","), )
    return a

def check_automata(a):
    for state in a.I:
        if state not in a.Q:
            print(state + " no està a Q")
            exit(-2)
    print("Tot I està a Q") 
    for state in a.F:
        if state not in a.Q:
            print(state + " no està a Q")
            exit(-2)
    print("Tot F està a Q")

if __name__ == "__main__":
    filename = get_filename()
    read_file(filename)

    a = read_file(filename)
    check_automata(a)    



