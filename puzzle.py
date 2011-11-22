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
        self.co_worker_list = []
        self.original_co_worker_list = []
        self.checked = False

    def add_co_worker(self, employee):
        """Method for adding an item to co_worker list"""
        self.co_worker_list.append(employee)
        self.original_co_worker_list.append(employee)

    def del_co_worker(self, employee):
        """Method for removing an item to co_worker list"""
        self.co_worker_list.remove(employee)
        
    def restore_object(self):
        """Method for restoring the object to its initial state"""
        self.co_worker_list = self.original_co_worker_list
        self.checked = False
        
def find(func, list_seq):
    """Dynamic sarch function that returns the first item in list
       where func(item) is True."""
    for list_item in list_seq:
        if func(list_item):
            return list_item

def reduce_list(employee_list, check_favorite = False):
    """Function for reducing the list of all employees to a minimum"""
    
    # Introduce a list for all traveling employees
    traveling_employee_list = []

    # Find a employee that's not has been checked
    if check_favorite == True:
        # If check_favorite is set, set favorite employee to be checked
        check_favorite_employee = find(lambda item: item.number == "1009",
                              employee_list)
        
        if check_favorite_employee != None:
            employee_list.remove(check_favorite_employee)
            employee_list.insert(0,check_favorite_employee)
        
    # Loop all employees in list
    for i in range(0, len(employee_list)):
        if check_favorite == False:
            # Sort the list of employees by teamCount
            employee_list = sorted(employee_list,
                                   key=lambda empl : len(empl.co_worker_list),
                                    reverse=True)
                                    
        check_favorite = False
        
        employee = employee_list[0] 
        # Loop all co workers of the employee found
        if employee.checked == False:
            # Is is_going flag set: put employee to traveling list
            traveling_employee_list.append(employee.number)

            employee_list.remove(employee)
            
            employee.checked = True
            
            for co_worker in employee.co_worker_list:
                # Delete the reference to the employee
                co_worker.del_co_worker(employee)
            
                # Remove the co_worker from employee_list if it has
                # no co_workers left
                if len(co_worker.co_worker_list) == 0:
                    co_worker.checked = True
        else:
            # Otherwise skip this employee
            continue
        
    return traveling_employee_list


def retrieve_teams():
    """Function that reads team members from file and returns them in a list """
    #print "Print the number of teams and the members on team"
    employee_list_total = []

    # Read how many teams that shall be given
    stdin_input = sys.stdin.readline()
    
    try:
        # Test if input was numeric
        no_of_teams = int(stdin_input)
        
        input_rows = []
        
        # Read in all teams from stdin
        for i in range(0, no_of_teams):
            input_rows.append(sys.stdin.readline())
                
    except ValueError:
        print "Error: Input must be numeric. Program will exit!"
        sys.exit()

    for row in input_rows:
        # Split team into two members
        team = row.split()

        # Test if two members are given
        if len(team) != 2:
            print "Error: Two team members must be given: Program will exit!"
            sys.exit()

        temp_empl = [0, 0]
        
        # Loop both team members on row and check if the are in the list
        for i in range(0, 2):
            employee_found = 0
                        
            for temp_empl[i] in employee_list_total:
                if temp_empl[i].number == team[i]:
                    employee_found = 1
                    break
                
            if temp_empl[i] == 0 or employee_found == 0:
                # Employee is not found in list, add it!
                temp_empl[i] = Employee(team[i])
                employee_list_total.append(temp_empl[i])

        i = 0                    
        for i in range(0, 2):
            # Add co_workers to respectivly employee
            if i == 0:
                temp_empl[i].add_co_worker(temp_empl[1])
            else:
                temp_empl[i].add_co_worker(temp_empl[0])
                            
    # Return the list of employees
    return employee_list_total

# Get a list of employee
total_list1 = retrieve_teams()
total_list2 = total_list1[:]

# Reduce the list to a minimum of travelling employees
default_list = reduce_list(total_list1)
print ("-----")
# Restore the list for another run
for item in total_list2:
    item.restore_object()

# Reduce the list to a minimum of travelling employees with 
# considereations to the favorite employee
favorite_list = reduce_list(total_list2, True)

print len(favorite_list)
print len(default_list)
# Print the shortest list
if len(favorite_list) <= len(default_list):
    print len(favorite_list)
    for item in favorite_list:
        print item
else:
    print len(default_list)
    for item in default_list:
        print item
