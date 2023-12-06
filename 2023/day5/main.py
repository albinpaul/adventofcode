def getItemInRange(item, ranges):
    found = False
    for itemRange in ranges:
        destItem = itemRange[0]
        sourceItem = itemRange[1]
        length = itemRange[2]
        if sourceItem <= item and item <= sourceItem + length:
            found = True
            yield destItem + item - sourceItem
    if not found:
        yield item

with open("input.txt") as f:
    ans = 0
    lines = f.read().split("\n")
    seeds = []
    seedToSoil = False

    seedsToSoilRanges = list()
    soilToFertilizerRanges = list()
    fertilizerToWaterRanges = list()
    waterToLightRanges = list()
    lightToTemperatureRanges = list()
    temperatureToHumidityRanges = list()
    humidityToLocationRanges = list()

    for i, line in enumerate(lines):
        if line.startswith("seeds"):
            seeds = line.split(':')[1].split()
            seeds = [int(seed) for seed in seeds]
            print(seeds)
        elif line.startswith("seed-to-soil map"):
            seedToSoil = True
        elif line.startswith("humidity-to-location map"):
            humidityToLocation = True
        elif line.startswith("temperature-to-humidity map"):
            temperatureToHumidity = True
        elif line.startswith("light-to-temperature map"):
            lightToTemperature = True
        elif line.startswith("water-to-light map"):
            waterToLight = True
        elif line.startswith("fertilizer-to-water map"):
            fertilizerToWater = True
        elif line.startswith("soil-to-fertilizer map"):
            soilToFertilizer = True
        
        elif len(line) == 0:
            seedToSoil = False
            humidityToLocation = False
            temperatureToHumidity = False
            lightToTemperature = False
            waterToLight = False
            fertilizerToWater = False
            soilToFertilizer = False
        else:
            if seedToSoil:
                seedsToSoilRanges.append(
                    [int(item) for item in line.split()]
                )
            if humidityToLocation:
                humidityToLocationRanges.append(
                    [int(item) for item in line.split()]
                )
            if temperatureToHumidity:
                temperatureToHumidityRanges.append(
                    [int(item) for item in line.split()]
                )
            if lightToTemperature:
                lightToTemperatureRanges.append(
                    [int(item) for item in line.split()]
                )
            if waterToLight:
                waterToLightRanges.append(
                    [int(item) for item in line.split()]
                )
            if fertilizerToWater:
                fertilizerToWaterRanges.append(
                    [int(item) for item in line.split()]
                )
            if soilToFertilizer:
                soilToFertilizerRanges.append(
                    [int(item) for item in line.split()]
                )
    ans = 1<<40
    new_seeds = []
    for i in range(1, len(seeds), 2):
        for j in range(seeds[i]):
            new_seeds.append(seeds[i-1] + j)
    print(new_seeds)
    for seed in new_seeds:
        for soil in getItemInRange(seed, seedsToSoilRanges):
            for fertilizer in getItemInRange(soil, soilToFertilizerRanges):
                for water in getItemInRange(fertilizer, fertilizerToWaterRanges):
                    for light in getItemInRange(water, waterToLightRanges):
                        for temperature in getItemInRange(light, lightToTemperatureRanges):
                            for humidity in getItemInRange(temperature, temperatureToHumidityRanges):
                                for location in getItemInRange(humidity, humidityToLocationRanges):
                                    ans = min(ans, location)
    print(ans)