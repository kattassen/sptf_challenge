#
# Author: Simon Furborg
# Date:   2011-11-13
#
#
# -bilateral puzzle-
# Program asks for amount of teams and team members. The program
# then calculates the least member possible for representing all
# teams on a company conference. If possible the employee with
# number 1009 shall be included in the list of traveling members.
# Output shows the amount of members and their numbers.
#
# The input shall be given on the following form (example 3 teams):
#    3
#    1001 2001
#    1009 2002
#    1010 2001
#
# Output:
#    2
#    2001
#    1009
#

import sys
from copy import deepcopy

class Employee():
    """Employee class """
    def __init__(self, employee_no):
        self.number = employee_no
        self.co_worker = []
        self.is_going = False

    def add_co_worker(self, employee_no):
        """Method for adding an item to co_worker list"""
        self.co_worker.append(employee_no)

    def del_co_worker(self, employee_no):
        """Method for removing an item to co_worker list"""
        self.co_worker.remove(employee_no)

def find(func, list_seq):
    """Dynamic sarch function that returns the first item in list
       where func(item) is True."""
    for list_item in list_seq:
        if func(list_item):
            return list_item

def reduce_list(employee_list, check_favorite = False):
    """Function for reducing the list of all employees to a minimum"""
    # Sort the list of employees by teamCount
    employee_list = sorted(employee_list,
                          key=lambda empl : len(empl.co_worker),
                          reverse=True)

    # Find a employee that's not has been checked
    if check_favorite == True:
        # If check_favorite is set, set favorite employee to be checked
        check_employee = find(lambda item: item.number == "1009",
                              employee_list)
    else:
        # Find employee with greatest team count that has not been checked
        check_employee = find(lambda item: item.is_going == False,
                              employee_list)

    # If no employee is found return list. We are finished!
    if (check_employee == None):
        return employee_list

    # Loop all co workers of the employee found
    for co_worker in check_employee.co_worker:
        # Find the co worker in the list of employees
        employee = find(lambda item: item.number == co_worker, employee_list)

        if employee == None:
            continue

        # Remove the reference to the checked employee
        # from the co-worker list
        for co_worker2 in employee.co_worker:
            if (co_worker2 == check_employee.number):
                employee.del_co_worker(co_worker2)
        # Remove this co-worker if it does not
        # belong to any more team
        if len(employee.co_worker) == 0:
            employee_list.remove(employee)

    # Mark this employee to be finished
    check_employee.is_going = True

    # Call this function again recursivly
    return reduce_list(employee_list)


def retrieve_teams():
    """Function that reads team members from file and returns them in a list """
    print "Print the number of teams and the members on team"

    employee_list_total = []

    # Read how many teams that shall be given
    stdin_input = sys.stdin.readline()

    # Test if input was numeric
    try:
        no_of_teams = int(stdin_input)
    except ValueError:
        print "Error: Input must be numeric. Program will exit!"
        sys.exit()

    for i in range(0, no_of_teams):
        # Read a line from standard in
        team_row = sys.stdin.readline()
        # Split team into two members
        team = team_row.split()

        # Test if two members are given
        if len(team) != 2:
            print "Error: Two team members must be given: Program will exit!"
            sys.exit()

        temp_empl = 0

        # Loop both team members on row
        for i in range(0, 2):
            employee_found = False

            for temp_empl in employee_list_total:
                if temp_empl.number == team[i]:
                    employee_found = True
                    # Add the coworker to employee coworker list
                    if i == 0:
                        temp_empl.add_co_worker(team[1])
                    else:
                        temp_empl.add_co_worker(team[0])
                    break

            if employee_found == False:
                # Employee is not found in list, add it!
                temp_empl = Employee(team[i])
                # Add the coworker to employee coworker list
                if i == 0:
                    temp_empl.add_co_worker(team[1])
                else:
                    temp_empl.add_co_worker(team[0])
                employee_list_total.append(temp_empl)
    # Return the list of employees
    return employee_list_total


# Get list of employees and reduce the list to
total_list1 = retrieve_teams()
total_list2 = deepcopy(total_list1)

# a minimum of travelling employees
default_list = reduce_list(total_list1)

# Get a list of employees and reduce the list to
# a minimum of travelling employees but with special
# consideration to a favorite employe
favorite_list = reduce_list(total_list2, True)

# Print the shortest list
if len(favorite_list) <= len(default_list):
    print len(favorite_list)
    for item in favorite_list:
        print item.number
else:
    print len(default_list)
    for item in default_list:
        print item.number
