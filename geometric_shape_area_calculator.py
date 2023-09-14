#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14

    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    print("Welcome to the geometric shape area calculator!")
    # User Options
    Circle = 1
    Rectangle = 2
    Triangle = 3
    
    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
    print(f'Circle = {Circle} Rectangle = {Rectangle} Triangle = {Triangle}' )

    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = input("Select a shape by entering 1, 2, or 3 ")
    # TODO: Convert the variable 'choice' to an integer data type.
    choice = int(choice)
    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
    print(type (choice) == int)
    if choice == 1:  #DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle

        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        radius = input("What is the radius of the circle? ")
        # TODO: Convert 'radius' to float.
        radius = float(radius)
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        area = circle_pi * (radius ** 2)
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        length = input("What is the length? ")
        width = input("What is the width? ")
        # TODO: Convert both 'length' and 'width' to float.
        length = int(length)
        width = int(width)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        area = length * width
        # HINT: The formula to find the area of a rectangle: length times width

    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        base = input("What is the base length? ")
        height = input("What is the height? ")
        # TODO: Convert both 'base' and 'height' to float.
        base = float(base)
        height = float(height)
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        area = base * height / 2
        # HINT: The formula to find the area of a Triangle: half times base times height

    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice ."
        print("Invalid choice .")
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific. 
    step_1 = "log on to canvas, choose courses, then techpathways '23, then assignments, then choose the correct assignement, then start assignment"
    step_2 = "accept the assignment"
    step_3 = "go on github and click on code in green box to copy the link"
    step_4 = "create a folder and drag the folder onto vsc to open the folder"
    step_5 = "in terminal type 'git clone ' and paste in the copied link" 
    step_6 = "in terminal type 'git init' to initialize"
    step_7 = "in terminal type 'cd ' and the folder name and press enter to go inside the assignment folder"
    step_8 = "finish the assignment"
    step_9 = "in terminal type 'git add .', then 'git commit -m ' and type a message saying you finished your assignement, then 'git push' to push to github"
    print(f'Step 1: {step_1} \nStep 2: {step_2} \nStep 3: {step_3} \nStep 4: {step_4} \nStep 5: {step_5} \nStep 6: {step_6} \nStep 7: {step_7} \nStep 8: {step_8} \nStep 9: {step_9} \n')


if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY



