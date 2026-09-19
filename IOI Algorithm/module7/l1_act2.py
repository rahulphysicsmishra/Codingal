# Search list and target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto" ]
target_city = "New York City"

#Linear Search Algorithm
def linear_search(search_list, target_value):
    matches = []
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            # If target value found in the list
            # add index in matches list
            matches.append(idx)

    # If the element is not in matches list
    # Raise an error
    if not matches:
        raise ValueError("{} is not in the list".format(target_value))
    # Otherwise return the matches list
    # with indexes where element is present
    else:
        return matches

#Function call
tour_stops = linear_search(tour_locations, target_city)
print("{} is present in following locations in the list: {}".format(target_city,tour_stops))