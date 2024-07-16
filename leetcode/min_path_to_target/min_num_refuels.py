class Solution:
    memo = {}
    target = -1
    stations = []

    def refuel_helper(self, rem_fuel, curr_station, no_refuels):
        if curr_station == -1:
            current_dist = 0
        else:
            current_dist = self.stations[curr_station][0]

        if (rem_fuel, curr_station) in self.memo:
            return self.memo[(rem_fuel, curr_station)]

        # if we can get to the target directly
        if self.target - current_dist <= rem_fuel:
            return no_refuels
        # if this is the final gas st., and we can't make it to the end...
        if curr_station == len(self.stations) - 1:
            return -1
        # if we can't even reach the closest gas st.
        if rem_fuel < self.stations[curr_station + 1][0] - current_dist:
            return -1

        # main case
        possible_refuels = []
        for i in range(curr_station + 1, len(self.stations)):
            rem_dist_to_station = self.stations[i][0] - current_dist

            if rem_fuel < rem_dist_to_station:
                # We can't reach any further stations
                break

            station_fuel = self.stations[i][1]
            new_rem_fuel = rem_fuel - rem_dist_to_station + station_fuel
            # We have to refuel at least once
            possible_refuels.append(self.refuel_helper(new_rem_fuel, i, no_refuels + 1))
            # Keep old remaining fuel for future iterations, to see how far we can make it

        # Return min. possible nr. stations visited, that isn't -1
        possible_refuels = sorted(possible_refuels)

        for ref in possible_refuels:
            if ref >= 0:
                self.memo[(rem_fuel, curr_station)] = ref
                return ref

        return -1

    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        self.memo = {}  # Reset for leetcode
        self.target = target
        # stations.insert(0, [0, startFuel])  # Insert a fake "fuel stop" at starting point
        self.stations = stations
        return self.refuel_helper(startFuel, -1, 0)


if __name__ == '__main__':
    sln = Solution()

    # print(sln.minRefuelStops(target = 1, startFuel = 1, stations = []))

    # print(sln.minRefuelStops(target = 100, startFuel = 1, stations = [[10,100]]))

    # print(sln.minRefuelStops(target=100, startFuel=50, stations=[[25, 25], [50, 50]]))

    # print(sln.minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))

    # print(sln.minRefuelStops(target=100, startFuel=25, stations=[[25,25],[50,25],[75,25]]))

    print(sln.minRefuelStops(target=1000, startFuel=299, stations=[[42,39],[132,236],[166,142],[434,7],[462,80],[518,103],[545,209],[656,104],[769,137],[811,67]]))
