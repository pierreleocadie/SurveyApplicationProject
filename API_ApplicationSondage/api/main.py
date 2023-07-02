from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import admin, api_key, constituent, foods, stats, survey

app = FastAPI(
    title="API Documentation - Application de survey SAÉ S4",
    description="Documentation de l'API de l'application de survey SAÉ S4",
    version="1.0.0",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
    openapi_url="/api/v1/openapi.json",
    contact={
        "Developers": "LEOCADIE Pierre, HURST Charles, BAUMARD Jordan"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin.router)
app.include_router(api_key.router)
app.include_router(constituent.router)
app.include_router(foods.router)
app.include_router(stats.router)
app.include_router(survey.router)