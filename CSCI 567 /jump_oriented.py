# This example demonstrates the concept of Jump-Oriented Programming (JOP)
# in a very simplified manner.

# Define some functions that mimic "gadgets"
def gadget1():
    print("Gadget 1: Setting up...")
    return gadget2  # Return the next gadget to execute

def gadget2():
    print("Gadget 2: Performing an action")
    return gadget3  # Return the next gadget to execute

def gadget3():
    print("Gadget 3: Cleaning up")
    return None  # End of the chain

# Mimic a JOP chain execution
def execute_jop_chain(start_gadget):
    gadget = start_gadget
    while gadget is not None:
        next_gadget = gadget()  # Execute the gadget and get the next
        gadget = next_gadget

# Start the JOP chain with gadget1
if __name__ == "__main__":
    execute_jop_chain(gadget1)
