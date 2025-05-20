from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import junctions, professions, riders, admin

app = FastAPI(title="Rider Connect API")

# Enable CORS for Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(junctions.router, prefix="/junctions", tags=["Junctions"])
app.include_router(professions.router, prefix="/professions", tags=["Professions"])
app.include_router(riders.router, prefix="/riders", tags=["Riders"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
async def root():
    return {"message": "Welcome to Rider Connect API"}