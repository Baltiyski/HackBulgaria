def winter_is_coming(seasons):  
    counter = 0;

    for season in seasons:
        if(season == "winter"):
            counter = 0;
        else:
            counter += 1;

    return counter >= 5;


print(winter_is_coming(["winter", "summer", "summer", "summer", "spring", "srping"]));

