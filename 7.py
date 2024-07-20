import time
def log_time(func):
    def wrapper(*args, **kwargs):
        try:
            start_time = time.time()  # Record the start time
            result = func(*args, **kwargs)  # Execute the function and get result
            end_time = time.time()  # Record the end
            elapsed_time = end_time - start_time  # Calculate elapsed time
            print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds to execute")
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            raise e
    return wrapper
# Use the decorator on the function
@log_time
def expensive_task(n):
    return sum(i**2 for i in range(n))
try:
    # Testing the function with decorator
    result = expensive_task(1000000)
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")
