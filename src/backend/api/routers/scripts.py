from fastapi import APIRouter, Depends, HTTPException
from services.script_service import ScriptService
from data import databese
from models.script import Script, ScriptCreate

router = APIRouter()


def get_service(db=Depends(databese.get_db)):
    return ScriptService(ScriptRepository(db))


@router.post("/scripts", response_model=Script)
async def create_script(
    script_data: ScriptCreate, service: ScriptService = Depends(get_service)
):
    return service.create_script(script_data)


@router.get("/scripts/{script_id}", response_model=Script)
async def get_script(script_id: str, service: ScriptService = Depends(get_service)):
    try:
        return service.get_script(script_id)
    except Exception as e:
        raise HTTPException(404, detail=str(e))
