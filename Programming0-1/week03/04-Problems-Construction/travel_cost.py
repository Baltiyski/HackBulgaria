def travel_cost(travels):
    travelSum = 0;

    for travel in travels:

        if(travel >= 23):
            travelSum += 23;
        else:
            travelSum += travel * 1;

        if(travelSum >= 50):
            return 50;
    return travelSum;


travels = [23, 24, 2];

print(travel_cost(travels));
