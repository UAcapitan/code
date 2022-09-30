states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"}
}

def algorithm(needed, stations):
    final_stations = set()
    
    for station, states in stations.items():
        if len(needed & states) > 0:
            needed -= states
            final_stations.add(station)

    return final_stations


if __name__ == "__main__":
    print(algorithm(states_needed, stations))