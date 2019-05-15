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

    ft_dic = make_ft(plist[2].split(","))

    a = Automata(plist[0].split(","),plist[1].split(","), ft_dic,
                 plist[3].split(","), plist[4].split(","), )
    return a

def make_ft(ft):
    ft_dic = {}
    for transition in ft:        
        if transition[0] in ft_dic:
            ft_dic[transition[0]].append({transition[1]: transition[2]})
        else:
            ft_dic[transition[0]] = [{transition[1]: transition[2]}]
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
    print("Insereix una paraula que vulguis provar amb l'AF definit a " + filename)
    print("Fes \"quit\" per marxar")

    while quit != 1:
        line = sys.stdin.readline()
        line = line.rstrip("\n")
        if line == "quit" or line == "quit\n":
            quit = 1
        elif line != "\n" and line != '':
            print (a.ft)
            check_word(line, a)
            

def check_word(line, a):
    if(not check_alph(line, a)):
        print("Paraula no acceptada, lletra no pertany a l'alfabet")
        exit(-3)
    if not reach_end(line, a):
        print("Paraula no acceptada per l'autòmat.")
        exit(-3)
    print("Praula " + line + " acceptada per l'autòmat.")
    exit(1)

def reach_end(word, a):
    return call_reach_end(a.I,word,a)

def  call_reach_end(states, word, a):
    if not word and states in a.F:
        return True
    else:
        for state in states:
            print(state)
            print(word)
            for way in a.ft[state]:
                if word and word[0] in way:
                    return call_reach_end(way[word[0]],word[1:], a)
        return False

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
    


