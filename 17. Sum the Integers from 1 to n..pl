sum(1, 1).
sum(N, Total) :-
    N > 1,
    N1 is N - 1,
    sum(N1, Rem),
    Total is N + Rem.