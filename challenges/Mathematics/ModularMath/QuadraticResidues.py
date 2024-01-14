p = 29
ints = [14, 6, 11]
#for i in range(29):
#  print(pow(i,2,29))
#  if pow(i,2,29)==18:
#    print("i="+str(i))

for i in ints:
  for a in range(29):
    if pow(a,2,29)==i:
      print("a="+str(a))

