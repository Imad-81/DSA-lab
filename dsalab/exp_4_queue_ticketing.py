import heapq
import time

class Ticket:
    """
    Represents a customer support ticket.
    Priority: 1 (Urgent), 2 (Normal), 3 (Low)
    Lower priority value means higher priority in processing.
    """
    _id_counter = 1

    def __init__(self, customer_name, issue, priority=2):
        self.id = Ticket._id_counter
        Ticket._id_counter += 1
        self.customer_name = customer_name
        self.issue = issue
        self.priority = priority
        self.timestamp = time.time()  # To maintain FCFS for same priority

    def __lt__(self, other):
        # Priority Queue (heapq) is a min-heap.
        # We want lower priority value processed first.
        # If priorities are equal, we use timestamp (FCFS).
        if self.priority == other.priority:
            return self.timestamp < other.timestamp
        return self.priority < other.priority

    def __str__(self):
        priority_str = {1: "Urgent", 2: "Normal", 3: "Low"}.get(self.priority, "Unknown")
        return f"[ID: {self.id}] Priority: {priority_str} | Customer: {self.customer_name} | Issue: {self.issue}"


class TicketingSystem:
    def __init__(self):
        self.queue = []  # List used as a priority queue

    def submit_ticket(self, name, issue, priority):
        ticket = Ticket(name, issue, priority)
        heapq.heappush(self.queue, ticket)
        print(f"\nTicket submitted successfully! {ticket}")

    def display_tickets(self):
        if not self.queue:
            print("\nNo pending tickets.")
            return

        print("\n--- Current Pending Tickets (Sorted by Priority & Time) ---")
        # We need to sort because heapq doesn't maintain absolute order, only the min property
        sorted_tickets = sorted(self.queue)
        for ticket in sorted_tickets:
            print(ticket)

    def process_ticket(self):
        if not self.queue:
            print("\nNo tickets to process.")
            return

        ticket = heapq.heappop(self.queue)
        print(f"\nProcessing Ticket: {ticket}")
        print("Status: Resolved.")


def main():
    system = TicketingSystem()
    print("Welcome to the Customer Support Ticketing System")

    while True:
        print("\n1. Submit Ticket")
        print("2. Display Current Tickets")
        print("3. Process/Resolve Ticket")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            name = input("Enter Customer Name: ")
            issue = input("Enter Issue Description: ")
            print("Select Priority:")
            print("1. Urgent")
            print("2. Normal")
            print("3. Low")
            try:
                priority = int(input("Choice (1-3): "))
                if priority not in [1, 2, 3]:
                    raise ValueError
            except ValueError:
                print("Invalid priority. Defaulting to Normal (2).")
                priority = 2
            
            system.submit_ticket(name, issue, priority)

        elif choice == '2':
            system.display_tickets()

        elif choice == '3':
            system.process_ticket()

        elif choice == '4':
            print("Exiting Ticketing System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
