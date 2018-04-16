/* Write a predicate binDec(L, N), where L is a list of zeroes and ones, 
 * and N is a natural number. The predicate is true if N is the decimal 
 * representation of the sequence of binary digits in L.
 * 
 * For example, the following queries should succeed:
 * 
 * binDec( [ s(0), 0, s(0) ], s(s(s(s(s(0))))) ) (because 0b101 = 5)
 * binDec( [ 0, s(0), s(0) ], s(s(s(0))))) ) (because 0b011 = 3)
 */

down([], X, X).
down([_|L], s(X), R) :- down(L, X, R).
binDec([], s(0)).
binDec([s(_)|L], X) :- down(L, X, R1), down(L, R1, R2), binDec(L, R2).
binDec([_|L], X) :- binDec(L, X).

%----------------------------------------------------------------
/* Write a predicate rotLeft(L1, N, L2), where L1 and L2 are lists, 
 * and N is a natural number. The predicate is true if L2 is the list 
 * obtained by rotating L1 left by N steps.
 * 
 * For example, the following queries should succeed:
 * 
 * rotLeft( [a, b, c, d, e, f, g], s(s(0)), [c, d, e, f, g, a, b] )
 * rotLeft( [1, a, 2, b], 0, [1, a, 2, b] )
 * rotLeft( [1, 2], s(s(s(s(s(0))))), [2, 1] )
 */

% Binds arg2 to the leftshift x1 of arg1
lshift([H|L], R) :- append(L, [H], R).

% Binds arg3 to arg1, leftshifted N times
rotLeft(L, 0, L).
rotLeft(L1, s(N), L2) :- lshift(L1, R), rotLeft(R, N, L2).

%----------------------------------------------------------------
/* Write a predicate repeat(L1, N, L2), where L1 and L2 are lists, 
 * and N is a natural number. The predicate is true if L2 is the list
 * obtained by repeating each element of L1, N times.
 * 
 * For example, the following queries should succeed:
 * repeat( [a, b, c], s(s(0)), [a, a, b, b, c, c] )
 * repeat( [1, a, 2, b], 0, [ ] )
 * repeat( [1, 1, 2], s(s(s(0))), [1, 1, 1, 1, 1, 1, 2, 2, 2] )
 */

% Binds Arg3 to the value of Arg1, repeated until unary Arg2 reaches 0
% In terms for mortals, Repeats Arg1, Arg2 times
rpt(_, 0, []).
rpt(E, s(N), L) :- rpt(E, N, NL), append([E], NL, L).

% Recurses through the list, repeating the head element N times for each one
repeat([], _, []).
repeat([H|L], N, O) :- rpt(H, N, RL), repeat(L, N, NO), append(RL, NO, O).
