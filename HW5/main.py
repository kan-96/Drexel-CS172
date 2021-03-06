from employee import Employee
from linkedList import Linkedlist

if __name__ == "__main__":
    menu = ("\na. Add New Employee"
            "\nb. Enter Employee Hours"
            "\nc. Update Employee Hourly Rate"
            "\nd. Display Payroll"
            "\ne. Remove Employee from Payroll"
            "\nf. Exit the program"
            "\nEnter your choice: ")
    # create new linked list
    myLinkedList = Linkedlist()
    print("*** CS 172 Payroll Simulator ***")
    user_choice = input(menu)
    while user_choice != 'f':
        if (user_choice == 'a'):
            name = input("Enter the new employee name: ")
            rate = input("\nEnter their hourly rate: ")
            employee = Employee(name,rate)
            myLinkedList.append(employee)
            print("Employee " + str(employee.getEID()) + " added to payroll")

        elif (user_choice == 'b'):
            for i in range(0, len(myLinkedList)):
                new_hour = input('\nEnter hours worked for employee ' + str(myLinkedList[i].getEID()) + ":")
                myLinkedList[i].setHours(new_hour)

        elif (user_choice == 'c'):
            id_num = input("Enter employee ID: ")
            if myLinkedList.search(id_num):
                new_rate = input("Enter new wage for employee " + str(id_num) + " :")
                myLinkedList[int(id_num)-1].setRate(new_rate)
            else:
                print("Employee doesn't exist.")
        elif (user_choice == 'd'):
            print("*** Payroll***")
            if not myLinkedList.isEmpty():
                print(myLinkedList)
        elif (user_choice == 'e'):
            id_num = input("Enter employee ID: ")
            if myLinkedList.search(id_num):
                myLinkedList.remove(id_num)
            else:
                print("Employee doesn't exist.")
        else:
            print("Invalid entry.")

        user_choice = input(menu)
    print("Goodbye.")
