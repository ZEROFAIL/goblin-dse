def _hash(val):
    if isinstance(val, dict):
        result = 0
        for key, value in val.items():
            result += _hash((key, _hash(value)))
        return result
    else:
        return hash(val)


def dse_get_hashable_id(val):
    if isinstance(val, dict):
        return _hash(val)
    return val
