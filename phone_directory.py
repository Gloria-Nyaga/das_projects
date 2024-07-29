class ContactNode:

    def __init__(self, name, phone_number, age, classroom, email):
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.classroom = classroom
        self.email = email
        self.prev = None 
        self.next = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.contact_map = {} 

    def add_contact(self, name, phone_number, age, classroom, email):
        new_node = ContactNode(name, phone_number, age, classroom, email)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.contact_map[name.lower()] = new_node

    def display_contacts(self):
        current = self.head
        while current:
            print(f"{current.name}: {current.phone_number} : {current.age} : {current.classroom}, {current.email}", end=" <-> ")
            current = current.next
        print("None") 

    def search_contact(self, name): 
        contact = self.contact_map.get(name.lower()) 
        if contact:
            return f"Found: {name} , Age: {contact['age']}, Classroom: {contact['classroom']}, Email: {contact['email']}"
        else:
            return "Contact not found."

    def delete_contact(self, name):
        current = self.contact_map.get(name.lower()) 
        if current:
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            if current == self.head: 
                self.head = current.next
            if current == self.tail:
                self.tail = current.prev
            
            del self.contact_map[name.lower()]
            print(f"Contact {current.name} deleted successfully.")
        else:
            print("Contact not found.")

    def filter_contacts_by_age(self, min_age):
        filtered_contacts = []
        current = self.head
        while current:
            if current.age >= min_age:
                filtered_contacts.append(current)
            current = current.next
        return filtered_contacts

    def group_contacts_by_classroom(self):
        classroom_groups = {}
        current = self.head
        while current:
            classroom = current.classroom
            if classroom in classroom_groups:
                classroom_groups[classroom].append(current)
            else:
                classroom_groups[classroom] = [current]
            current = current.next
        return classroom_groups

    def reshape_contact_data(self):
        reshaped_data = []
        current = self.head
        while current:
            reshaped_data.append((current.name, current.phone_number))
            current = current.next
        return reshaped_data

if __name__ == "__main__":
    directory = DoublyLinkedList()
    
    while True:
        print("\nPhone Directory Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Filter Contacts by Age")
        print("6. Group Contacts by Classroom")
        print("7. Reshape Contact Data")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            age = int(input("Enter age: "))
            classroom = input("Enter classroom: ")
            email = input("Enter email: ")
            directory.add_contact(name, phone_number, age, classroom, email)
            print(f"Contact {name} added successfully.")

        elif choice == '2':
            name = input("Enter name to search: ")
            contact = directory.search_contact(name)
            if contact:
                print(f"Found: {contact.name} - {contact.phone_number}, Age: {contact.age}, Classroom: {contact.classroom}, Email: {contact.email}")
            else:
                print("Sorry, this contact cannot be found.")

        elif choice == '3':
            name = input("Enter name to delete: ")
            directory.delete_contact(name)

        elif choice == '4':
            print("Contacts in the directory:")
            directory.display_contacts()

        elif choice == '5':
            min_age = int(input("Enter minimum age: "))
            filtered_contacts = directory.filter_contacts_by_age(min_age)
            print(f"Contacts with age >= {min_age}:")
            for contact in filtered_contacts:
                print(f"{contact.name} - {contact.age}")

        elif choice == '6':
            classroom_groups = directory.group_contacts_by_classroom()
            print("Contacts grouped by classroom:")
            for classroom, contacts in classroom_groups.items():
                print(f"Classroom: {classroom}")
                for contact in contacts:
                    print(f"{contact.name} - {contact.phone_number}")
                print()

        elif choice == '7':
            reshaped_data = directory.reshape_contact_data()
            print("Reshaped contact data (Name, Phone Number):")
            for name, phone_number in reshaped_data:
                print(f"{name} - {phone_number}")

        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
