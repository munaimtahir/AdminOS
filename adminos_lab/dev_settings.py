from .settings import *  # noqa

# Force safe dev defaults (does not affect production)
DEBUG = True

# If SECRET_KEY is missing in .env, use a dev-only fallback
if not SECRET_KEY:  # noqa: F405
    SECRET_KEY = "dev-not-for-production-please-set-SECRET_KEY-in-.env"  # noqa: F405

# Accept local/IP hosts during dev
ALLOWED_HOSTS = ["*",]  # you can tighten to ["172.235.33.181", "127.0.0.1", "localhost"]

# Helpful when accessing via IP:PORT
# Adjust to https://your-domain later if you enable TLS
try:
    CSRF_TRUSTED_ORIGINS  # noqa: F401
except NameError:
    CSRF_TRUSTED_ORIGINS = []
if "http://172.235.33.181:8001" not in CSRF_TRUSTED_ORIGINS:
    CSRF_TRUSTED_ORIGINS.append("http://172.235.33.181:8001")
