def returns(return_type):
  # define decorator
  def decorator(func):
    def wrapper(*args,**kwargs):
      #wrap the decorator
      result = func(return_type)
      assert type(result) == return_type
      return result
    return wrapper
  return decorator
  
@returns(dict)
def whattype(value):
  return value

try:
  print(whattype((5,5,5)))
except AssertionError:
  print('whattype() did not return a dict!')