import sys
PY2 = sys.version_info[0] == 2

if not PY2:
    strtypes = (str,)
else:
    strtypes = (str, unicode)
    