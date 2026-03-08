"""
API Routes package - aggregates all sub-routers.
"""

from fastapi import APIRouter

from .endpoints import router as endpoints_router
from .prompts import router as prompts_router
from .spinning import router as spinning_router
from .intelligent_attack import router as attack_router
from .analytics import router as analytics_router
from .data_management import router as data_router
from .health import router as health_router
from .wizard import router as wizard_router
from .multi_turn import router as multi_turn_router
from .integrations import router as integrations_router
from .scraper import router as scraper_router

api_router = APIRouter()
api_router.include_router(wizard_router, prefix="/wizard", tags=["Wizard"])
api_router.include_router(endpoints_router, prefix="/endpoints", tags=["Endpoints"])
api_router.include_router(prompts_router, prefix="/prompts", tags=["Prompts"])
api_router.include_router(spinning_router, prefix="/spinning", tags=["Spinning"])
api_router.include_router(attack_router, prefix="/intelligent-attack", tags=["Intelligent Attack"])
api_router.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
api_router.include_router(data_router, prefix="/data", tags=["Data Management"])
api_router.include_router(health_router, tags=["Health"])
api_router.include_router(multi_turn_router, prefix="/multi-turn", tags=["Multi-Turn Attacks"])
api_router.include_router(integrations_router, prefix="/integrations", tags=["Integrations"])
api_router.include_router(scraper_router, prefix="/scraper", tags=["Document Agent"])
