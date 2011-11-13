""" puzzle.py """


class Employee():
    """ Employee class """
    def __init__(self, employee_no):
        self.number = employee_no
        self.co_worker = []
        self.is_going = False

    def add_co_worker(self, employee_no):
        self.co_worker.append(employee_no)

    def del_co_worker(self, employee_no):
        self.co_worker.remove(employee_no)

def find(func, list_seq):
    """Dynamic sarch function that returns the first item in list
       where func(item) is True."""
    for list_item in list_seq:
        if func(list_item):
            return list_item

def reduce_list(employee_list, check_favorite = False):
    """Fucntion for reducing the list of all employee to a minimum"""
    # Sort the list of employees by teamCount
    employee_list = sorted(employee_list,
                          key=lambda empl : len(empl.co_worker),
                          reverse=True)

    # Set all_checked flag to true
    employee_found = False

    # Find a employee that's not has been checked
    if check_favorite == True:
        # If check_favorite is set, set favorite employee
        # to be checked.
        for check_employee in employee_list:
            if check_employee.number == "1009":
                employee_found = True
                break
    else:
        # Find employee with greatest team count that
        # has not been checked.
        for check_employee in employee_list:
            if check_employee.is_going == False:
                # Set all_checked flag to False to indicate that
                # we found
                employee_found = True
                break

    # If no employee is found return list. We are finished!
    if (employee_found == False):
        return employee_list

    # Loop all co workers of the employee found
    for co_worker in check_employee.co_worker:
        # Find the co worker in the list of employees
        employee = find(lambda item: item.number == co_worker, employee_list)

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
    # Open file with teams
    team_file = open('./teams', 'r')

    # Declare a list of emplyees
    empl_file_list = []

    first_run = True

    for line in team_file:
        # Skip first row (amount of teams)
        if first_run == True:
            first_run = False
            continue

        employee_row = line.split()

        empl = 0

        # Loop both team members on row
        for i in range(0, 2):
            employee_found = False

            for empl in empl_file_list:
                if empl.number == employee_row[i]:
                    # print "Employee " + employee_row[i] + " found"
                    employee_found = True
                    # Add the coworker to employees coworker list
                    if i == 0:
                        empl.add_co_worker(employee_row[1])
                    else:
                        empl.add_co_worker(employee_row[0])
                    break

            if employee_found == False:
                # Employee is not found in list, add it!
                empl = Employee(line.split()[i])
                # Add the coworker to employees coworker list
                if i == 0:
                    empl.add_co_worker(employee_row[1])
                else:
                    empl.add_co_worker(employee_row[0])
                empl_file_list.append(empl)
                #print "Employee " + employee_row[i] + " added!"
    # Return the list of employees
    return empl_file_list



# Get list of employees and reduce the list to
# a minimum of travelling employees
default_list = reduce_list(retrieve_teams())

# Get a list of employees and reduce the list to
# a minimum of travelling employees but with special
# consideration to a favorite employe
favorite_list = reduce_list(retrieve_teams(), True)

# Check if the list with the favorite is shorter (or equal) than
# the list with the optimal amount of employees.
# Print the shortest list
if len(favorite_list) <= len(default_list):
    print len(favorite_list)
    for item in favorite_list:
        print item.number
else:
    print len(default_list)
    for item in default_list:
        print item.number
