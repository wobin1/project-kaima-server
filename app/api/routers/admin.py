from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.database import get_db_connection

router = APIRouter()

# Pydantic models for request validation
class JunctionCreate(BaseModel):
    name: str

class ProfessionCreate(BaseModel):
    name: str

class ProfessionalCreate(BaseModel):
    name: str
    phone_number: str

class JunctionProfessionalCreate(BaseModel):
    junction_id: int
    profession_id: int
    professional_id: int

# Junction CRUD
@router.get("/junctions", response_model=list[dict])
async def get_junctions():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM junctions ORDER BY name")
            junctions = cur.fetchall()
        return junctions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

@router.post("/junctions", response_model=dict)
async def create_junction(junction: JunctionCreate):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO junctions (name) VALUES (%s) RETURNING id, name",
                (junction.name,)
            )
            conn.commit()
            return cur.fetchone()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating junction: {str(e)}")
    finally:
        conn.close()

@router.put("/junctions/{junction_id}", response_model=dict)
async def update_junction(junction_id: int, junction: JunctionCreate):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE junctions SET name = %s WHERE id = %s RETURNING id, name",
                (junction.name, junction_id)
            )
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Junction not found")
            conn.commit()
            cur.execute("SELECT id, name FROM junctions WHERE id = %s", (junction_id,))
            return cur.fetchone()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating junction: {str(e)}")
    finally:
        conn.close()

@router.delete("/junctions/{junction_id}")
async def delete_junction(junction_id: int):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM junctions WHERE id = %s", (junction_id,))
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Junction not found")
            conn.commit()
            return {"message": "Junction deleted"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Error deleting junction: {str(e)}")
    finally:
        conn.close()

# Profession CRUD
@router.get("/professions", response_model=list[dict])
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

@router.post("/professions", response_model=dict)
async def create_profession(profession: ProfessionCreate):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO professions (name) VALUES (%s) RETURNING id, name",
                (profession.name,)
            )
            conn.commit()
            return cur.fetchone()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating profession: {str(e)}")
    finally:
        conn.close()

@router.put("/professions/{profession_id}", response_model=dict)
async def update_profession(profession_id: int, profession: ProfessionCreate):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE professions SET name = %s WHERE id = %s RETURNING id, name",
                (profession.name, profession_id)
            )
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Profession not found")
            conn.commit()
            return cur.fetchone()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating profession: {str(e)}")
    finally:
        conn.close()

@router.delete("/professions/{profession_id}")
async def delete_profession(profession_id: int):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM professions WHERE id = %s", (profession_id,))
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Profession not found")
            conn.commit()
            return {"message": "Profession deleted"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Error deleting profession: {str(e)}")
    finally:
        conn.close()

# Professional CRUD
@router.get("/professionals", response_model=list[dict])
async def get_professionals():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, phone_number FROM professionals ORDER BY name")
            professionals = cur.fetchall()
        return professionals
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

@router.post("/professionals", response_model=dict)
async def create_professional(professional: ProfessionalCreate):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO professionals (name, phone_number) VALUES (%s, %s) RETURNING id, name, phone_number",
                (professional.name, professional.phone_number)
            )
            conn.commit()
            return cur.fetchone()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating professional: {str(e)}")
    finally:
        conn.close()

@router.put("/professionals/{professional_id}", response_model=dict)
async def update_professional(professional_id: int, professional: ProfessionalCreate):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE professionals SET name = %s, phone_number = %s WHERE id = %s RETURNING id, name, phone_number",
                (professional.name, professional.phone_number, professional_id)
            )
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Professional not found")
            conn.commit()
            return cur.fetchone()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Error updating professional: {str(e)}")
    finally:
        conn.close()

@router.delete("/professionals/{professional_id}")
async def delete_professional(professional_id: int):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM professionals WHERE id = %s", (professional_id,))
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Professional not found")
            conn.commit()
            return {"message": "Professional deleted"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Error deleting professional: {str(e)}")
    finally:
        conn.close()

# Junction-Professional Association
@router.post("/junction-professionals", response_model=dict)
async def create_junction_professional(assoc: JunctionProfessionalCreate):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO junction_professionals (junction_id, profession_id, professional_id) VALUES (%s, %s, %s) RETURNING id, junction_id, profession_id, professional_id",
                (assoc.junction_id, assoc.profession_id, assoc.professional_id)
            )
            conn.commit()
            return cur.fetchone()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating association: {str(e)}")
    finally:
        conn.close()

@router.delete("/junction-professionals/{assoc_id}")
async def delete_junction_professional(assoc_id: int):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM junction_professionals WHERE id = %s", (assoc_id,))
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Association not found")
            conn.commit()
            return {"message": "Association deleted"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Error deleting association: {str(e)}")
    finally:
        conn.close()

@router.get("/junction-professionals", response_model=list[dict])
async def get_junction_professionals():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT jp.id, j.name as junction_name, pr.name as profession_name, p.name as professional_name, p.phone_number
                FROM junction_professionals jp
                JOIN junctions j ON jp.junction_id = j.id
                JOIN professions pr ON jp.profession_id = pr.id
                JOIN professionals p ON jp.professional_id = p.id
                ORDER BY j.name, pr.name, p.name
            """)
            associations = cur.fetchall()
        return associations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()