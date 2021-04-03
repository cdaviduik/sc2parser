import os
import pickle

from replay.common.logger import log


def load_cache(parsed_path, enable_caching=True):
    if not enable_caching:
        return []

    cache_filename = _get_cache_filename(parsed_path)
    if not os.path.exists(cache_filename):
        return []

    with open(cache_filename, 'rb') as fp:
        return pickle.load(fp)


def write_cache(cache, parsed_path, enable_caching=True):
    if not enable_caching:
        return

    cache_filename = _get_cache_filename(parsed_path)
    log('writing cache to filename', cache_filename)
    log('cache', cache)
    with open(cache_filename, 'wb') as fp:
        pickle.dump(cache, fp)


def _get_cache_filename(parsed_path):
    return '{}/parsed.cache'.format(parsed_path)
