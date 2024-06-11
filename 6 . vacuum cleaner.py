class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment
        self.position = (0, 0)  # Starting position of the vacuum cleaner

    def clean(self):
        while True:
            current_cell = self.environment[self.position[0]][self.position[1]]
            if current_cell == 'D':
                print(f"Cleaning dirt at position {self.position}")
                self.environment[self.position[0]][self.position[1]] = '-'  # Mark the cell as clean
            self.move()

    def move(self):
        rows, cols = len(self.environment), len(self.environment[0])
        if self.position[1] < cols - 1:  # Move right if possible
            self.position = (self.position[0], self.position[1] + 1)
        elif self.position[0] < rows - 1:  # Move down if possible
            self.position = (self.position[0] + 1, self.position[1])
        elif self.position[1] > 0:  # Move left if possible
            self.position = (self.position[0], self.position[1] - 1)
        else:  # Move up if possible
            self.position = (self.position[0] - 1, self.position[1])

# Example environment (5x5 grid with some dirt cells)
environment = [
    ['-', '-', '-', '-', '-'],
    ['-', 'D', '-', 'D', '-'],
    ['D', '-', 'D', '-', '-'],
    ['-', 'D', '-', '-', 'D'],
    ['-', '-', '-', 'D', '-']
]

# Create a vacuum cleaner agent and start cleaning
vacuum_cleaner = VacuumCleaner(environment)
vacuum_cleaner.clean()
