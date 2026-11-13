
from .round_steps import get_round_steps


def host_advance(session):

    if session["round"] == 1:

        if session["step"] == "lobby":
            if len(session["crews"]) < 2:
                raise ValueError("At least 2 crews are required!")

            session["step"] = "briefing"
            return session

        if session["step"] == "decide":
            if session["r1"]["final"] is None:
                raise ValueError("The host must set the final answer first!")

            session["step"] = "reveal"
            return session

        steps = get_round_steps(1)

        if session["step"] in steps:
            current_index = steps.index(session["step"])

            if current_index < len(steps) - 1:
                session["step"] = steps[current_index + 1]
            elif session["step"] == "debrief":
                session["step"] = "roundComplete"

        return session

    if session["round"] == 2:

        step = session["step"]
        day = session["r2"]["day"]

        if step == "dayResult":
            history = session["r2"]["history"]

            if not history or history[-1]["day"] != day:
                raise ValueError("Day result has not been calculated!")

            if not history[-1]["survived"]:
                session["step"] = "result"
                return session

            if day == 1:
                session["r2"]["day"] = 2
                session["step"] = "day2Alert"
                return session

            if day == 2:
                session["step"] = "result"
                return session

        steps = get_round_steps(2)

        if step == "alert":
            session["step"] = "investigate"

        elif step == "investigate":
            session["step"] = "plan"

        elif step == "day2Alert":
            session["step"] = "plan"

        elif step == "result":
            session["step"] = "debrief"

        elif step == "debrief":
            session["step"] = "roundComplete"

        return session

    return session



def host_back(session):

    if session["round"] == 1:

        if session["step"] == "lobby":
            return session

        if session["step"] == "roundComplete":
            session["step"] = "debrief"
            return session

        if session["step"] == "reveal":
            session["step"] = "decide"
            return session

        if session["step"] == "decide":
            if session["r1"]["final"] is not None:
                raise ValueError("The final decision is already locked!")

            session["step"] = "share"
            return session

        steps = get_round_steps(1)
        current_index = steps.index(session["step"])

        if current_index > 0:
            session["step"] = steps[current_index - 1]

        return session

    if session["round"] == 2:

        step = session["step"]

        if step == "lobby":
            return session

        if step == "roundComplete":
            session["step"] = "debrief"
            return session

        if step == "debrief":
            session["step"] = "result"
            return session

        if step == "result":
            session["step"] = "dayResult"
            return session

        if step == "dayResult":
            if session["r2"]["day"] == 2:
                session["step"] = "plan"
            else:
                session["step"] = "plan"

            return session

        if step == "day2Alert":
            session["r2"]["day"] = 1
            session["step"] = "dayResult"
            return session

        if step == "plan":
            if session["r2"]["day"] == 2:
                session["step"] = "day2Alert"
            else:
                session["step"] = "investigate"

            return session

        if step == "investigate":
            session["step"] = "alert"
            return session

        return session

    return session
