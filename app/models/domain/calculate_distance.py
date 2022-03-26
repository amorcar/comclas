from math import (
    radians,
    sin,
    cos,
    atan2,
    sqrt,
    acos,
    hypot
)

C_EARTH = C_EARTH = 6371000.0
async def get_distance_between_positions_haversine(
        first_lat_deg: float,
        first_lon_deg: float,
        second_lat_deg: float,
        second_lon_deg: float
    ) -> float:
    '''
    Returns the absolute distance (in meters) between the two
    (lat, lon) points given using the Haversine Formula.

    This function expects the input parameters in decimal format:
    28.071988, -15.457261
    '''

    lat_1 = radians(first_lat_deg)
    lon_1 = radians(first_lon_deg)
    lat_2 = radians(second_lat_deg)
    lon_2 = radians(second_lon_deg)

    delta_lon = lon_2 - lon_1
    delta_lat = lat_2 - lat_1

    # Haversine Formula
    a = sin(delta_lat / 2.0) * sin(delta_lat / 2.0) + sin(delta_lon / 2.0)\
            * sin(delta_lon / 2.0) * cos(lat_1) * cos(lat_2)

    c = atan2(sqrt(a), sqrt(1.0 - a))
    d = C_EARTH * 2 * c

    return d

async def get_distance_between_positions_law_cosines(
        first_lat_deg: float,
        first_lon_deg: float,
        second_lat_deg: float,
        second_lon_deg: float
    ) -> float:

    '''
    Returns the absolute distance (in meters) between the two
    (lat, lon) points given using the Law of Cosines Formula.

    This function expects the input parameters in the format:
    28.071988, -15.457261
    '''

    lat_1 = radians(first_lat_deg)
    lon_1 = radians(first_lon_deg)
    lat_2 = radians(second_lat_deg)
    lon_2 = radians(second_lon_deg)

    delta_lon = lon_2 - lon_1

    # Spherical Law of Cosines
    d = acos(sin(lat_1) * sin(lat_2) + cos(lat_1)\
            * cos(lat_2) * cos(delta_lon)) * C_EARTH

    return d

async def get_distance_between_positions_equirectangular(
        first_lat_deg: float,
        first_lon_deg: float,
        second_lat_deg: float,
        second_lon_deg: float
    ) -> float:
    '''
    Returns the absolute distance (in meters) between the two
    (lat, lon) points given using the equirectangular approximation.

    This function expects the input parameters in the format:
    28.071988, -15.457261
    '''

    lat_1 = radians(first_lat_deg)
    lon_1 = radians(first_lon_deg)
    lat_2 = radians(second_lat_deg)
    lon_2 = radians(second_lon_deg)

    delta_lon = lon_2 - lon_1
    delta_lat = lat_2 - lat_1

    # Equirectangular approximation
    y = delta_lon * cos(lat_2+lat_1/2)
    x = delta_lat
    d = hypot(x,y) * C_EARTH
    return d

