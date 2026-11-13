ROUND1_STEPS = [
    "briefing",
    "investigate",
    "submit",
    "share",
    "decide",
    "reveal",
    "debrief"
]

ROUND2_STEPS = [
    "alert",
    "investigate",
    "plan",
    "dayResult",
    "day2Alert",
    "plan",
    "dayResult",
    "result",
    "debrief"
]

ROUND3_STEPS = [
    "alert",
    "rescuePlan",
    "rescue",
    "shelterAlert",
    "shelterBuild",
    "shelterResults",
    "debrief"
]

def get_round_steps(round_number):
    if round_number == 1:
        return ROUND1_STEPS

    elif round_number == 2:
        return ROUND2_STEPS

    elif round_number == 3:
        return ROUND3_STEPS

    return []