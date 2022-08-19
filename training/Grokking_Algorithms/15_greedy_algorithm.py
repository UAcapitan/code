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
    while needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        needed -= states_covered
        final_stations.add(best_station)

    return final_stations


if __name__ == "__main__":
    print(algorithm(states_needed, stations))