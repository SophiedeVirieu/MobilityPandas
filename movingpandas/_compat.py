import os

HAS_PYMEOS = None
USE_PYMEOS = None

INSTALL_PYMEOS_ERROR = "To use PyMEOS within MovingPandas, you need to install PyMEOS: \
'conda install pymeos' or 'pip install pymeos'"

try:
    import pymeos  # noqa

    HAS_PYMEOS = True
except ImportError:
    HAS_PYMEOS = False

print("HAS_PYMEOS = ", HAS_PYMEOS)

def set_use_pymeos(val=None):
    """
    Set the global configuration on whether to use PyMEOS or not.

    The default is use PyMEOS if it is installed. This can be overridden
    with an environment variable USE_PYMEOS (this is only checked at
    first import, cannot be changed during interactive session).

    Alternatively, pass a value here to force a True/False value.
    """
    global USE_PYMEOS

    if val is not None:
        USE_PYMEOS = bool(val)
    else:
        if USE_PYMEOS is None:

            USE_PYMEOS = HAS_PYMEOS

            env_use_pymeos = os.getenv("USE_PYMEOS", None)
            if env_use_pymeos is not None:
                USE_PYMEOS = bool(int(env_use_pymeos))

    # validate the pygeos version
    if USE_PYMEOS:
        try:
            import pymeos  # noqa

            # validate the pymeos version if needed
        except ImportError:
            raise ImportError(INSTALL_PYMEOS_ERROR)

set_use_pymeos()

