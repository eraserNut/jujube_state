# -*- coding: UTF-8 -*-
import os
import random
import shutil
import PIL.Image as Image


if __name__ == '__main__':
    root_path = "../../data/"
    train_path = "../../train_data/"
    test_path = "../../test_data/"
    split_rate = 0.8
    typelist = os.listdir(root_path)
    for type in typelist:
        if not os.path.isdir(os.path.join(root_path, type)):
            continue
        type_root_path = os.path.join(root_path, type)
        filelist = os.listdir(type_root_path)
        random.shuffle(filelist)
        type_train_path = os.path.join(train_path, type)
        type_test_path = os.path.join(test_path, type)
        if not os.path.exists(type_train_path):
            os.makedirs(type_train_path)
        if not os.path.exists(type_test_path):
            os.makedirs(type_test_path)
        for file in filelist[:int(len(filelist)*split_rate)]:
            shutil.copyfile(os.path.join(type_root_path, file), os.path.join(type_train_path, file))
            print('copy file ' + file + ' to train dir. Success!')
        for file in filelist[int(len(filelist)*split_rate):]:
            shutil.copyfile(os.path.join(type_root_path, file), os.path.join(type_test_path, file))
            print('copy file ' + file + ' to test dir. Success!')















