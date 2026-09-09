import sys

qwe = 1
asd = '1231sww'
try:
  zxc = asd+qwe
  print('int')
except TypeError:
  print('str')
  exit()
  print('except_end')
finally:
   print('finally_end')

print('programm_end')