truthy = frozenset(('t', 'true', 'y', 'yes', 'on', '1'))


def asbool(s):
    """
    Return the boolean value ``True`` if the case-lowered value of string
    input ``s`` is any of ``t``, ``true``, ``y``, ``on``, or ``1``, otherwise
    return the boolean value ``False``. If ``s`` is the value ``None``, return
    ``False``. If ``s`` is already one of the boolean values ``True`` or
    ``False``.
    """
    if s is None:
        return False
    if isinstance(s, bool):
        return s
    s = str(s).strip()
    return s.lower() in truthy
