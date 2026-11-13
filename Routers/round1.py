
from fastapi import APIRouter, HTTPException
from Game.game_logic import submit_round1
from session_store import sessions

router = APIRouter()


@router.post("/round1/submit/{code}")
def submit_answer(code: str, crew_id: str, choice: str, reason_id: str):

    if code not in sessions:
        raise HTTPException(status_code=404, detail="Session not found!")

    session = sessions[code]

    try:
        submit_round1(session, crew_id, choice, reason_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return {
        "message": "Answer submitted successfully!",
        "submission": session["r1"]["submissions"][crew_id]
    }
