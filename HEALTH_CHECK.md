# Health Check Endpoint Configuration

This file documents the health check configuration for production deployment.

## Health Check Endpoint

**Path**: `/health/`

The health check endpoint verifies:
- Application is running
- Database connection is active
- Critical services are operational

## Render Configuration

In `render.yaml`, the health check is configured as:
```yaml
healthCheckPath: /
```

## Implementation

If you need a dedicated health check endpoint, add this to your Django app:

### Create health check view

**File**: `server/djangoapp/views.py`

```python
from django.http import JsonResponse
from django.db import connection

def health_check(request):
    """
    Health check endpoint for monitoring
    Returns 200 if application is healthy
    """
    try:
        # Check database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        return JsonResponse({
            'status': 'healthy',
            'database': 'connected'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'unhealthy',
            'error': str(e)
        }, status=503)
```

### Add URL route

**File**: `server/djangoproj/urls.py`

```python
from djangoapp.views import health_check

urlpatterns = [
    path('health/', health_check, name='health_check'),
    # ... other urls
]
```

### Update render.yaml

```yaml
healthCheckPath: /health/
```

## Monitoring

Render automatically monitors your health check endpoint and alerts if:
- Endpoint returns non-200 status
- Endpoint times out (>30 seconds)
- Multiple consecutive failures occur

## Best Practices

1. Keep health checks lightweight (< 1 second response time)
2. Verify critical dependencies (database, cache, etc.)
3. Return appropriate HTTP status codes:
   - `200`: Healthy
   - `503`: Service Unavailable
4. Log health check failures for debugging
