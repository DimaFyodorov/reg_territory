from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import Response, RedirectResponse, HTMLResponse

from api.schemas import RBParams, User

from api.dao import UserDAO

router = APIRouter(
    tags=["api"],
)

# Регистрация территории: 
# Проверить свободна ли территория:


# Изменение статуса территории (Запретка/Открытая):
# Передача территории:

# Удаление территории:
@router.post("/reg_user/")
def reg_user(user: User):
    


@router.post("/reg/")
def reg(xy1, xy2):
    pass

@router.get("/check/")
def reg(xy1, xy2):
    pass

@router.get("/check/user/{uuid}")
def reg():
    pass

@router.post("/set_status/")
def reg(terr_id, status):
    pass

@router.post("/transfer_territory/")
def reg(terr_id, uuid):
    pass

@router.post("/removing_territory/")
def reg(terr_id):
    pass

@router.post("/change_territory/")
def reg(terr_id, xy1, xy2):
    pass

@router.get("log/")
def get_logs_by(request_body: RBParams = Depends()):
    pass