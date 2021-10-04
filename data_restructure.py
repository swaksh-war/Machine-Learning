#renaming and resizing each files in 10 folders
import os
import cv2
import multiprocessing
import time

WIDTH = 128
HEIGHT = 128


path_to_main = r"D:\Coding\Python Programming\Modules\Pytorch\tomato_leaf\tomato\train"
subfolders = ['Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___healthy', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_mosaic_virus', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus']



path_to_new = r"D:\Coding\Python Programming\Modules\Pytorch\new_tomato_data\train"
new_subfolder = ['baterical_spot', 'early_blight', 'healthy', 'late_blight', 'leaf_mold', 'septoria_leaf_spot', 'spider_mites', 'target_spot', 'tomato_mosaic_virus', 'yellow_leaf_curl_virus']



def resizeallimg(t):
    x=0
    path_to_the_folder = path_to_main + '\\' + subfolders[t]
    path_to_the_save_folder = path_to_new + '\\' + new_subfolder[t]
    for i in os.listdir(path_to_the_folder):
        img_path = path_to_the_folder + '\\' + i
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        resized_img = cv2.resize(img,(WIDTH,HEIGHT))
        cv2.imwrite(path_to_the_save_folder+ '\\' +f'{x}.jpg', resized_img)
        x+=1

if __name__ == '__main__':

    start = time.perf_counter()
    arr = []
    for i in range(10):
        p = multiprocessing.Process(target= resizeallimg, args=(i,))
        p.start()
        arr.append(p)
        
    for o in arr:
        o.join()
    end = time.perf_counter()
    print(f"execution time: {round(end-start, 2)}")