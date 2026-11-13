
def calculate_rescue_result(rover_explorer):
    if rover_explorer not in [1, 2, 3]:
        raise ValueError("Choose Explorer 1, 2 or 3!")

    walking_times = {
        1: 4,
        2: 7,
        3: 11
    }

    rover_times = {
        1: 3,
        2: 5,
        3: 6
    }

    results = {}

    for explorer in [1, 2, 3]:
        if explorer == rover_explorer:
            time = rover_times[explorer]
        else:
            time = walking_times[explorer]

        results[explorer] = {
            "time": time,
            "safe": time <= 8
        }

    return {
        "results": results
    }


def calculate_shelter_score(placements):
    if len(placements) != 3:
        raise ValueError("Each crew must place exactly 3 objects!")

    inventory = {
        "thick_water_bag": 1,
        "wide_water_bag": 2,
        "packed_food_bag": 1,
        "wide_clothing_bag": 1,
        "empty_storage_bag": 1
    }

    area_layers = {
        "A": 0,
        "B": 0,
        "C": 0
    }

    for placement in placements:
        item = placement["item"]
        area = placement["area"]

        if item not in inventory or inventory[item] <= 0:
            raise ValueError("Invalid or unavailable item!")

        inventory[item] -= 1

        if item in ["thick_water_bag", "packed_food_bag"]:
            if area not in ["A", "B", "C"]:
                raise ValueError("Invalid area!")

            area_layers[area] += 2

        elif item == "empty_storage_bag":
            if area not in ["A", "B", "C"]:
                raise ValueError("Invalid area!")

        elif item in ["wide_water_bag", "wide_clothing_bag"]:
            if area == "A":
                area_layers["A"] += 1
                area_layers["B"] += 1
            elif area == "B":
                area_layers["B"] += 1
                area_layers["C"] += 1
            else:
                raise ValueError("Wide items must cover A+B or B+C!")

    area_points = {}

    for area, layers in area_layers.items():
        area_points[area] = min(layers, 2)

    total_score = sum(area_points.values())

    return {
        "layers": area_layers,
        "areaPoints": area_points,
        "totalScore": total_score
    }


def save_rescue_result(session, rover_explorer):
    if session["round"] != 3 or session["step"] != "rescue":
        raise ValueError("Rescue result cannot be saved now!")

    session["r3"]["rover"] = rover_explorer
    return session


def save_shelter_result(session, crew_id, placements):
    if session["round"] != 3 or session["step"] != "shelterBuild":
        raise ValueError("Shelter result cannot be saved now!")

    crew_exists = any(
        crew["id"] == crew_id for crew in session["crews"]
    )

    if not crew_exists:
        raise ValueError("Crew not found!")

    result = calculate_shelter_score(placements)

    session["r3"]["shelters"][crew_id] = placements
    session["r3"]["shelterScores"][crew_id] = result["totalScore"]

    return session
