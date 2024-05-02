

import tkinter as tk
import pickle

class EventManagementSystem():

    def __init__(self,name,owner):
        self.name = name
        self.owner = owner
        self.employees = []
        self.events = []
        self.clients = []
        self.guests = []
        self.cateringCompanies = []
        self.decorationsCompanies = []
        self.cleaningCompanies = []
        self.furnitureSupplyCompanies = []

    def add_employee(self,employee_type,name,employee_id,department,basic_salary,age,dob,passport,manager_id):

        if employee_type == "Sales Managers":
            employee = SalesManager(name,employee_id,department,"Sales Manager",basic_salary,age,dob,passport)
            print("Sales Manager Successfully Added")

        elif employee_type == "Salespersons":
            employee = Salesperson(name,employee_id,department,"Salesperson",basic_salary,age,dob,passport,manager_id)
            print("Salesperson Successfully Added")

        elif employee_type == "Marketing Managers":
            employee = MarketingManager(name,employee_id,department,"Salesperson",basic_salary,age,dob,passport)
            print("Marketing Manager Successfully Added")

        elif employee_type == "Marketers":
            employee = Marketer(name,employee_id,department,"Salesperson",basic_salary,age,dob,passport)
            print("Marketer Successfully Added")

        elif employee_type == "Accountants":
            employee = Accountant(name,employee_id,department,"Salesperson",basic_salary,age,dob,passport)
            print("Accountant Successfully Added")

        elif employee_type == "Designers":
            employee = Designer(name,employee_id,department,"Salesperson",basic_salary,age,dob,passport)
            print("Designer Successfully Added")

        elif employee_type == "Handymen":
            employee = Handyman(name,employee_id,department,"Salesperson",basic_salary,age,dob,passport)
            print("Handymen Successfully Added")

        self.employees.append(employee)

        employee_file = open("employees.pkl",'wb')
        pickle.dump(self.employees,employee_file)
        employee_file.close()


    def add_event(self,eventID,eventType,theme,date,time,duration,venueAddress,clientID,invoice):

        if eventType == "Wedding":
            event = Wedding(eventID,eventType,theme,date,time,duration,venueAddress,clientID,invoice)
        elif eventType == "Birthday":
            event = Birthday(eventID,eventType,theme,date,time,duration,venueAddress,clientID,invoice)
        elif eventType == "ThemedParty":
            event = ThemedParty(eventID,eventType,theme,date,time,duration,venueAddress,clientID,invoice)
        elif eventType == "Graduation":
            event = Graduation(eventID,eventType,theme,date,time,duration,venueAddress,clientID,invoice)

        print("Event successfully added.")
        self.events.append(event)

        event_file = open("events.pkl", 'wb')
        pickle.dump(self.events, event_file)
        event_file.close()

    def add_client(self,clientID,name,address,contactDetails,budget):
        client = Client(clientID,name,address,contactDetails,budget)
        print("Client Successfully Added.")
        self.clients.append(client)

        client_file = open("clients.pkl", 'wb')
        pickle.dump(self.clients, client_file)
        client_file.close()

    def add_guest(self,guestID,name,address,contactDetails):
        guest = Guest(guestID,name,address,contactDetails)
        print("Guest Successfully Added.")
        self.guests.append(guest)

        guest_file = open("guests.pkl", 'wb')
        pickle.dump(self.guests, guest_file)
        guest_file.close()

    def add_supplier(self,supplier_type,name,address,contact):
        if supplier_type == "catering":
            supplier = CateringSupplier(name,address,contact)
            self.cateringCompanies.append(supplier)
        elif supplier_type =="decorations":
            supplier = DecorationsSupplier(name,address,contact)
            self.decorationsCompanies.append(supplier)
        elif supplier_type == "cleaning":
            supplier = CleaningSupplier(name,address,contact)
            self.cleaningCompanies.append(supplier)
        elif supplier_type == "furniture":
            supplier = FurnitureSupplier(name,address,contact)
            self.furnitureSupplyCompanies.append(supplier)

        print("Supplier Successfully Added.")

        supplier_file = open("suppliers.pkl", 'wb')
        pickle.dump(self.getSuppliers(), supplier_file)
        supplier_file.close()

    def getName(self):
        return self.name

    def getOwner(self):
        return self.owner

    def getEmployees(self):
        return self.employees

    def getEvents(self):
        return self.events

    def getClients(self):
        return self.clients

    def getGuests(self):
        return self.guests

    def getCateringCompanies(self):
        return self.cateringCompanies

    def getDecorationsCompanies(self):
        return self.decorationsCompanies

    def getCleaningCompanies(self):
        return self.cleaningCompanies

    def getFurnitureSupplyCompanies(self):
        return self.furnitureSupplyCompanies

    def getSuppliers(self):
        suppliers = []

        for i in self.getCateringCompanies():
            suppliers.append(i)

        for i in self.getCleaningCompanies():
            suppliers.append(i)

        for i in self.getDecorationsCompanies():
            suppliers.append(i)

        for i in self.getFurnitureSupplyCompanies():
            suppliers.append(i)

        return suppliers

    def getEmployeeByID(self,id):
        for obj in self.employees:
            if id == obj.get_employee_id():
                return obj
        return False

    def getEventByID(self,id):
        for obj in self.events:
            if id == obj.getEventID():
                return obj
        return False

    def getClientByID(self,id):
        for obj in self.clients:
            if id == obj.getClientID():
                return obj
        return False

    def getGuestByID(self,id):
        for obj in self.guests:
            if id == obj.getGuestID():
                return obj
        return False

    def getSupplierByID(self,id):
        self.getSuppliers()
        for obj in self.getSuppliers():
            if id == obj.getId():
                return obj
        return False

    def removeEmployeeByID(self,id):
        for obj in self.employees:
            if id == obj.get_employee_id():
                self.employees.remove(obj)
                print("Employee Removed.")
                return
        print("Employee Not Found")

    def removeEventByID(self,id):
        for obj in self.events:
            if id == obj.getEventID():
                self.events.remove(obj)
                print("Event Removed.")
                return
        print("Event Not Found")

    def removeClientByID(self,id):
        for obj in self.clients:
            if id == obj.getClientID():
                self.clients.remove(obj)
                print("Client Removed.")
                return
        print("Client Not Found")

    def removeGuestByID(self, id):
        for obj in self.guests:
            if id == obj.getGuestID():
                self.guests.remove(obj)
                print("Guest Removed.")
                return
        print("Guest Not Found")

    def removeSupplierByID(self, id):
        for obj in self.getSuppliers():
            if id == obj.getGuestID():
                if type(obj) == CateringSupplier:
                    self.cateringCompanies.remove(obj)
                elif type(obj) == self.cleaningCompanies:
                    self.cleaningCompanies.remove(obj)
                elif type(obj) == self.decorationsCompanies:
                    self.decorationsCompanies.remove(obj)
                elif type(obj) == self.furnitureSupplyCompanies:
                    self.furnitureSupplyCompanies.remove(obj)
                print("Supplier Removed.")
                return
        print("Supplier Not Found")

    def AddGuestIntoEvent(self,event_id,guest_id):

        guest = self.getGuestByID(guest_id)
        event = self.getEventByID(event_id)

        if guest != False and event!= False:
            event.guestList.append(guest)
            return True

        else:
            print("Wrong Information provided")
            return False


class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details

    # Getters and setters
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_employee_id(self):
        return self.employee_id

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def get_job_title(self):
        return self.job_title

    def set_job_title(self, job_title):
        self.job_title = job_title

    def get_basic_salary(self):
        return self.basic_salary

    def set_basic_salary(self, basic_salary):
        self.basic_salary = basic_salary

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def get_passport_details(self):
        return self.passport_details

    def set_passport_details(self, passport_details):
        self.passport_details = passport_details

    def details(self):
        details = "\n*** Employee {} ***\n".format(self.get_employee_id())
        details += "Name : {}\nDepartment : {}\nJob : {}\nSalary : {}" \
                   "\nAge : {}\nDate of Birth : {}\nPassport : {}\n".format(self.get_name(),self.get_department(),
                                                                            self.get_job_title(),self.get_basic_salary(),
                                                                            self.get_age(),self.get_date_of_birth(),
                                                                            self.get_passport_details())
        return details




class SalesManager(Employee):
    pass


class Salesperson(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details,manager_id):
        super(Salesperson, self).__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.manager_id = manager_id

    def details(self):
        details = "\n*** Employee {} ***\n".format(self.get_employee_id())
        details += "Name : {}\nDepartment : {}\nJob : {}\nSalary : {}" \
                   "\nAge : {}\nDate of Birth : {}\nPassport : {}\nManager ID : {}\n".format(self.get_name(),self.get_department(),
                                                                            self.get_job_title(),self.get_basic_salary(),
                                                                            self.get_age(),self.get_date_of_birth(),
                                                                            self.get_passport_details(),self.get_manager_id())
        return details

    def get_manager_id(self):
        return self.manager_id

    def set_manager_id(self,id):
        self.manager_id = id



class MarketingManager(Employee):
    pass


class Marketer(Employee):
    pass


class Accountant(Employee):
    pass


class Designer(Employee):
    pass


class Handyman(Employee):
    pass

class Event:
    def __init__(self, eventID, eventType, theme, date, time, duration, venueAddress, clientID, invoice, guestList=[], cateringCompany="", cleaningCompany="", decorationsCompany="", furnitureSupplyCompany=""):
        self.eventID = eventID
        self.eventType = eventType
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venueAddress = venueAddress
        self.clientID = clientID
        self.guestList = guestList
        self.cateringCompany = cateringCompany
        self.cleaningCompany = cleaningCompany
        self.decorationsCompany = decorationsCompany
        self.furnitureSupplyCompany = furnitureSupplyCompany
        self.invoice = invoice

    def getEventID(self):
        return self.eventID

    def setEventID(self, eventID):
        self.eventID = eventID

    def getEventType(self):
        return self.eventType

    def setEventType(self, eventType):
        self.eventType = eventType

    def getTheme(self):
        return self.theme

    def setTheme(self, theme):
        self.theme = theme

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def getDuration(self):
        return self.duration

    def setDuration(self, duration):
        self.duration = duration

    def getVenueAddress(self):
        return self.venueAddress

    def setVenueAddress(self, venueAddress):
        self.venueAddress = venueAddress

    def getClientID(self):
        return self.clientID

    def setClientID(self, clientID):
        self.clientID = clientID

    def getGuestList(self):
        return self.guestList

    def setGuestList(self, guestList):
        self.guestList = guestList

    def getCateringCompany(self):
        return self.cateringCompany

    def setCateringCompany(self, cateringCompany):
        self.cateringCompany = cateringCompany

    def getCleaningCompany(self):
        return self.cleaningCompany

    def setCleaningCompany(self, cleaningCompany):
        self.cleaningCompany = cleaningCompany

    def getDecorationsCompany(self):
        return self.decorationsCompany

    def setDecorationsCompany(self, decorationsCompany):
        self.decorationsCompany = decorationsCompany

    def getFurnitureSupplyCompany(self):
        return self.furnitureSupplyCompany

    def setFurnitureSupplyCompany(self, furnitureSupplyCompany):
        self.furnitureSupplyCompany = furnitureSupplyCompany

    def getInvoice(self):
        return self.invoice

    def setInvoice(self, invoice):
        self.invoice = invoice

    def details(self):
        # Catering_name =
        # Cleaning_name =
        # Decorations_name =
        # FurnitureSupply_name =

        details = "\n*** Event {} ***\n".format(self.getEventID())
        details += "Event Type : {}\nTheme : {}\nDate : {}\nTime : {}\n" \
                   "Dureation : {}\nAddress : {}\nClient ID : {}\nInvoice : {}\nGuests : {}\n" \
                   "Catering Company : {}\nCleaning Company : {}\nDecorations Company : {}\n" \
                   "Furniture Supply Company : {}\n".format(self.getEventType(),self.getTheme(),self.getDate(),
                                                            self.getTime(),self.getDuration(),self.getVenueAddress(),
                                                            self.getClientID(),self.getInvoice(),len(self.getGuestList()),
                                                            self.getCateringCompany(),self.getCleaningCompany(),
                                                            self.getDecorationsCompany(),self.getFurnitureSupplyCompany())
        return details

class Wedding(Event):
    pass

class Birthday(Event):
    pass

class ThemedParty(Event):
    pass

class Graduation(Event):
    pass


class Client:
    def __init__(self, clientID, name, address, contactDetails, budget):
        self.clientID = clientID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.budget = budget

    def getClientID(self):
        return self.clientID

    def setClientID(self, clientID):
        self.clientID = clientID

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getContactDetails(self):
        return self.contactDetails

    def setContactDetails(self, contactDetails):
        self.contactDetails = contactDetails

    def getBudget(self):
        return self.budget

    def setBudget(self, budget):
        self.budget = budget

    def organize_event(self):
        pass

    # Details method
    def details(self):
        details = "\n*** Client {} ***\n".format(self.getClientID())
        details += "Name: {}\nAddress: {}\nContact Details: {}\nBudget: {}\n".format(
            self.getName(), self.getAddress(), self.getContactDetails(), self.getBudget()
        )
        return details

class Guest:
    def __init__(self, guestID, name, address, contactDetails):
        self.guestID = guestID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

    def getGuestID(self):
        return self.guestID

    def setGuestID(self, guestID):
        self.guestID = guestID

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getContactDetails(self):
        return self.contactDetails

    def setContactDetails(self, contactDetails):
        self.contactDetails = contactDetails

    def attend_event(self):
        pass

    def details(self):
        details = "\n*** Guest {} ***\n".format(self.getGuestID())
        details += "Name: {}\nAddress: {}\nContact Details: {}\n".format(
            self.getName(), self.getAddress(), self.getContactDetails()
        )
        return details


class Supplier():

    def __init__(self,id,name,address,contact,supplier_type):
        self.name = name
        self.address = address
        self.contact = contact
        self.id = id
        self.supplier_type = supplier_type

    def offer_catering_service(self):
        pass

    def offer_cleaning_service(self):
        pass

    def offer_furniture_service(self):
        pass

    def offer_decorations_service(self):
        pass

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSupplierType(self):
        return self.supplier_type

    def setSupplierType(self, st):
        self.supplier_type = st

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getContact(self):
        return self.contact

    def setContact(self, contact):
        self.contact = contact

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def __repr__(self):
        return self.getName()

    def details(self):
        details = "\n*** Supplier {} ***\n".format(self.getId())
        details += "Name : {}\nAddress: {}\nContact: {}\n".format(self.getName(),self.getAddress(), self.getContact())
        return details



class CateringSupplier(Supplier):
    pass

class DecorationsSupplier(Supplier):
    pass

class CleaningSupplier(Supplier):
    pass

class FurnitureSupplier(Supplier):
    pass








class EventManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Event Management System")
        self.geometry("950x600")
        self.configure(bg="lightgray")

        self.EventManagementSystem = EventManagementSystem("MyEventManagement","Fatima Alrashdi")

        # Creating Employees
        sm = SalesManager("Nora","3","Sales","Sales Manager","20000","32","1/1/1994","PP6752383")
        sp1 = Salesperson("Sales Person 1","1","Sales","Sales Person","10000","30","1/1/1995","PP123456","3")
        sp2 = Salesperson("Sales Person 2", "2", "Sales", "Sales Person", "10000", "30", "1/1/1995", "PP867878", "3")
        accountant = Accountant("Salem","4","Accounts","Accountant","18000","32","1/1/1994","PP87517239")

        self.EventManagementSystem.employees.extend([sm,sp1,sp2,accountant])

        # Creating Events
        event1 = Wedding("1","Weeding","Theme1","5/2/2024","8PM","2 hours","UAE","1","50000")
        event2 = Birthday("2", "Birthday", "Batman", "5/2/2024", "5PM", "2 hours", "UAE", "2", "10000")
        event3 = Graduation("3", "Graduation", "Theme3", "5/2/2024", "2PM", "2 hours", "UAE", "3", "20000")

        self.EventManagementSystem.events.extend([event1,event2,event3])

        # Creating clients
        client1 = Client("1","Khaled","Street 1 Dubai","3457394793","50000")
        client2 = Client("2", "Mariam", "Street 2 Dubai", "97932484", "10000")
        client3 = Client("3", "Aisha", "Street 3 Dubai", "12234939", "20000")

        self.EventManagementSystem.clients.extend([client1,client2,client3])

        # creating guests
        guest1 = Guest("1","Fatima","Street 4 Dubai","3423434")
        guest2 = Guest("2", "Hamdan", "Street 5 Dubai", "34234499")
        guest3 = Guest("3", "Amna", "Street 6 Dubai", "5432234")
        guest4 = Guest("4", "Alya", "Street 7 Dubai", "8688797")
        guest5 = Guest("5", "Mahra", "Street 8 Dubai", "3423434")

        self.EventManagementSystem.guests.extend([guest1,guest2,guest3,guest4,guest5])

        # creating suppliers
        supplier1 = CateringSupplier("1","Catering Supplier","UAE","43454345","catering")
        supplier2 = CleaningSupplier("2", "Cleaning Supplier", "UAE", "753465", "cleaning")
        supplier3 = DecorationsSupplier("3", "Decoration Supplier", "UAE", "2343564", "decoration")
        supplier4 = FurnitureSupplier("4", "Furniture Supplier", "UAE", "87967980", "furniture")

        self.EventManagementSystem.cateringCompanies.append(supplier1)
        self.EventManagementSystem.cleaningCompanies.append(supplier2)
        self.EventManagementSystem.decorationsCompanies.append(supplier3)
        self.EventManagementSystem.furnitureSupplyCompanies.append(supplier4)




        # Create and configcre the title label with a black border
        title_label = tk.Label(self, text="Event Management System", font=("Arial", 18), bg="white", bd=8)
        title_label.place(relx=0.5, rely=0.01, anchor="n")

        labels_names = ["Employees","Events","Clients","Guests","Suppliers"]
        labels_rely = 0.15
        for i in range(0, 5):
            label = tk.Label(self, text=f"{labels_names[i]} :", font=("Arial", 12), bg="white", fg="black")
            label.place(relx=0.02, rely=labels_rely, anchor="w")
            labels_rely += 0.1

        # Buttons
        buttons_rely = 0.15
        button_functions = [self.add_Employee_window, self.add_Event_window, self.add_Client_window, self.add_Guest_window, self.add_Supplier_window]
        for i in range(0, 5):
            button = tk.Button(self, text=f"Add", command=button_functions[i])
            button.place(relx=0.15, rely=buttons_rely, anchor="w",width=50)
            buttons_rely += 0.1


        # Buttons
        buttons_rely = 0.15
        display_functions = [self.display_employees, self.display_events, self.display_clients, self.display_guests, self.display_suppliers]
        for i in range(0, 5):
            button = tk.Button(self, text=f"Display All", command=display_functions[i])
            button.place(relx=0.55, rely=buttons_rely, anchor="w",width=80)
            buttons_rely += 0.1

        # Buttons
        buttons_rely = 0.15
        modify_functions = [self.modify_employee, self.modify_event, self.modify_client, self.modify_guest, self.modify_supplier]
        for i in range(0, 5):
            button = tk.Button(self, text=f"Modify", command=modify_functions[i])
            button.place(relx=0.35, rely=buttons_rely, anchor="w",width=80)
            buttons_rely += 0.1

        # Buttons
        buttons_rely = 0.15
        delete_functions = [self.delete_employee, self.delete_event, self.delete_client, self.delete_guest, self.delete_supplier]
        for i in range(0, 5):
            button = tk.Button(self, text=f"Delete", command=delete_functions[i])
            button.place(relx=0.45, rely=buttons_rely, anchor="w",width=80)
            buttons_rely += 0.1


        self.employee_id_entry = tk.Entry(self, width=10)
        self.employee_id_entry.insert(0, "")
        self.employee_id_entry.place(relx=0.25, rely=0.15, anchor="w")

        self.event_id_entry = tk.Entry(self, width=10)
        self.event_id_entry.insert(0, "")
        self.event_id_entry.place(relx=0.25, rely=0.25, anchor="w")

        self.client_id_entry = tk.Entry(self, width=10)
        self.client_id_entry.insert(0, "")
        self.client_id_entry.place(relx=0.25, rely=0.35, anchor="w")

        self.guest_id_entry = tk.Entry(self, width=10)
        self.guest_id_entry.insert(0, "")
        self.guest_id_entry.place(relx=0.25, rely=0.45, anchor="w")

        self.supplier_id_entry = tk.Entry(self, width=10)
        self.supplier_id_entry.insert(0, "")
        self.supplier_id_entry.place(relx=0.25, rely=0.55, anchor="w")

        level_event = tk.Label(self, text="Event ID")
        label_guest = tk.Label(self, text="Guest ID")

        level_event.place(relx=0.02, rely=0.65, anchor="w")
        label_guest.place(relx=0.1, rely=0.65, anchor="w")


        self.e1_event = tk.Entry(self, width=10)
        self.e1_event.insert(0, "")
        self.e1_event.place(relx=0.02, rely=0.7, anchor="w")

        self.e2_guest = tk.Entry(self, width=10)
        self.e2_guest.insert(0, "")
        self.e2_guest.place(relx=0.1, rely=0.7, anchor="w")

        self.add_guest_to_event = tk.Button(self, text="Add Guest into Event", command=self.AddGuestIntoEvent)
        self.add_guest_to_event.place(relx=0.25, rely=0.7, anchor="center")

        self.show_all_event_guests = tk.Button(self, text="Show all Event Guests", command=self.ShowAllGuestsOfEvent)
        self.show_all_event_guests.place(relx=0.25, rely=0.8, anchor="center")

        label_event2 = tk.Label(self, text="Event ID")
        label_event2.place(relx=0.02, rely=0.75, anchor="w")

        self.e2_event = tk.Entry(self, width=10)
        self.e2_event.insert(0, "")
        self.e2_event.place(relx=0.02, rely=0.8, anchor="w")

        label_event3 = tk.Label(self, text="Event ID")
        label_event3.place(relx=0.02, rely=0.85, anchor="w")

        self.e3_event = tk.Entry(self, width=10)
        self.e3_event.insert(0, "")
        self.e3_event.place(relx=0.02, rely=0.9, anchor="w")

        label_supplier = tk.Label(self, text="Supplier ID")
        label_supplier.place(relx=0.1, rely=0.85, anchor="w")

        self.e4_supplier = tk.Entry(self, width=10)
        self.e4_supplier.insert(0, "")
        self.e4_supplier.place(relx=0.1, rely=0.9, anchor="w")

        self.add_supplier_to_event = tk.Button(self, text="Add Supplier to Event", command=self.AddSupplierToEvent)
        self.add_supplier_to_event.place(relx=0.25, rely=0.9, anchor="center")

        label = tk.Label(self, text="Output Window", font=("Arial", 12), bg="white", fg="black")
        label.place(relx=0.88, rely=0.13, anchor="ne")

        # Output text area
        self.output_text = tk.Text(self, wrap="word", width=38, height=28)
        self.output_text.place(relx=0.98, rely=0.19, anchor="ne")

    def add_Employee_window(self):
        new_window = tk.Toplevel(self)
        new_window.geometry("350x500")
        new_window.title("Add Employee")

        # Dropdown menu for job titles
        job_titles = [
            "Sales Managers",
            "Salespersons",
            "Marketing Managers",
            "Marketers",
            "Accountants",
            "Designers",
            "Handymen"
        ]
        selected_job = tk.StringVar(new_window)
        selected_job.set(job_titles[0])  # Default value
        job_label = tk.Label(new_window, text="Select Employee Type")
        job_label.pack()
        job_dropdown = tk.OptionMenu(new_window, selected_job, *job_titles)
        job_dropdown.pack()

        # Name
        name_label = tk.Label(new_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(new_window)
        name_entry.pack()

        # Employee ID
        employee_id_label = tk.Label(new_window, text="Employee ID:")
        employee_id_label.pack()
        employee_id_entry = tk.Entry(new_window)
        employee_id_entry.pack()

        # Department
        department_label = tk.Label(new_window, text="Department:")
        department_label.pack()
        department_entry = tk.Entry(new_window)
        department_entry.pack()

        # Basic Salary
        basic_salary_label = tk.Label(new_window, text="Basic Salary:")
        basic_salary_label.pack()
        basic_salary_entry = tk.Entry(new_window)
        basic_salary_entry.pack()

        # Age
        age_label = tk.Label(new_window, text="Age:")
        age_label.pack()
        age_entry = tk.Entry(new_window)
        age_entry.pack()

        # Date of Birth
        dob_label = tk.Label(new_window, text="Date of Birth:")
        dob_label.pack()
        dob_entry = tk.Entry(new_window)
        dob_entry.pack()

        # Passport Details
        passport_label = tk.Label(new_window, text="Passport Details:")
        passport_label.pack()
        passport_entry = tk.Entry(new_window)
        passport_entry.pack()

        # Passport Details
        manager_id = tk.Label(new_window, text="Manager ID:")
        manager_id.pack()
        manager_id_entry = tk.Entry(new_window)
        manager_id_entry.pack()

        # Button to add employee
        add_button = tk.Button(new_window, text="Add Employee", command=lambda: self.EventManagementSystem.add_employee(
            selected_job.get(),
            name_entry.get(),
            employee_id_entry.get(),
            department_entry.get(),
            basic_salary_entry.get(),
            age_entry.get(),
            dob_entry.get(),
            passport_entry.get(),
            manager_id_entry.get()
        ))
        add_button.pack()

        self.output_text.insert(tk.END, "Adding Employee...\n")

    def add_Event_window(self):
        new_window = tk.Toplevel(self)
        new_window.geometry("350x600")
        new_window.title("Add Event")

        # Event ID
        event_id_label = tk.Label(new_window, text="Event ID:")
        event_id_label.pack()
        event_id_entry = tk.Entry(new_window)
        event_id_entry.pack()

        # Event Type
        event_type_label = tk.Label(new_window, text="Event Type:")
        event_type_label.pack()
        event_type_entry = tk.Entry(new_window)
        event_type_entry.pack()

        # Theme
        theme_label = tk.Label(new_window, text="Theme:")
        theme_label.pack()
        theme_entry = tk.Entry(new_window)
        theme_entry.pack()

        # Date
        date_label = tk.Label(new_window, text="Date:")
        date_label.pack()
        date_entry = tk.Entry(new_window)
        date_entry.pack()

        # Time
        time_label = tk.Label(new_window, text="Time:")
        time_label.pack()
        time_entry = tk.Entry(new_window)
        time_entry.pack()

        # Duration
        duration_label = tk.Label(new_window, text="Duration:")
        duration_label.pack()
        duration_entry = tk.Entry(new_window)
        duration_entry.pack()

        # Venue Address
        venue_label = tk.Label(new_window, text="Venue Address:")
        venue_label.pack()
        venue_entry = tk.Entry(new_window)
        venue_entry.pack()

        # Client ID
        client_id_label = tk.Label(new_window, text="Client ID:")
        client_id_label.pack()
        client_id_entry = tk.Entry(new_window)
        client_id_entry.pack()

        # Invoice
        invoice_label = tk.Label(new_window, text="Invoice:")
        invoice_label.pack()
        invoice_entry = tk.Entry(new_window)
        invoice_entry.pack()

        # Button to add event
        add_button = tk.Button(new_window, text="Add Event", command=lambda: self.EventManagementSystem.add_event(
            event_id_entry.get(),
            event_type_entry.get(),
            theme_entry.get(),
            date_entry.get(),
            time_entry.get(),
            duration_entry.get(),
            venue_entry.get(),
            client_id_entry.get(),
            invoice_entry.get()
        ))
        add_button.pack()

        self.output_text.insert(tk.END, "Adding Event...\n")

    def add_Client_window(self):
        new_window = tk.Toplevel(self)
        new_window.geometry("350x400")
        new_window.title("Add Client")

        # Client ID
        client_id_label = tk.Label(new_window, text="Client ID:")
        client_id_label.pack()
        client_id_entry = tk.Entry(new_window)
        client_id_entry.pack()

        # Name
        name_label = tk.Label(new_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(new_window)
        name_entry.pack()

        # Address
        address_label = tk.Label(new_window, text="Address:")
        address_label.pack()
        address_entry = tk.Entry(new_window)
        address_entry.pack()

        # Contact Details
        contact_label = tk.Label(new_window, text="Contact Details:")
        contact_label.pack()
        contact_entry = tk.Entry(new_window)
        contact_entry.pack()

        # Budget
        budget_label = tk.Label(new_window, text="Budget:")
        budget_label.pack()
        budget_entry = tk.Entry(new_window)
        budget_entry.pack()

        # Button to add client
        add_button = tk.Button(new_window, text="Add Client", command=lambda: self.EventManagementSystem.add_client(
            client_id_entry.get(),
            name_entry.get(),
            address_entry.get(),
            contact_entry.get(),
            budget_entry.get()
        ))
        add_button.pack()

        self.output_text.insert(tk.END, "Adding Client...\n")

    def add_Guest_window(self):
        new_window = tk.Toplevel(self)
        new_window.geometry("350x400")
        new_window.title("Add Guest")

        # Guest ID
        guest_id_label = tk.Label(new_window, text="Guest ID:")
        guest_id_label.pack()
        guest_id_entry = tk.Entry(new_window)
        guest_id_entry.pack()

        # Name
        name_label = tk.Label(new_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(new_window)
        name_entry.pack()

        # Address
        address_label = tk.Label(new_window, text="Address:")
        address_label.pack()
        address_entry = tk.Entry(new_window)
        address_entry.pack()

        # Contact Details
        contact_label = tk.Label(new_window, text="Contact Details:")
        contact_label.pack()
        contact_entry = tk.Entry(new_window)
        contact_entry.pack()

        # Button to add guest
        add_button = tk.Button(new_window, text="Add Guest", command=lambda: self.EventManagementSystem.add_guest(
            guest_id_entry.get(),
            name_entry.get(),
            address_entry.get(),
            contact_entry.get()
        ))
        add_button.pack()

        self.output_text.insert(tk.END, "Adding Guest...\n")

    def add_Supplier_window(self):
        new_window = tk.Toplevel(self)
        new_window.geometry("350x500")
        new_window.title("Add Supplier")
        self.output_text.insert(tk.END, "Adding Supplier...\n")

        # Dropdown menu for job titles
        supplier_types = [
            "catering","decorations",
            "cleaning","furniture"
        ]
        selected_supplier = tk.StringVar(new_window)
        selected_supplier.set(supplier_types[0])
        supplier_types_label = tk.Label(new_window, text="Select Supplier Type")
        supplier_types_label.pack()
        supplier_dropdown = tk.OptionMenu(new_window, selected_supplier, *supplier_types)
        supplier_dropdown.pack()

        # Name
        name_label = tk.Label(new_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(new_window)
        name_entry.pack()

        # Address
        address_label = tk.Label(new_window, text="Address:")
        address_label.pack()
        address_entry = tk.Entry(new_window)
        address_entry.pack()

        # Contact
        contact_label = tk.Label(new_window, text="Contact:")
        contact_label.pack()
        contact_entry = tk.Entry(new_window)
        contact_entry.pack()

        # Button to add guest
        add_supplier = tk.Button(new_window, text="Add Supplier", command=lambda: self.EventManagementSystem.add_supplier(
            selected_supplier.get(),
            name_entry.get(),
            address_entry.get(),
            contact_entry.get()
        ))
        add_supplier.pack()

    def display_employees(self):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, "Displaying Employees...\n")

        employees = self.EventManagementSystem.getEmployees()
        all_details = ""
        for i in employees:
            all_details += i.details()
        self.output_text.insert(tk.END, all_details)


    def display_events(self):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, "Displaying Events...\n")

        events = self.EventManagementSystem.getEvents()
        all_details = ""
        for i in events:
            all_details += i.details()
        self.output_text.insert(tk.END, all_details)

    def display_clients(self):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, "Displaying Clients...\n")

        clients = self.EventManagementSystem.getClients()
        all_details = ""
        for i in clients:
            all_details += i.details()
        self.output_text.insert(tk.END, all_details)

    def display_guests(self):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, "Displaying Guests...\n")

        guests = self.EventManagementSystem.getGuests()
        all_details = ""
        for i in guests:
            all_details += i.details()
        self.output_text.insert(tk.END, all_details)

    def display_suppliers(self):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, "Displaying Suppliers...\n")

        suppliers = self.EventManagementSystem.getSuppliers()
        all_details = ""
        for i in suppliers:
            all_details += i.details()
        self.output_text.insert(tk.END, all_details)


        
if __name__ == "__main__":
    app = EventManagementApp()
    app.mainloop()
