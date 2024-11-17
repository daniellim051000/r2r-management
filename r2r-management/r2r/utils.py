from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError
from django.conf import settings

from datetime import datetime

from azure.storage.blob import BlobServiceClient
from django.core.cache import cache


def check_database():
    try:
        with connections["default"].cursor() as cursor:
            cursor.execute("SELECT 1")
            return "healthy"
    except Exception as e:
        return f"unhealthy: {str(e)}"


def check_azure_storage():
    if not settings.USE_AZURE:
        return "not configured"

    try:
        # Try to connect to Azure Storage
        blob_service_client = BlobServiceClient.from_connection_string(
            settings.AZURE_CONNECTION_STRING
        )
        # List containers to verify connection
        containers = blob_service_client.list_containers()
        next(containers)  # Try to access at least one container
        return "healthy"
    except Exception as e:
        return f"unhealthy: {str(e)}"


# Optional: Add cache check if you're using cache
def check_cache():
    try:
        cache.set("healthcheck", "test", 1)
        if cache.get("healthcheck") == "test":
            return "healthy"
        return "unhealthy"
    except Exception as e:
        return f"unhealthy: {str(e)}"


def health_check(request):
    # Check database connection
    db_healthy = True
    try:
        db_conn = connections["default"]
        db_conn.cursor()
    except OperationalError:
        db_healthy = False

    # Check if application is running
    status = {
        "status": "healthy" if db_healthy else "unhealthy",
        "database": "connected" if db_healthy else "disconnected",
        "application": "running",
    }

    status_code = 200 if db_healthy else 503
    return JsonResponse(status, status=status_code)


def readiness_check(request):
    # More comprehensive check including external services
    status = {
        "status": "ready",
        "database": check_database(),
        "azure_storage": check_azure_storage(),
        "timestamp": datetime.now().isoformat(),
    }

    all_healthy = all(v == "healthy" for v in status.values() if isinstance(v, str))
    status_code = 200 if all_healthy else 503

    return JsonResponse(status, status=status_code)
