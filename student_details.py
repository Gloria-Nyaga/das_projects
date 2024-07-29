import heapq

class ContactNode:
    def __init__(self, name, phone_number, age, classroom, email, priority):
        self.name = name
        self.phone_number = phone_number
        self.age = age
        self.classroom = classroom
        self.email = email
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class PriorityQueue:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        heapq.heappush(self.contacts, contact)

    def remove_contact(self):
        return heapq.heappop(self.contacts) if self.contacts else None

    def display_contacts(self):
        for contact in sorted(self.contacts):
            print(f"{contact.name}: {contact.phone_number} : {contact.age} : {contact.classroom}, {contact.email}, Priority: {contact.priority}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

class PhoneDirectory:
    def __init__(self):
        self.contact_map = {} 
        self.priority_queue = PriorityQueue()

    def add_contact(self, name, phone_number, age, classroom, email, priority):
        new_node = ContactNode(name, phone_number, age, classroom, email, priority)
        self.priority_queue.add_contact(new_node)
        self.contact_map[name.lower()] = new_node 

    def search_contact(self, name):

        return self.contact_map.get(name.lower(), None)

    def delete_contact(self, name):
        contact = self.contact_map.get(name.lower())
        if contact:  
            self.priority_queue.contacts.remove(contact)
            heapq.heapify(self.priority_queue.contacts)  # Re-heapify after removal
            
            del self.contact_map[name.lower()]

    def display_contacts(self):
        self.priority_queue.display_contacts()

if __name__ == "__main__":
    directory = PhoneDirectory()
    
    while True:
        print("\nPhone Directory Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Remove Highest Priority Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            age = int(input("Enter age: "))
            classroom = input("Enter classroom: ")
            email = input("Enter email: ")
            priority = int(input("Enter priority (lower number means higher priority): "))
            directory.add_contact(name, phone_number, age, classroom, email, priority)
            print(f"Contact {name} added successfully.")

        elif choice == '2':
            name = input("Enter name to search: ")
            contact = directory.search_contact(name)
            if contact:
                print(f"Found: {contact.name} - {contact.phone_number}, Age: {contact.age}, Classroom: {contact.classroom}, Email: {contact.email}, Priority: {contact.priority}")
            else:
                print("Sorry, this contact cannot be found.")

        elif choice == '3':
            removed_contact = directory.priority_queue.remove_contact()
            if removed_contact:
                print(f"Removed contact: {removed_contact.name}")
            else:
                print("No contacts to remove.")

        elif choice == '4':
            print("Contacts in the directory:")
            directory.display_contacts()

        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
