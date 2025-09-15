country = input("welcome to your travel partner, where would you like to go?(Type choice to see what country we support")
choice=print("here are the countries we currently support")
print("we currently support travel to America, Japan, Italy, Canada, Mexico, France, Germany, China and India")
country= input("where would you like to go?(Type the country name with a capital letter)")
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
   ItalyQuestion3 = input("do you speak Italian?")
  if ItalyQuestion3==("no"):
   print ("sorry but you will need a translator")
  elif ItalyQuestion3==("yes"):
   print ("thats all we need,you may travel to Italy")

elif country==("Canada"):
 CanadaQuestion1= input("do you have a passport?")
 if CanadaQuestion1==("no"):
  print ("sorry but to travel you need a passport")
 elif CanadaQuestion1==("yes"):
  CanadaQuestion2= input("do you have a visa?")
  if CanadaQuestion2==("no"):
   print ("sorry but you will need a visa")
  elif CanadaQuestion2==("yes"):
   print ("thats all we need,you may travel to Canada")

elif country==("Mexico"):
 MexicoQuestion1= input("do you have a passport?") 
 if MexicoQuestion1==("no"):
  print ("sorry but to travel you need a passport")
 elif MexicoQuestion1==("yes"):
  MexicoQuestion2= input("do you have a visa?")
  if MexicoQuestion2==("no"):
   print ("sorry but you will need a visa")
  elif MexicoQuestion2==("yes"):
   MexicoQuestion3 = input("do you speak Spanish?")
   if MexicoQuestion3==("no"):
    print ("sorry but you will need a translator")
   elif MexicoQuestion3==("yes"):
    print ("thats all we need,you may travel to Mexico")

elif country==("France"):
 FranceQuestion1= input("do you have a passport?")
 if FranceQuestion1==("no"):
  print ("sorry but to travel you need a passport")
 elif FranceQuestion1==("yes"):
  FranceQuestion2= input("do you have a visa?")
  if FranceQuestion2==("no"):
   print ("sorry but you will need a visa")
  elif FranceQuestion2==("yes"):
   FranceQuestion3 = input("do you speak French?")
   if FranceQuestion3==("no"):
    print ("sorry but you will need a translator")
   elif FranceQuestion3==("yes"):
    print ("thats all we need,you may travel to France")

elif country==("Germany"):
 GermanyQuestion1= input("do you have a passport?")
 if GermanyQuestion1==("no"):
  print ("sorry but to travel you need a passport")
 elif GermanyQuestion1==("yes"):
  GermanyQuestion2= input("do you have a visa?")
  if GermanyQuestion2==("no"):
   print ("sorry but you will need a visa")
  elif GermanyQuestion2==("yes"):
   GermanyQuestion3 = input("do you speak German?")
   if GermanyQuestion3==("no"):
    print ("sorry but you will need a translator")
   elif GermanyQuestion3==("yes"):
    print ("thats all we need,you may travel to Germany")

elif country==("China"):
 ChinaQuestion1= input("do you have a passport?")
 if ChinaQuestion1==("no"):
  print ("sorry but to travel you need a passport")
 elif ChinaQuestion1==("yes"):
  ChinaQuestion2= input("do you have a visa?")
  if ChinaQuestion2==("no"):
   print ("sorry but you will need a visa")
  elif ChinaQuestion2==("yes"):
   ChinaQuestion3 = input("do you speak Chinese?")
   if ChinaQuestion3==("no"):
    print ("sorry but you will need a translator")
   elif ChinaQuestion3==("yes"):
    print ("thats all we need,you may travel to China")

elif country==("India"):
 IndiaQuestion1= input("do you have a passport?")
 if IndiaQuestion1==("no"):
  print ("sorry but to travel you need a passport")
 elif IndiaQuestion1==("yes"):
  IndiaQuestion2= input("do you have a visa?")
  if IndiaQuestion2==("no"):
   print ("sorry but you will need a visa")
  elif IndiaQuestion2==("yes"):
   IndiaQuestion3 = input("do you speak hindi?")
   if IndiaQuestion3==("no"):
    print ("sorry but you will need a translator")
   elif IndiaQuestion3==("yes"):
    print ("thats all we need,you may travel to India")
else:
 print("sorry but we do not support some countries yet")

