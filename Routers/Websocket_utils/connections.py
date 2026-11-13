
device_connections = {}
host_connections = {}

CREW_IDS = {"orion", "lyra", "vega", "draco"}


def get_device_crew(session, device_id):
    for crew in session["crews"]:
        if device_id in crew["devices"]:
            return crew

    return None
