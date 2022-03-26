from typing import Callable


async def get_distance_response(method: Callable, **kwargs) -> dict:
    return {
        'meters' : await method(**kwargs)
    }
