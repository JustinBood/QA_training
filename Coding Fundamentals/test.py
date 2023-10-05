def count(sequence, item):
  sum = 0
  for n in sequence:
    if n == item:
      sum += 1
  return sum

def test_count_int():
  assert count([1,2,3,4,1,1,5,1,1],1) == 5

def test_count_str():
  assert count(["Audi","BMW","Mercedes","Audi","Lamborghini","Porsche"],"Audi") == 2 

#we're using pytest in the terminal to test our code