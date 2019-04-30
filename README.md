# Simulador d'automats finits
FA_simulator és un programa escrit en python 3 que, donat
un autòmat finit (no cal que sigui determinista), és capaç
de determinar si les paraules introduides per consola són
acceptades pel autòmat.

## Introduir autòmat
L'autòmat s'introduirà en un fitxer de text amb el nom 
desitjat. En el cas de l'exemple, el fitxer es diu 
input.txt.
Aquest fitxer ha de contenir 5 línies, en la primera hi
haurà el nom dels estats separats per comes. El nom de 
cada estat ha de ser d'un símbol, per exemple, A,B,C seria
un conjunt d'estats acceptats, no com q1,q2,q3.
En segon lloc s'han d'indicar les lletres
de l'alfabet separades per una coma.
En la tercera línia s'indicarà cada estat, a quin altre
estat anirà, i amb quina lletra. Per exemple, si
l'estat A va al B amb el símbol 1, i l'estat B va a 
l'A amb el símbol 2, la línia resultant seria: 
A1B,B2A.
La quarta línia es tracta del conjunt d'estats inicials, 
separats per una coma. De la mateixa forma és la cinquena
línia, però amb els estats finals.

## Ús
Una vegada idicat l'autòmat. S'executa l'scrpit de python 
AFscript.py amb 1 paràmetre, el nom del fitxer on hi ha
indicat l'autòmat. Per exemple, per utilitzar el programa
amb l'exemple enviat, la comanda seria:
python AFscript.py input.txt
Una vegada executat, introduir les paraules que es vulguin
comprobar o fer "quit" per sortir.

## Exemple enviat
Entre els fitxers envits, hi ha un autòmat d'exemple a 
input.txt. Es tracta d'un autòmat que accepta qualsevol
paraula formada per 1 i 0 que compleixi la condició de 
tenir un 1 en la penúltima posició. Si es vol provar 
aquest exemple, com s'ha dit anteriorment, executar
la comanda: 
python AFscript.py input.txt


Autors: Ian Palacín Aliana i Joaquim Picó Mora
