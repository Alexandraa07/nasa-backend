import secrets

CHARACTERS = "ABCDEFGHJKLMNPQRSTUVWXYZ" # characters for the random code
sessions = {} # here we keep the game's sessions

def generate_code():
    while True:
        letters = []
        for i in range(4):
            letters.append(secrets.choice(CHARACTERS))

        code = "".join(letters)
        if code not in sessions:
            return code


def create_session_host():
    code = generate_code()

    sessions[code] = {
        "round": 1,
        "step": "lobby",
        "classScore": 0,
        "crews": [],
        "hostToken": secrets.token_urlsafe(16),
        "timer": {
            "endsAt": None
        },

        "r1": {
            "submissions": {},
            "votes": {},
            "final": None,
            "hintsReleased": []
        },

        "r2": {
            "battery": 8,
            "day": 1,
            "levels": {},
            "history": []
        },

        "r3": {
            "roles": {},
            "rover": None,
            "shelters": {},
            "shelterScores": {}
        }
    }

    return {
        "code": code,
        "hostToken": sessions[code]["hostToken"]
    }
