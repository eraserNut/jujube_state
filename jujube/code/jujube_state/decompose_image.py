# -*- coding: UTF-8 -*-
import os
import PIL.Image as Image


def decom_img(img, decom_num):
    decom_list = []

    width, height = img.size
    decom_width = int(width/3)
    for i in range(0, decom_num):
        for j in range(0, decom_num):
            box = (j*decom_width, i*decom_width, (j+1)*decom_width, (i+1)*decom_width)
            decom = img.crop(box)
            decom_list.append(decom)
    return decom_list

def crop_by_center(img, rate):
    raw_size, _ = img.size
    padding = int(raw_size*(1-rate)/2)
    rect = (padding, padding, raw_size-padding, raw_size-padding)
    crop_img = img.crop(rect)
    return crop_img


if __name__ == '__main__':
    root_path = '../../data'
    dst_path = '../../data_decom'
    # generate dst dir
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    typelist = os.listdir(root_path)
    for type in typelist:
        # make sure type is dir
        if not os.path.isdir(os.path.join(root_path, type)):
            continue
        if type == 'beak' or type == 'mould':
            mode = type
            if not os.path.exists(os.path.join(dst_path, mode)):
                os.makedirs(os.path.join(dst_path, mode))
        else:
            mode = 'well'
            if not os.path.exists(os.path.join(dst_path, mode)):
                os.makedirs(os.path.join(dst_path, mode))

        src_path = os.path.join(root_path, type)
        img_list = os.listdir(src_path)
        for img_name in img_list[:200]:
            (name, ext) = os.path.splitext(img_name)
            img_path = os.path.join(src_path, img_name)
            img = Image.open(img_path)
            img = img.resize((224, 224))
            # img = crop_by_center(img, rate=0.7) # crop rate by center from img
            decom_list = decom_img(img, decom_num=3) # 3 means 3*3=9

            index = 1
            for decom in decom_list:
                save_name = name + '_crop' + str(index) + '.png'
                if not os.path.exists(os.path.join(dst_path, mode, save_name)):
                    decom.save(os.path.join(dst_path, mode, save_name))
                    print('save ' + save_name)
                index += 1




