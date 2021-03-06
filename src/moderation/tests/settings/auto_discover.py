from moderation.tests.utils.testsettingsmanager import get_only_settings_locals

DATABASE_ENGINE = 'sqlite3'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'moderation',
    'moderation.tests.apps.test_app2',
)

ROOT_URLCONF = 'moderation.tests.urls.auto_register.py'

DJANGO_MODERATION_MODERATORS = (
                               'test@example.com',
                               )
settings = get_only_settings_locals(locals().copy())
