def buildingsSeen(buildings):
    if(len(buildings) == 0):
        return 0;
    
    seen = 1;
    count = buildings[0];

    for building in buildings:
        if(building > count):
            seen += 1;
            count = building;
            
    return seen;

howManyBuilding = input("Enter how many buildings do you wish - ");
howManyBuilding = int(howManyBuilding);

buildings = [];
index = 1;

while(index <= howManyBuilding):
    floor = input("Input how many floor's yu wish for " +str(index)+ " building - ");
    floor = int(floor);
    buildings = buildings + [floor]
    index += 1;

print("Seen buildings - " + str(buildingsSeen(buildings)));
