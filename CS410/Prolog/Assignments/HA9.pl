max([M], M).
max([H|L], H) :- max(L, C), H >= C.
max([H|L], M) :- max(L, M), H =< M.
min([M], M).
min([H|L], H) :- max(L, C), H =< C.
min([H|L], M) :- max(L, M), H >= M.
dia(L, D) :- max(L, A), min(L, I), D is A - I.

poly([], _, _, _).
poly([H|L], X, S, A) :- NS is S - (H*(X**A)), poly(L, X, NS, A+1).
poly(L, X, S) :- poly(L, X, S, 0).
