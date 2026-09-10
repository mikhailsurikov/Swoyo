### `__init__.py`
# Настройте пакет так, чтобы работал импорт:
# from order_system import calculate_total, OrderError

from .validators import *
from .calculator import *
from .exceptions import *

__all__ = [name for name in globals() if not name.startswith('_')]
