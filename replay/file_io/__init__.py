import os
import shutil

from replay.common.logger import log


def copy_file(root_src_path, src_filepath, dst_filename, root_dst_path, skip_existing=True, path_separator="\\"):
    log('original_path', root_src_path)

    print "\nsrc_filepath:"
    print src_filepath

    filepath, _, old_filename = src_filepath.rpartition(path_separator)
    print "\nfilepath:"
    print filepath

    _, _, relative_path = filepath.rpartition(root_src_path)
    log('relative_path', relative_path)

    parsed_path = root_dst_path + relative_path

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

    log("copying file from src to dst", src_filepath, dst_filepath)
    shutil.copy(src_filepath, dst_filepath)
