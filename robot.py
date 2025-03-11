class Robot:
    def __init__(self):
        # Initialize the robot's starting position and direction
        self.x = 0
        self.y = 0
        self.direction = "NORTH"  # Default direction is NORTH

    def move(self):
        """Move the robot one step in the current direction."""
        if self.direction == "NORTH":
            self.y += 1
        elif self.direction == "SOUTH":
            self.y -= 1
        elif self.direction == "EAST":
            self.x += 1
        elif self.direction == "WEST":
            self.x -= 1

    def turn_left(self):
        """Turn the robot 90 degrees to the left."""
        if self.direction == "NORTH":
            self.direction = "WEST"
        elif self.direction == "WEST":
            self.direction = "SOUTH"
        elif self.direction == "SOUTH":
            self.direction = "EAST"
        elif self.direction == "EAST":
            self.direction = "NORTH"

    def turn_right(self):
        """Turn the robot 90 degrees to the right."""
        if self.direction == "NORTH":
            self.direction = "EAST"
        elif self.direction == "EAST":
            self.direction = "SOUTH"
        elif self.direction == "SOUTH":
            self.direction = "WEST"
        elif self.direction == "WEST":
            self.direction = "NORTH"

    def report(self):
        """Report the robot's current position and direction."""
        return f"Position: ({self.x}, {self.y}), Direction: {self.direction}"

    def execute_commands(self, commands):
        """
        Execute a sequence of commands.
        Commands can be 'M' (move), 'L' (turn left), or 'R' (turn right).
        """
        for command in commands:
            if command == "M":
                self.move()
            elif command == "L":
                self.turn_left()
            elif command == "R":
                self.turn_right()
            else:
                print(f"Invalid command: {command}")
        print(self.report())


# Example usage
if __name__ == "__main__":
    # Create a robot instance
    robot = Robot()

    # Provide a sequence of commands (e.g., "MMRMLM")
    print("Enter a sequence of commands (M: Move, L: Turn Left, R: Turn Right):")
    user_input = input().strip().upper()

    # Execute the commands
    robot.execute_commands(user_input)