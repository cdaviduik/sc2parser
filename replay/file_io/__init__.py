import os
import shutil

from replay.common.logger import log


def copy_file(src_filepath, dst_filename, skip_existing=True):
    print "\nsrc_filepath:"
    print src_filepath

    # TODO: configure for mac vs win
    filepath, _, old_filename = src_filepath.rpartition('\\')
    print "\nfilepath:"
    print filepath

    parsed_path = '{}/parsed'.format(filepath)
    print "\nparsed_path:"
    print parsed_path
    if not os.path.exists(parsed_path):
        os.makedirs(parsed_path)

    dst_filepath = '{}/{}'.format(parsed_path, dst_filename)
    dst_exists = os.path.exists(dst_filepath)
    log("dst_filepath", dst_filepath)
    log("file exists", dst_exists)

    if dst_exists and skip_existing:
        log("skipping existing", dst_filepath)
        return

    shutil.copy(src_filepath, dst_filepath)
