def drive(car_speed):
    if car_speed>200:
        print ('You are insane, man!!')
    elif car_speed>100:
        print ('Too fast!')
    elif car_speed>80 and car_speed<100:
        print ('You are passed the optimal speed for your car.')
    elif car_speed>70 and car_speed<80:
        print ('The optimal speed for your car.')
    else:
        print ('You are driving below the speed limit. Well Done!')
