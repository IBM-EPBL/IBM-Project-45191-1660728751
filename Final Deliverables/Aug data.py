from keras.preprocessing.image import ImageDataGenerator
import cv2
from os import listdir
import time    

def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return f"{h}:{m}:{round(s,1)}"

def augment_data(file_dir, n_generated_samples, save_to_dir):
    data_gen = ImageDataGenerator(rotation_range=30, 
                                  width_shift_range=0.1,
                                  height_shift_range=0.15, 
                                  shear_range=0.25, 
                                  zoom_range = 0.2,
                                  horizontal_flip=True, 
                                  vertical_flip=False, 
                                  fill_mode='nearest',
                                  brightness_range=(0.5,1.2)
                                 )

    
    for filename in listdir(file_dir):
        image = cv2.imread(file_dir + '/' + filename)
        image = image.reshape((1,)+image.shape)
        save_prefix = 'aug_' + filename[:-4]    
        i=0
        for batch in data_gen.flow(x=image, batch_size=1, save_to_dir=save_to_dir,
                                   save_prefix=save_prefix, save_format='jpg'):
            i += 1
            if i > n_generated_samples:
                break
start_time = time.time()

augmented_data_path = r'E:\IBM Project\augmented data'
augment_data(file_dir=r'E:\IBM Project\augmented data\Bird\GIB_AUG', n_generated_samples=8, save_to_dir=augmented_data_path+'/Bird/GIB_AUG')
augment_data(file_dir=r'E:\IBM Project\augmented data\Bird\SPS_AUG', n_generated_samples=8, save_to_dir=augmented_data_path+'/Bird/SPS_AUG')
augment_data(file_dir=r'E:\IBM Project\augmented data\Flower\Corpse_AUG', n_generated_samples=8, save_to_dir=augmented_data_path+'/Flower/Corpse_AUG')
augment_data(file_dir=r'E:\IBM Project\augmented data\Flower\LS_Orchid_AUG', n_generated_samples=8, save_to_dir=augmented_data_path+'/Flower/LS_Orchid_AUG')
augment_data(file_dir=r'E:\IBM Project\augmented data\Mammal\LS_Pangolin_AUG', n_generated_samples=8, save_to_dir=augmented_data_path+'/Mammal/Pangolin_AUG')
augment_data(file_dir=r'E:\IBM Project\augmented data\Mammal\SW_Deer_AUG', n_generated_samples=8, save_to_dir=augmented_data_path+'/Mammal/SW_Deer_AUG')


end_time = time.time()
execution_time = (end_time - start_time)
print("Elapsed Time : "+str(execution_time))