"""
TD
"""

from .crud_cms import get_info_cms_next_film
from .crud_cms import get_info_cms_films
from .crud_cms import get_info_cms_schedules
from .crud_cms import get_info_users
from .crud_cms import get_info_user

from .crud_cms import update_user_info
from .crud_cms import update_user_status
from .crud_cms import update_user_hash
from .crud_cms import delete_user
from .crud_cms import insert_new_series
from .crud_cms import insert_new_records
from .crud_cms import update_records



from .crud_cms import get_info_serieses
from .crud_cms import get_info_series_status



from .crud_main import get_id_current_series
from .crud_main import get_info_series
from .crud_main import get_info_schedules
from .crud_main import get_info_series_ids
from .crud_main import get_info_film


# Define what should be available when using "from .crud import *"
__all__ = ['get_info_cms_next_film',
           'get_info_cms_films',
           'get_info_cms_schedules',
           'get_info_users',
           'get_info_user',
           'get_info_serieses',
           'get_info_series_status',
           'get_id_current_series',
           'get_info_series',
           'get_info_schedules',
           'get_info_series_ids',
           'get_info_film',
           ]
