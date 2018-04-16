aunt(A,X) :- sister(A,B), parent(B,X).

parent(P,C) :- father(P,C).
parent(P,C) :- mother(P,C).

cousin(C,S) :- parent(F,C), sibling(F,B), parent(B,S).

sibling(C,S) :- brother(C,S).
sibling(C,S) :- sister(C,S).

father(jim,linda).
father(jim,harry).
father(john,bill).
father(john,will).
father(frank,tom).
father(frank,gary).
father(frank,mary).

mother(beth,linda).
mother(beth,harry).
mother(janice,bill).
mother(janice,will).
mother(liz,tom).
mother(liz,gary).
mother(liz,mary).

sister(linda,harry).
sister(mary,tom).
sister(mary,gary).
sister(beth,john).
sister(beth,frank).

brother(harry,linda).
brother(bill,will).
brother(will,bill).
brother(tom,gary).
brother(gary,tom).
brother(tom,mary).
brother(gary,mary).
brother(john,beth).
brother(john,frank).
brother(frank,john).
brother(frank,beth).
