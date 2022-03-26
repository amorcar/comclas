from datetime import datetime

def get_current_UTC() -> float:
    return datetime.utcnow().timestamp()