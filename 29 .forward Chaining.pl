rainy(chennai).
rainy(coimbatore).
rainy(ooty).
cold(ooty).
snowy(X) :- rainy(X), cold(X).
forward_chaining :-
    (   snowy(X)
    ->  format('~w is snowy.~n', [X])
    ;   write('No snowy locations inferred.'), nl).
start :-
    forward_chaining.