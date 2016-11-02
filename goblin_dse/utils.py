import functools
import operator


def get_id_hash(id_dict):
    hashes = map(hash, id_dict.items())
    id_hash = functools.reduce(operator.xor, hashes, 0)
    return id_hash
