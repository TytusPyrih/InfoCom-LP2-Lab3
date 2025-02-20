import math
import requests
import argparse
import time

stepLength = 1

def travel(current_pos, dest_pos, SERVER_URL): 

    dx = dest_pos[0] - current_pos[0]
    dy = dest_pos[1] - current_pos[1]
    steps = 100
    oneStepX = dx/steps
    oneStepY = dy/steps
    drone_coords = current_pos
    for i in range(steps + 1):
        current_pos = (current_pos[0] + oneStepX, current_pos[1] + oneStepY)
        drone_coords = current_pos
        with requests.Session() as session:
            drone_location = {'longitude': drone_coords[0],
                            'latitude': drone_coords[1]
                        }
            resp = session.post(SERVER_URL, json=drone_location)
        time.sleep(0.01)


#Write you own function that moves the dron from one place to another 
#the function returns the drone's current location while moving
#====================================================================================================
"""def your_function(current_coords, to_coords, stepInXMovement,stepInYMovement):
    
    longitude = current_coords[0]
    latitude = current_coords[1] #set new cordinated for the drone
    
    lengthXLeft = current_coords[0] - to_coords[0] #to se the length left to go
    lengthYLeft = current_coords[1] - to_coords[1]
    if((lengthXLeft > stepLength or lengthXLeft < -stepLength) and (lengthYLeft > stepLength or lengthYLeft < -stepLength)): #check to se if drone is close to the point
        longitude += stepInXMovement #add the steps
        latitude += stepInYMovement
    else: #when almost there go to the location
        longitude = to_coords[0]
        latitude = to_coords[1]
    time.sleep(1)
    

    return (longitude, latitude)"""
#====================================================================================================


def run(current_coords, from_coords, to_coords, SERVER_URL):
    # Compmelete the while loop:
    # 1. Change the loop condition so that it stops sending location to the data base when the drone arrives the to_address
    # 2. Plan a path with your own function, so that the drone moves from [current_address] to [from_address], and the from [from_address] to [to_address]. 
    # 3. While moving, the drone keeps sending it's location to the database.
    #====================================================================================================
    travel(current_coords, from_coords, SERVER_URL)
    travel(from_coords, to_coords, SERVER_URL)

    """
    hypotenuseTofrom_cords = math.sqrt((to_coords[0] - current_coords[0])**2 +  (to_coords[1] - current_coords[1])**2)
     #used to calculate the movement in y and x to take 1 unit steps
    StepXfrom_coords = stepLength * ((from_coords[0]- current_coords[0])/hypotenuseTofrom_cords)
    stepYfrom_coords = stepLength * ((from_coords[1] - current_coords[1])/hypotenuseTofrom_cords)
    totalStepsFrom = int(hypotenuseTofrom_cords/StepXfrom_coords) + 1

    hypotenuse = math.sqrt((from_coords[0] - to_coords[0])**2 + (from_coords[1] - to_coords[1])**2)
    stepInXMovement = float(stepLength *(to_coords[0]- from_coords[0]/hypotenuse))       #using the sin = a/c where sin is the same in both triangles and one c = 1
    stepInYMovement = float(stepLength *(to_coords[1]- from_coords[1]/hypotenuse))       # same thing as above but with cos
    totalStepsTo = int(hypotenuse/stepInXMovement) +  1

    hasNotArrivedAtfrom_coords = True
    hasNotArrivedAtto_coords = True
    notArrived = True

    amountOfStepsFrom = 0
    amountOfStepsTo = 0
    while notArrived:
        while hasNotArrivedAtfrom_coords:
            drone_coords = your_function(current_coords, from_coords,StepXfrom_coords,stepYfrom_coords)
            with requests.Session() as session:
                drone_location = {'longitude': drone_coords[0],
                                'latitude': drone_coords[1]
                            }
                resp = session.post(SERVER_URL, json=drone_location)
            current_coords = drone_coords
            if(amountOfStepsFrom == totalStepsFrom):
                hasNotArrivedAtfrom_coords = False
    
        while hasNotArrivedAtto_coords:
            drone_coords = your_function(current_coords, from_coords,stepInXMovement,stepInYMovement)
            with requests.Session() as session:
                drone_location = {'longitude': drone_coords[0],
                                'latitude': drone_coords[1]
                            }
                resp = session.post(SERVER_URL, json=drone_location)
            current_coords = drone_coords
            if(totalStepsTo == amountOfStepsTo):
                hasNotArrivedAtto_coords = False"""
            
                
  #====================================================================================================

   
if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"

    parser = argparse.ArgumentParser()
    parser.add_argument("--clong", help='current longitude of drone location' ,type=float)
    parser.add_argument("--clat", help='current latitude of drone location',type=float)
    parser.add_argument("--flong", help='longitude of input [from address]',type=float)
    parser.add_argument("--flat", help='latitude of input [from address]' ,type=float)
    parser.add_argument("--tlong", help ='longitude of input [to address]' ,type=float)
    parser.add_argument("--tlat", help ='latitude of input [to address]' ,type=float)
    args = parser.parse_args()

    current_coords = (args.clong, args.clat)
    from_coords = (args.flong, args.flat)
    to_coords = (args.tlong, args.tlat)

    print(current_coords)
    print(from_coords)
    print(to_coords)

    run(current_coords, from_coords, to_coords, SERVER_URL)
