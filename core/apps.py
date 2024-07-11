from django.apps import AppConfig
from django.conf import settings
import os

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    
    def ready(self):
        
        if os.environ.get('RUN_MAIN') == 'true':
            from core.scheduler import start_scheduler
            start_scheduler()