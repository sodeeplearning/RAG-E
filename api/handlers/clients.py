from fastapi import APIRouter

from models import StatusModel, CustomerModel
from status_messages import user_is_customer, not_admin, user_not_found
from utils.checking import is_admin

from bots_data import clients_database


router = APIRouter()


@router.post("/add_customer")
async def add_customer(body: CustomerModel) -> StatusModel:
    status = "success"

    if is_admin(body.admin_id):
        if body.user_id in clients_database:
            status = user_is_customer
        else:
            clients_database.append(body.user_id)
    else:
        status = not_admin

    return StatusModel(status=status)


@router.delete("/remove_customer")
async def remove_customer(body: CustomerModel) -> StatusModel:
    status = "success"
    if is_admin(body.admin_id):
        if body.user_id in clients_database:
            clients_database.remove(body.user_id)
        else:
            status = user_not_found
    else:
        status = not_admin

    return StatusModel(status=status)
