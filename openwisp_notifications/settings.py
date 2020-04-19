from django.conf import settings
from notifications.settings import CONFIG_DEFAULTS

CONFIG_DEFAULTS.update(
    {
        'email_subject': 'Default email subject',
        'USE_JSONFIELD': True,
        'url': 'https://localhost:8000/admin',
    }
)


def get_config():
    user_config = getattr(settings, 'OPENWISP_NOTIFICATIONS_CONFIG', {})

    config = CONFIG_DEFAULTS.copy()
    config.update(user_config)

    return config
