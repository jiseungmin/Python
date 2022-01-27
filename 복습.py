def sayhello(name, age):
  if age < 18 :
    print("안녕, "+ name)
  elif age <= 20 and age >= 10:
   print("안녕하세요," + name)
  else:
   print("안녕하십니까," + name)

   sayhello("워니", 10)
   