
def setupConfigurations():
    import django
    from pathlib import Path
    from django.conf import settings

    if settings.configured:
        return
    
    BASE_DIR                 = Path(__file__).resolve().parent.parent

   
    settings.configure(
        INSTALLED_APPS = ["boilerplate", ],
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'database/db.sqlite3',
            },
        }, 
        
        DEBUG=True,
    )

    django.setup()