country = input("welcome to your travel partner, where would you like to go?")
if country==("America"):
 AmericaQuestion1 = input("do you have a passport?")
 if AmericaQuestion1==("no"):
  print ("sorry but to travel you need a passport")
 elif AmericaQuestion1==("yes"):
  AmericaQuestion2 = input("do you have a U.S visa or an approved electronicsystem for travel authorization under the visa waiver program?")
  if AmericaQuestion2==("no"):
   print ("sorry but you need to have a U.S visa or an approved electronicsystem for travel authorization under the visa waiver program")
  elif AmericaQuestion2==("yes"):
   print ("thats all we need,you may travel to America")

elif country==("Japan"):
 JapanQuestion1= input("do you have a passport?")
 if JapanQuestion1==("no"):
  print ("sorry but to travel you need a passport")
 elif JapanQuestion1==("yes"):
  JapanQuestion2= input("are you able to speak japanese?")
  if JapanQuestion2==("no"):
   print ("sorry but you will need a translator")
  elif JapanQuestion2==("yes"):
   print ("thats all we need,you may travel to Japan")

elif country==("Italy"):
 ItalyQuestion1= input("do you have a passport?")
 if ItalyQuestion1==("no"):
  print ("sorry but to travel you need a passport")
 elif ItalyQuestion1==("yes"):
  ItalyQuestion2= input("do you have a visa?")
  if ItalyQuestion2==("no"):
   print ("sorry but you will need a visa")
  elif ItalyQuestion2==("yes"):
   print ("thats all we need,you may travel to Italy")