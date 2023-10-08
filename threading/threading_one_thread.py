import threading

# Function that will be executed in parallel in a thread


def my_function():
    for _ in range(5):
        print("Executing in a thread")


# Create a new thread
my_thread = threading.Thread(target=my_function)

# Start the thread
my_thread.start()

# Wait for the thread to finish before continuing with the rest of the code
my_thread.join()

print("Main thread continues execution")

"""
Explanation:
The threading module provides a Thread class to create and manage threads in Python.
To spawn other threads, you need to call the start() method on the Thread instance.
Once you call start(), the new thread will execute the function given as the target
in the constructor, in parallel with the other threads. When the function returns,
the thread terminates without executing the rest of the code.
"""
