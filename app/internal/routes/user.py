from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v1/users"
)


@router.get("/hello")
def user_hello():

    return {"hello": "world"}
