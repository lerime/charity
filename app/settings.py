try:
    from app.settings_local import *
except ImportError:
    from app.settings_default import *
