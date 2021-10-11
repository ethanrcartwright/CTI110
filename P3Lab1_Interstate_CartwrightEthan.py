
#input by user
highway_number = int(input())#inputofnumber
highway_direction = (highway_number % 2)#calculates if number is odd or even 
auxillary_serving = abs(highway_number) % 100 # gives last two numbers of aux. interstate highways



#calculating interstate highway status and direction.
if (highway_number <= 99) and (highway_number > 0):
    print('I-',highway_number,'is primary,',end='')
    if highway_direction == 0:
        print(' going east/west.')
    else:
        print(' going north/south.')
#calculating interstate highway status and direction 
elif highway_number > 99:
    if auxillary_serving == 00:
        print(highway_number,'is not a valid interstate highway number.')
    if auxillary_serving != 00:
        print('I-',highway_number, 'is auxiliary, serving I-', auxillary_serving,',', end='')
        if highway_direction == 0:
            print( ' going east/west.')
        else:
            print(' going north/south.')
#if highway_number does not fit in with numbering scheme
else:
    print('I-', highway_number , 'is not a valid interstate highway number.')
    

    

    

        

    

  
    
    
    
