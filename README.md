This Python script allows users to manage daily temperature data for the week using a dictionary. It provides a menu for inserting, displaying, or exiting data.

Code Breakdown:
Setup:

my_dict = {} stores temperature data (day: temperature).
days_of_week = ["Monday", "Tuesday", ..., "Sunday"] validates user input for days.
A welcome message greets the user.
Main Loop:

A while True loop displays a menu with options to:
Insert data (temperature for a day).
Display stored temperatures.
Exit.
Option 1 - Insert Data:

Prompts the user to enter a valid day and temperature, then stores it in my_dict.
Displays an error if the day is invalid.
Option 2 - Display Data:

Checks if my_dict contains any data, and displays stored temperatures.
If empty, informs the user.
Option 3 - Exit:

Exits the loop and prints a message.
Error Handling:

If the user selects an invalid option, the program notifies them.
Program Flow:
The loop continues until the user selects "Exit" (option 3).
The user can continuously insert and view data interactively.
Example:
mathematica
Copy code
Welcome!
1. Insert Data
2. Display Data
3. Exit
Enter your choice: 1
Enter day: Monday
Enter temperature: 25
...
This simple program effectively manages weekly temperature data with easy-to-use options and input validation.







