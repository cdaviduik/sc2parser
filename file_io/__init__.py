import shutil


def copy_file(src_filepath, dst_filename):
    filepath, _, old_filename = src_filepath.rpartition('/')
    print "\nfilepath:"
    print filepath

    dst_filepath = '{}/{}'.format(filepath, dst_filename)

    print "\ndst_filepath"
    print dst_filepath

    shutil.copy(src_filepath, dst_filepath)