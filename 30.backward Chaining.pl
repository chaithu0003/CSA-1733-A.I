% Facts
parent(ravi, lakshmi).
parent(ravi, sai).
parent(lakshmi, anita).
parent(lakshmi, prasad).
parent(prasad, vamsi).

% Rules
ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

% Backward chaining predicate to find relationships
query_relationship(X, Y) :-
    ancestor(X, Y),
    format('~w is an ancestor of ~w.~n', [X, Y]).