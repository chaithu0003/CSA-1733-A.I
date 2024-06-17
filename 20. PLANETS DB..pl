% Facts about planets and their date of discovery
planet(mercury, 1631).
planet(venus, 1610).
planet(earth, unknown). % Earth's discovery date is not well-defined
planet(mars, 1610).
planet(jupiter, 1610).
planet(saturn, 1610).
planet(uranus, 1781).
planet(neptune, 1846).
planet(pluto, 1930). % Pluto is considered a dwarf planet

% Queries to retrieve the date of discovery of planets
discovery_date(Planet, Date) :-
    planet(Planet, Date).

% Example queries:
% ?- discovery_date(mercury, Date).
% ?- discovery_date(earth, Date).
% ?- discovery_date(pluto, Date).
