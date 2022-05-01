#This can be use for any codes, but mostly decoraters for function.
def counter(func):
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return wrapper.count
  wrapper.count = 0
  # Return the new decorated function
  return wrapper


# This is example for using
@counter
def asd():
    print('blablabla')

asd()
asd()
asd()

print('You talking nonsenses {} times a day.'.format(asd.count))