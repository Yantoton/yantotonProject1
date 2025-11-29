traffic_light = input("Enter tha traffic light:")
traffic_signal =int(traffic_light)

if traffic_signal <= 1:
    print("Now is \'Green Signal\' Please Go!!!!")
elif traffic_signal <= 2:
    print("Now is \'Yellow Signal\' Please Wait  !!!!")
else:
    print("Now is \'Red Signal\' Please Stop!!!!")
