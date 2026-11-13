
def round2(number_of_teams: int, life_support: int, food: int, temperature: int, comms: int, battery: int):
    if number_of_teams < 2 or number_of_teams > 4:
        raise ValueError("There have to be a minimum of 2 and a maximum of 4 teams!")

    if life_support not in [0, 1, 2]:
        raise ValueError("Life Support must be 0, 1 or 2!")

    if food not in [0, 1, 2]:
        raise ValueError("Food must be 0, 1 or 2!")

    if temperature not in [0, 1, 2]:
        raise ValueError("Temperature must be 0, 1 or 2!")

    if comms not in [0, 1, 2]:
        raise ValueError("Communications must be 0, 1 or 2!")

    total_energy = life_support + food + temperature + comms

    if total_energy > battery:
        raise ValueError("Not enough battery energy!")

    return {
        "life_support": life_support,
        "food": food,
        "temperature": temperature,
        "comms": comms,
        "total_energy": total_energy,
        "remaining_energy": battery - total_energy
    }


def calculate_day_result(life_support: int, temperature: int):
    survived = life_support >= 1 and temperature >= 1
    return {"survived": survived}


def calculate_round2_score(day1_survived: bool, day2_survived: bool):
    if day1_survived and day2_survived:
        return 3
    elif day1_survived:
        return 1
    return 0


def update_class_score(session, round_score):
    session["classScore"] += round_score
    return session


def save_day_result(session, day, life_support, temperature, total_energy):
    if day not in [1, 2]:
        raise ValueError("Day must be 1 or 2!")

    result = calculate_day_result(life_support, temperature)
    update_battery(session, total_energy)

    session["r2"]["history"].append({
        "day": day,
        "survived": result["survived"],
        "energy_used": total_energy
    })

    return session


def end_round2(session):
    day1 = None
    day2 = None

    for result in session["r2"]["history"]:
        if result["day"] == 1:
            day1 = result["survived"]
        elif result["day"] == 2:
            day2 = result["survived"]

    if day1 is None or day2 is None:
        raise ValueError("Both days must have results!")

    score = calculate_round2_score(day1, day2)
    session["r2"]["score"] = score
    update_class_score(session, score)

    return session


def update_battery(session, total_energy):
    if total_energy > session["r2"]["battery"]:
        raise ValueError("Not enough battery energy!")

    session["r2"]["battery"] -= total_energy
    return session
