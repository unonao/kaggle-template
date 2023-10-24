from .data import *

import time
from contextlib import contextmanager


@contextmanager
def timer(name):
    """
    Examples:
        >>> with timer("wait"):
                time.sleep(2.0)
    """
    t0 = time.time()
    yield
    elapsed_time = time.time() - t0
    print(f"[{name}] done in {elapsed_time:.1f} s")