import threading

# Function to be executed in a thread


def print_messages():
    for _ in range(5):
        print("Current thread: {}".format(threading.current_thread().name))


# Create two threads
thread1 = threading.Thread(target=print_messages, name="Thread 1")
thread2 = threading.Thread(target=print_messages, name="Thread 2")

# Start the threads
print("Thread 1 started")
thread1.start()

print("Thread 2 started")
thread2.start()


# Wait for the threads to finish before continuing with the rest of the code
thread1.join()
thread2.join()

print("Main program continues execution")

"""
Explanation:
Python can't execute threads in parallel because of the Global Interpreter Lock (GIL).
The GIL is a mutex that protects access to Python objects, preventing multiple threads
from executing Python bytecodes at once. This lock is necessary mainly because CPython's
memory management is not thread-safe. Therefore, you can't use multiple threads to
increase the execution speed of CPU-bound tasks. However, you can use threads in Python
to perform I/O operations concurrently. Since I/O operations are usually orders of
magnitude slower than CPU operations, the performance gains of using threads are
significant, even when using multiple threads to execute I/O-bound tasks.

The code above creates two threads and starts them. The print_messages() function
prints the name of the current thread five times. The output shows that the threads
are executed in parallel. However, the threads are not executed concurrently. The
output shows that the threads are executed one after the other. This is because the
print() function is not thread-safe. Therefore, the interpreter locks the standard
output (stdout) before executing the print() function. This means that only one thread
can execute the print() function at once. The other thread has to wait until the
interpreter unlocks the stdout object.
"""
