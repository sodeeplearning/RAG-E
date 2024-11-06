from fastapi import APIRouter

from . import checking
from . import prompting
from . import transfering

router = APIRouter()

router.include_router(checking.router)
router.include_router(prompting.router)
router.include_router(transfering.router)
