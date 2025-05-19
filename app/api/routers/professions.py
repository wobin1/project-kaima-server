from fastapi import APIRouter, HTTPException
from app.core.database import get_db_connection

router = APIRouter()

@router.get("/", response_model=list[dict])
async def get_professions():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM professions ORDER BY name")
            professions = cur.fetchall()
        return professions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()