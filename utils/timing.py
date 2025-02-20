import math
import os
import sys
import time
from contextlib import contextmanager

import psutil


@contextmanager
def trace(title):
    """
    Examples:
        >>> with trace("wait"):
                time.sleep(2.0)
    """
    t0 = time.time()
    p = psutil.Process(os.getpid())
    m0 = p.memory_info().rss / 2.0**30
    yield
    m1 = p.memory_info().rss / 2.0**30
    delta = m1 - m0
    sign = "+" if delta >= 0 else "-"
    delta = math.fabs(delta)
    print(
        f"[{m1:.1f}GB({sign}{delta:.1f}GB):{time.time() - t0:.1f}sec] {title} ",
        file=sys.stderr,
    )


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
