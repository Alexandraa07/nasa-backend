
from Game.round1 import submit_round1, vote_round1, set_final_round1
from Game.game_logic import host_advance

session = {
    "round": 1,
    "step": "submit",
    "classScore": 0,
    "crews": [
        {"id": "orion"},
        {"id": "lyra"}
    ],
    "r1": {
        "submissions": {},
        "votes": {},
        "final": None,
        "score": None,
        "hintsReleased": []
    }
}

# Test 1: crew Orion submits an answer
submit_round1(session, "orion", "A", "reason_1")
assert session["r1"]["submissions"]["orion"]["choice"] == "A"

# Test 2: host advances to Share
host_advance(session)
assert session["step"] == "share"

# Test 3: host advances to Decide
host_advance(session)
assert session["step"] == "decide"

# Test 4: crew Lyra votes
vote_round1(session, "lyra", "C")
assert session["r1"]["votes"]["lyra"] == "C"

# Test 5: host sets final answer
set_final_round1(session, "A")
assert session["r1"]["score"] == 3
assert session["classScore"] == 3

# Test 6: host advances to Reveal
host_advance(session)
assert session["step"] == "reveal"

print("All Round 1 tests passed!")
