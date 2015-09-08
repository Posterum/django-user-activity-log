# -*- coding: utf-8 -*-

from django.conf import settings


# Log anonimus actions?
ANONIMOUS = getattr(settings, 'ACTIVITYLOG_ANONIMOUS', True)

# Update last activity datetime in user profile
LAST_ACTIVITY = getattr(settings, 'ACTIVITYLOG_LAST_ACTIVITY', True)

# Only this methods will be logged
METHODS = getattr(settings, 'ACTIVITYLOG_METHODS',
                  ('GET', 'POST', 'PUT', 'PATCH', 'DELETE'))

# List of response statuses, which logged. By default - all logged.
# Don't use with ACTIVITYLOG_EXCLUDE_STATUSES
STATUSES = getattr(settings, 'ACTIVITYLOG_STATUSES', None)

# List of response statuses, which ignores. Don't use with ACTIVITYLOG_STATUSES
EXCLUDE_STATUSES = getattr(settings, 'ACTIVITYLOG_EXCLUDE_STATUSES', None)

# URL substrings, which ignores
EXCLUDE_URLS = getattr(settings, 'ACTIVITYLOG_EXCLUDE_URLS', ())

# Create DB automatically (for postgres, and may be mysql)
AUTOCREATE_DB = getattr(settings, 'ACTIVITYLOG_AUTOCREATE_DB', False)

# Log DB key in DATABASES (for internal usage only, don't modify)
LOG_DB_KEY = getattr(settings, 'DATABASE_APPS_MAPPING', {}).get('activity_log')

if AUTOCREATE_DB and LOG_DB_KEY and not settings.DATABASES.get(LOG_DB_KEY):
    db = settings.DATABASES['default'].copy()
    db['NAME'] = '{}_{}'.format(db['NAME'], LOG_DB_KEY)
    settings.DATABASES[LOG_DB_KEY] = db
