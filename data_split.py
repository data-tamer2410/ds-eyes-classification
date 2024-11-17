import os
import sys
import shutil
from sklearn.model_selection import train_test_split

dir_names = ["train", "val", "test"]
cls_names = ["closed_eye", "open_eye"]


def create_dirs(new_dir_name):
    base_dir = os.path.join("./", new_dir_name)
    if not os.path.exists(base_dir):
        os.mkdir(
            base_dir,
        )
    for dir_name in dir_names:
        path_dir = os.path.join(base_dir, dir_name)
        for cl in cls_names:
            os.makedirs(os.path.join(path_dir, cl), exist_ok=True)
    return base_dir


def split_data(dataset_path, base_dir):
    for class_name in cls_names:
        cls_path = os.path.join(dataset_path, class_name)
        images = os.listdir(cls_path)

        train_set, temp_set = train_test_split(images, test_size=0.3, random_state=2)
        test_set, val_set = train_test_split(temp_set, test_size=0.5, random_state=2)

        for dir_name, dataset in zip(dir_names, [train_set, val_set, test_set]):
            dts = os.path.join(base_dir, dir_name, class_name)
            for file_name in dataset:
                scr_path = os.path.join(cls_path, file_name)
                shutil.copy(scr_path, dts)
        shutil.make_archive('data','zip',base_dir)

if __name__ == "__main__":
    dir_name, data_path, *_ = sys.argv[1:]
    base_dir = create_dirs(dir_name)
    split_data(data_path, base_dir)
