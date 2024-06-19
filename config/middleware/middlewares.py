from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.http import JsonResponse

class RateLimitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("--middleware initiated")
        if request.user.is_authenticated and request.path == '/friend-request/send/':
            cache_key = f"friend_request_rate_{request.user.id}"
            request_count = cache.get(cache_key, 0)
            if request_count >= 3:
                return JsonResponse({"detail": "You cannot send more than 3 friend requests within a minute."}, status=429)
            cache.set(cache_key, request_count + 1, timeout=60)
