from fastapi import APIRouter

from .service import get_vessel_count

router = APIRouter()


@router.get("/vessel/")
def read_vessel():
    vessel_count = get_vessel_count()
    print("vessel count", vessel_count)
    return vessel_count
