import fastapi

router=fastapi.APIRouter()

@router.get('/api/mul')
def mul(x:int,y:int):
    val=x*y
    return{'multiplication result':val}