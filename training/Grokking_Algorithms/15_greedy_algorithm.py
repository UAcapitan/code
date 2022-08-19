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
        print('-'*7)
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            print(station, states)
            covered = needed & states
            print(covered)
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
                print(best_station, states_covered)

        needed -= states_covered
        final_stations.add(best_station)
        print(final_stations)

    return final_stations


if __name__ == "__main__":
    print(algorithm(states_needed, stations))