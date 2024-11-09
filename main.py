time=input("Enter the time: ")
time=int(time)
print("1.Taxi")
print("2.Minibus")
print("3.Commercial")
typeVehicle=input("Enter the type of vehicle: ")

cost=0

if typeVehicle=="1":
    if time==1:
        cost=10
    else:
        cost=time*(10*1.20)
elif typeVehicle=="2":
    if time==1:
        cost=15
    else:
        cost=time*(15*1.25)
else:
    if time==1:
        cost=20
    else:
        cost=time*(20*1.30)
print(cost)