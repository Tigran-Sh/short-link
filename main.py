from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.core.config import settings
from apps.core.utils import generate_api_prefix
from apps.link_management.routers import redirect_rout, link_routes

app = FastAPI(
    title=settings.APP_NAME,
    description='Service for generating short links',
    version='1.0.0',
    docs_url='/'
)

# origins = ["*"]
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"],
)

app.include_router(redirect_rout)
app.include_router(link_routes, prefix=generate_api_prefix('links'))
