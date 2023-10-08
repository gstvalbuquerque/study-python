import threading
from time import sleep

# Shared variable
counter = 0

# Lock to control access to the shared variable
lock = threading.Lock()

# Function to be executed in a thread


def increment_variable(value: int, thread_name: str):
    global counter
    print(f"{thread_name} started")

    # Acquire the lock before modifying the shared variable
    with lock:
        local_counter = counter
        local_counter += value

        sleep(0.1)

        counter = local_counter

    # Release the lock after modifying the shared variable
    print(f"{thread_name}: ", counter)


# Create two threads
thread1 = threading.Thread(target=increment_variable, args=(10, "Thread 1"))
thread2 = threading.Thread(target=increment_variable, args=(20, "Thread 2"))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish before continuing with the rest of the code
thread1.join()
thread2.join()

print(f'The final counter is {counter}')

"""
Explanation:
This python code demonstrates how to use a lock to control access to a shared variable.
The increment_variable() function increments the shared variable counter by a value
passed as an argument. The function also prints the name of the thread that is executing
the function. The output shows that the threads are executed concurrently. However, the
threads are not executed in parallel. The output shows that the threads are executed one
after the other. This is because the increment_variable() function acquires the lock
before modifying the shared variable. Therefore, only one thread can modify the shared
variable at once. The other thread has to wait until the thread that acquired the lock
releases it. This ensures that the shared variable is not modified by multiple threads
at once. The output shows that the final value of the counter is 30, which is the sum of
the values passed to the two threads.

Note: The with statement is used to acquire and release the lock. This ensures that the
lock is released even if an exception occurs while the lock is acquired. This is
important because the lock is released only when the lock object is destroyed. If the
lock is not released, the other threads will be blocked forever. Therefore, it is
important to ensure that the lock is released even if an exception occurs while the lock
is acquired. The with statement ensures that the lock is released even if an exception
occurs while the lock is acquired. Therefore, it is recommended to use the with
statement to acquire and release locks.
"""
