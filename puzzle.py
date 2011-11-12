#


class Employee():
    # Class members
    def __init__(self, employee_no):
        self.number = employee_no
        self.team_count = 0
        self.co_worker = []
        self.isGoing = 0

    def addCoWorker(self, employee_no):
        self.co_worker.append(employee_no)


def reduceList(employeeList, check_favorite = False):
    # Sort the list by teamCount
    employeeList = sorted(employeeList, 
                          key=lambda empl : empl.team_count, 
                          reverse=True)

    all_checked = True
    
    # Find a employee that's not has been checked
    if check_favorite == True:
        print "check_favorite"
        for employee1 in employeeList:
            if employee1.number == "1009":
                all_checked = False
                break
    else:
        for employee1 in employeeList:
            if employee1.isGoing == 0:
                all_checked = False
                break

    if (all_checked == True):
        return employeeList

    print employee1.number
    # Loop all coworkers in of the last employee in list
    for coWorker in employee1.co_worker:

        # Find the coWorker
        for employee in employeeList:
            if employee.number == coWorker:
                # Remove this coworker if it does not
                # belong to any more team
                if len(employee.co_worker) == 1:
                    employeeList.remove(employee)

    # Mark this employee to be finished
    employee1.isGoing = 1
    
    # Call this function again recursivly
    return reduceList(employeeList)



# Open file with teams
teamFile = open('./teams', 'r')

# Declare a list of emplyees
emplList = []

firstRun = 1

for line in teamFile:
    # Skip first row
    if firstRun == 1:
        firstRun = 0
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
                    empl.addCoWorker(tempEmployee[1])
                else:
                    empl.addCoWorker(tempEmployee[0])
                break

        if employeeFound == 0:
            empl = Employee(line.split()[i])
            if i == 0:
                empl.addCoWorker(tempEmployee[1])
            else:
                empl.addCoWorker(tempEmployee[0])
            emplList.append(empl)
            #print "Employee " + tempEmployee[i] + " added!"



emplList1 = reduceList(emplList)

print len(emplList1)
for item in emplList1:
    print item.number
print "-------------------"

emplList2 = reduceList(emplList, True)

print len(emplList2)
for item in emplList:
    print item.number


