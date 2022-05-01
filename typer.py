def print_return_type(func):
  # Define wrapper() the decorated function
  def wrapper(*args, **kwargs):
    # Call the function being decorated
    result = func(*args, **kwargs)
    print('{}() returned type {}'.format(
      func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper
  
@print_return_type
def what_is(value):
  return value
  
print(what_is(41.5))
print(what_is([1, 2, 3]))
print(what_is({'a': 13}))
print(what_is('blabla'))