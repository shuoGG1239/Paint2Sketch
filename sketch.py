from keras.models import load_model

from cv_utils import *

mod = None


def transforms(path):
    global mod
    if mod is None:
        mod = load_model('mod.h5')

    from_mat = cv2.imread(path)
    width = float(from_mat.shape[1])
    height = float(from_mat.shape[0])
    if (width > height):
        from_mat = cv2.resize(from_mat, (512, int(512 / width * height)), interpolation=cv2.INTER_AREA)
        new_width = 512
        new_height = int(512 / width * height)
    else:
        from_mat = cv2.resize(from_mat, (int(512 / height * width), 512), interpolation=cv2.INTER_AREA)
        new_width = int(512 / height * width)
        new_height = 512
    from_mat = from_mat.transpose((2, 0, 1))
    light_map = np.zeros(from_mat.shape, dtype=np.float)
    for channel in range(3):
        light_map[channel] = get_light_map_single(from_mat[channel])
    light_map = normalize_pic(light_map)
    light_map = resize_img_512_3d(light_map)
    line_mat = mod.predict(light_map, batch_size=1)
    line_mat = line_mat.transpose((3, 1, 2, 0))[0]
    line_mat = line_mat[0:int(new_height), 0:int(new_width), :]
    line_mat = np.amax(line_mat, 2)
    m1 = get_active_img_denoise(line_mat)
    m2 = get_active_img_denoise_filter(line_mat)
    m3 = get_active_img_denoise_filter2(line_mat)
    return [m1, m2, m3]
