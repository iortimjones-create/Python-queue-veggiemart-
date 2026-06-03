from collections import deque

class VeggieMartQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Order added: {order}. Queue size: {len(self.queue)}")

    def dequeue(self):
        if self.is_empty():
            print("No orders to process!")
            return None
        order = self.queue.popleft()
        print(f"Processing order: {order}")
        return order

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

# Test run
if __name__ == "__main__":
    veggie_queue = VeggieMartQueue()
    veggie_queue.enqueue("Order #1: Tomatoes")
    veggie_queue.enqueue("Order #2: Onions")
    veggie_queue.enqueue("Order #3: Peppers")
    print(f"Next order: {veggie_queue.peek()}")
    veggie_queue.dequeue()
    print(f"Queue empty? {veggie_queue.is_empty()}")


