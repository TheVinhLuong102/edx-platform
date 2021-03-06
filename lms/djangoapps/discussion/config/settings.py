"""
Discussion settings.
"""
from django.conf import settings

# .. toggle_name: FEATURES['ENABLE_FORUM_DAILY_DIGEST']
# .. toggle_implementation: DjangoSetting
# .. toggle_default: True
# .. toggle_description: Set to True to enable forum notification features.
# .. toggle_category: discussion
# .. toggle_use_cases: open_edx
# .. toggle_creation_date: 2020-03-09
# .. toggle_expiration_date: None
# .. toggle_tickets: None
# .. toggle_status: supported
# .. toggle_warnings: None
ENABLE_FORUM_DAILY_DIGEST = 'enable_forum_daily_digest'


def is_forum_daily_digest_enabled():
    """Returns whether forum notification features should be visible"""
    return settings.FEATURES.get('ENABLE_FORUM_DAILY_DIGEST')
