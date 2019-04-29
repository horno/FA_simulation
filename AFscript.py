# coding=utf-8
# encoding: utf-8
#!/usr/bin/env python3
import sys
import os

stop = False

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

    ft_dic = make_ft(plist[2].split(","), plist[0].split(","))

    a = Automata(plist[0].split(","),plist[1].split(","), ft_dic,
                 plist[3].split(","), plist[4].split(","), )
    return a

def make_ft(ft, Q):
    ft_dic = {}        
    
    for state in Q:
        ft_dic[state] = []

    for transition in ft:        
        ft_dic[transition[0]].append((transition[1], transition[2]))
    
    return ft_dic

def check_automata(a):
    for state in a.I:
        if state not in a.Q:
            print(state + " no està a Q")
            exit(-2)
    for state in a.F:
        if state not in a.Q:
            print(state + " no està a Q")
            exit(-2)

def service_loop(a):
    quit = 0
    print("> Insereix una paraula que vulguis provar amb l'AF definit a " + filename)
    print("> Fes \"quit\" per marxar")

    while quit != 1:
        line = sys.stdin.readline()
        line = line.rstrip("\n")
        if line == "quit" or line == "quit\n":
            quit = 1
        elif line != "\n" and line != '':
            check_word(line, a)

def check_word(line, a):
    if(not check_alph(line, a)):
        print("> Praula \"" + line + "\" no acceptada, lletra no pertany a l'alfabet.")
        # exit(0)
    elif not reach_end(line, a):
        print("> Praula \"" + line + "\" no acceptada per l'autòmat. :(")
        # exit(0)
    else: 
        print("> Praula \"" + line + "\" acceptada per l'autòmat. :)")
        # exit(0)
    print("> Introdueix una nova paraula o fes \"quit\" per marxar. ")
    global stop 
    stop = False

def reach_end(word, a): #TODO: Aquí aniran tots els estats inicials
    for init_state in a.I:
        if reach_end_rec(init_state, word, a):
            return True
    return False

def reach_end_rec(state, word, a):
    global stop
    if word == "":
        if state in a.F:
            print("> Estat final: " + state)
            stop = True
            return True
    elif not stop:
        found = False
        for direc in a.ft[state]:
            if direc[0] == word[0] and not stop:
                print("("+state+","+word+")-->"+direc[1])
                if reach_end_rec(direc[1], word[1:], a):
                    found = True
        if found:
            return True

def check_alph(word, a):
    for letter in word:
        if letter not in a.E:
            return False
    return True
        
if __name__ == "__main__":
    filename = get_filename()
    a = read_file(filename)
    check_automata(a)
    service_loop(a)


