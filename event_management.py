



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


