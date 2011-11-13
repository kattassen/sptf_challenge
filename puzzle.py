#


class Employee():
    # Class members
    def __init__(self, employee_no):
        self.number = employee_no
        self.team_count = 0
        self.co_worker = []
        self.is_going = False

    def add_co_worker(self, employee_no):
        self.co_worker.append(employee_no)

    def del_co_worker(self, employee_no):
        self.co_worker.remove(employee_no)


def reduce_list(employee_list, check_favorite = False):
    # Sort the list of employees by teamCount
    employee_list = sorted(employee_list,
                          key=lambda empl : empl.team_count,
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
            if check_employee.is_going == 0:
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
        for employee in employee_list:
            if employee.number == co_worker:
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


def retrive_teams():
    # Open file with teams
    team_file = open('./teams', 'r')

    # Declare a list of emplyees
    emplList = []

    first_run = True

    for line in team_file:
        # Skip first row
        if first_run == True:
            first_run = False
            continue

        tempEmployee = line.split()

        empl = 0

        # Loop both team members
        for i in range(0, 2):
            employeeFound = 0

            for empl in emplList:
                if empl.number == tempEmployee[i]:
                    # print "Employee " + tempEmployee[i] + " found"
                    empl.team_count += 1
                    employeeFound = 1
                    if i == 0:
                        empl.add_co_worker(tempEmployee[1])
                    else:
                        empl.add_co_worker(tempEmployee[0])
                    break

            if employeeFound == 0:
                empl = Employee(line.split()[i])
                if i == 0:
                    empl.add_co_worker(tempEmployee[1])
                else:
                    empl.add_co_worker(tempEmployee[0])
                emplList.append(empl)
                #print "Employee " + tempEmployee[i] + " added!"

    return emplList



# Get list of employees
tot_list = retrive_teams()
# Reduce the list to a minimum of travelling employees
default_list = reduce_list(tot_list)

# Get lsit of  employees
tot_list = retrive_teams()
# Reduce the list to a minimum of travelling employees but
# try to let the favorite employee to go as well
favorite_list = reduce_list(tot_list, True)

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
