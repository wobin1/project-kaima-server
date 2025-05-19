from fastapi import APIRouter, HTTPException
from app.core.database import get_db_connection

router = APIRouter()

@router.get("/{junction_id}/{profession_id}", response_model=list[dict])
async def get_riders(junction_id: int, profession_id: int):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT p.id, p.name, p.phone_number
                FROM professionals p
                JOIN junction_professionals jp ON p.id = jp.professional_id
                WHERE jp.junction_id = %s AND jp.profession_id = %s
                ORDER BY p.name
            """, (junction_id, profession_id))
            riders = cur.fetchall()
            if not riders:
                raise HTTPException(status_code=404, detail="No riders found for this junction and profession")
            return riders
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()