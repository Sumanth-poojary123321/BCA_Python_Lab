# Define a class named Employee
class Employee:

    # Constructor method (runs automatically when object is created)
    def __init__(self):
        self.empno = input("Emp no: ")          # Input employee number
        self.name = input("Name: ")             # Input employee name
        self.depname = input("Dept. Name: ")    # Input department name
        self.designation = input("Designation: ") # Input job designation
        self.age = int(input("Age: "))          # Input age and convert to integer
        self.salary = int(input("Salary: "))    # Input salary and convert to integer

    # Method to search employee using employee number
    def Search(self, eid):
        return self.empno == eid   # Return True if employee number matches

    # Method to display employee details
    def display(self):
        # Print employee details with tab spacing
        print(self.empno, "\t", self.name, "\t", self.depname, "\t",
              self.designation, "\t", self.age, "\t", self.salary)


# Create an empty list to store employee objects
lst = []

# Start an infinite loop for the menu
while True:

    # Display menu options
    print("\n1. Add \n2. Search \n3. Display \n4. Exit")
    print("----------")   # Print separator line

    # Take user's choice
    ch = input("Your choice: ")

    # If user chooses option 1 (Add employee)
    if ch == "1":

        # Ask how many employees to add
        n = int(input("Enter total number of employees: "))

        # Print message
        print(f"Enter the details of {n} Employees")

        # Print a line separator
        print("-" * 45)

        # Loop to add n employees
        for i in range(n):
            e1 = Employee()   # Create Employee object (constructor runs)
            lst.append(e1)    # Add employee object to list
            print("-" * 45)   # Print separator after each employee

    # If user chooses option 2 (Search employee)
    elif ch == "2":

        # Ask employee number to search
        eid = input("Enter Employee No: ")

        # Variable to check if employee is found
        isFound = False

        # Loop through employee list
        for e in lst:

            # Check if employee number matches
            if e.Search(eid):
                e.display()       # Display employee details
                isFound = True    # Mark as found
                break             # Stop loop

        # If employee not found
        if not isFound:
            print("\nEmployee not found\n")

    # If user chooses option 3 (Display all employees)
    elif ch == "3":

        # Print separator
        print("-" * 45)

        # Print heading
        print("---------List of Employees-------------")

        # Loop through all employees
        for e in lst:
            e.display()   # Display each employee's details

    # If user chooses option 4 (Exit program)
    elif ch == "4":
        print("\nExiting............")  # Print exit message
        break   # Stop the loop and end program

    # If user enters an invalid choice
    else:
        print("\nWrong Choice!")  # Display error message