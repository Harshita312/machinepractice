class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def display(self):
        return self.items

# Queue implementation
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def display(self):
        return self.items

# Main program
def main():
    stack = Stack()
    queue = Queue()

    while True:
        print("Stack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")

        print("Queue Operations:")
        print("5. Enqueue")
        print("6. Dequeue")
        print("7. Display")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter item to push: ")
            stack.push(item)
            print("Item pushed successfully!")

        elif choice == 2:
            item = stack.pop()
            if item is not None:
                print("Item popped:", item)
            else:
                print("Stack is empty!")

        elif choice == 3:
            print("Stack:", stack.display())

        elif choice == 4:
            break

        elif choice == 5:
            item = input("Enter item to enqueue: ")
            queue.enqueue(item)
            print("Item enqueued successfully!")

        elif choice == 6:
            item = queue.dequeue()
            if item is not None:
                print("Item dequeued:", item)
            else:
                print("Queue is empty!")

        elif choice == 7:
            print("Queue:", queue.display())

        elif choice == 8:
            break

        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
