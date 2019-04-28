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

    make_ft(plist[2].split(","))

    a = Automata(plist[0].split(","),plist[1].split(","), plist[2].split(",") ,
                 plist[3].split(","), plist[4].split(","), )
    return a

def make_ft(ft):
    ft_dic = {}
    for transition in ft:
        
        if transition[0] in ft_dic:
            ft_dic[transition[0]] = {transition[1]: ft_dic[transition[0]][transition[1]] + transition[2]}
        else:
            ft_dic[transition[0]] = {transition[1]: transition[2]}


        # print(ft_dic[transition[0]][transition[1]])

    print(ft_dic)

def check_automata(a):
    for state in a.I:
        if state not in a.Q:
            print(state + " no està a Q")
            exit(-2)
    for state in a.F:
        if state not in a.Q:
            print(state + " no està a Q")
            exit(-2)

if __name__ == "__main__":
    filename = get_filename()
    a = read_file(filename)
    check_automata(a)    


