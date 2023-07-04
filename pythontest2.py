def add(*args):
  var=0
  for i in args:
    var+=i
  return var

def sub(*args):
  var=0
  for i in args:
    var-=i
  return var

def prod(*args):
  var=1
  for i in args:
    var*=i
  return var

print('The square of the given output is ',add(sub(prod(4,5),12,4),6,10)**2)


  
