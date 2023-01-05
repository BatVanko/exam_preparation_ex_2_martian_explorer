# exam_preparation_ex_2_martian_explorer
Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
You will receive a 6x6 field on separate lines with:
•	One rover - marked with the letter "E"
•	Water deposit (one or many) - marked with the letter "W"
•	Metal deposit (one or many) - marked with the letter "M"
•	Concrete deposit (one or many) - marked with the letter "C"
•	Rock (one or many) - marked with the letter "R"
•	Empty positions will be marked with "-"
After that, you will be given the commands for the rover's movement on one line separated by a comma and a space (", "). Commands can be: "up", "down", "left", or "right".
For each command, the rover moves in the given directions with one step, and it can land on one of the given types of deposit or a rock:
•	When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and increase its value by 1.
•	If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown below, and the program ends.
•	If the rover goes out of the field, it should continue from the opposite side in the same direction. Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be placed at position (3, 5).
The rover needs to find at least one of each deposit to consider the area suitable to start our colony. 
Stop the program if you run out of commands or the rover gets broken.

Input
- R - - - -
- - - - - R
- E - R - -
- W - - - -
- - - C - -
M - - - - -
down, right, down, right, down, left, left, left

Output
Water deposit found at (3, 1)
Concrete deposit found at (4, 3)
Metal deposit found at (5, 0)
Area suitable to start the colony.
