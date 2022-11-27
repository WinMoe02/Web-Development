signals=[".",
         "Weather warning: there is a storm approaching",
         "~",
         "Helicopter arriving McMurdo station 10:00 Tuesday",
         "**",
         "First",
         "**",
         "First aid kit needed at far camp",
         "*&_)*&^&%^$~၉:~",
         "Food delivery drop will be dalayed by 48 hours",
         "Repairs needed at the observation platform",
         "Urgent - update all anti-virus systems",
         "Please re-send meteorological data",
         "234724u2u23u888",
         "..",
         "asjdha## djhaidj# ddjiadj#",
         "Medical officer requested at main base",
         " %"]

good_signal=[]
stop=len(signals)
for i in range(stop):
    print(signals[i])
    response=input("is it good/bad, type y or n :")
    if response=='y':
        good_signal.append(signals[i])
print("good signals are: ",good_signal)
