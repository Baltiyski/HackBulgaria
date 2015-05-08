def forecast(days):
    rain = 0;
    snow = 0;
    sunshine = 0;

    for day in days:
        if(day == "rain"):
            rain += 1;
        elif(day == "snow"):
            snow += 1;
        elif(day == "sunshine"):
            sunshine += 1;

    print(rain);
    print(snow);
    print(sunshine);

    if(rain > sunshine and rain > snow):
        return "rain";
    elif(sunshine > rain and sunshine > snow):
        return 'sunshine';
    elif(snow > rain and snow > sunshine):
        return 'snow';
    elif(snow == rain == sunshine):
        return days[len(days) - 1];
    elif(snow == rain and snow > sunshine and rain > sunshine):
        return 'sunshine';
    elif(snow == sunshine and snow > rain and sunshine > rain):
        return 'rain';
    elif(sunshine == rain and sunshine > snow and rain > snow):
        return 'snow';

print(forecast(["rain", "rain", "snow", "snow", "sunshine", "sunshine"]));
