def copy_image_with_suffix(src_path, suffix='_copy'):
    src = src_path
    parts = src.split('/')
    if len(parts) > 1:
        dir_part = '/'.join(parts[:-1]) + '/'
        name = parts[-1]
    else:
        dir_part = ''
        name = parts[0]
    parts2 = name.split('.')
    if len(parts2) > 1:
        dest = dir_part + '.'.join(parts2[:-1]) + suffix + '.' + parts2[-1]
    else:
        dest = dir_part + name + suffix
    with open(src, 'rb') as sf, open(dest, 'wb') as df:
        df.write(sf.read())
    return dest


if __name__ == '__main__':
    src = '/Users/wonseok/Desktop/polytec_python26/20_05_18_파일 입출력/cat.png'
    
    out = copy_image_with_suffix(src)