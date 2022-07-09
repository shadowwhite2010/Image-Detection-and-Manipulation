import json
import sys, os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
from mtcnn import MTCNN

import cv2
import math
import pathlib
# from distutils.dir_util import copy_tree
# import shutil
import pandas as pd
from keras import backend as K
import tensorflow as tf
my_devices = tf.config.experimental.list_physical_devices(device_type='CPU')
tf.config.experimental.set_visible_devices(devices= my_devices, device_type='CPU')
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras import applications
# from efficientnet.tfkeras import EfficientNetB0 #EfficientNetB1, EfficientNetB2, EfficientNetB3, EfficientNetB4, EfficientNetB5, EfficientNetB6, EfficientNetB7
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout
# from tensorflow.keras.optimizers import Adam
# from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import load_model
# base_path = '/content/DeepFake-Detect/train_sample_videos'

# tf.function(experimental_relax_shapes=True)
# tf.compat.v1.disable_eager_execution()
# base_path = 'D:/movies/fake_vid'
 
##$$testing
detector =  [MTCNN()]
best_model = [load_model('trained_models/best_model_7.h5')]


def get_filename_only(file_path):
    file_basename = os.path.basename(file_path)
    filename_only = file_basename.split('.')[0]
    return filename_only
 
# with open(os.path.join(base_path, 'metadata.json')) as metadata_json:
#     metadata = json.load(metadata_json)
#     print(len(metadata))
# filename = "WhatsApp Video 2021-03-26 at 1.05.16 PM.mp4"

def vid_img(file_path):
    path_file = pathlib.Path(file_path)
    filename = str(path_file.name)
    base_path = str(path_file.parent)
    # tmp_path = os.path.join(base_path, get_filename_only(filename))
    tmp_path = "d_f/vid_img"
    # print('Creating Directory: ' + tmp_path)
    # os.makedirs(tmp_path, exist_ok=True)
    print('Converting Video to Images...')
    count = 0
    video_file = os.path.join(base_path, filename)
    cap = cv2.VideoCapture(video_file)
    frame_rate = cap.get(5) #frame rate
    while(cap.isOpened()):
        frame_id = cap.get(1) #current frame number
        ret, frame = cap.read()
        if (ret != True):
            break
        if (frame_id % math.floor(frame_rate) == 0):
            print('Original Dimensions: ', frame.shape)
            if frame.shape[1] < 300:
                scale_ratio = 2
            elif frame.shape[1] > 1900:
                scale_ratio = 0.33
            elif frame.shape[1] > 1000 and frame.shape[1] <= 1900 :
                scale_ratio = 0.5
            else:
                scale_ratio = 1
            print('Scale Ratio: ', scale_ratio)

            width = int(frame.shape[1] * scale_ratio)
            height = int(frame.shape[0] * scale_ratio)
            dim = (width, height)
            new_frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
            print('Resized Dimensions: ', new_frame.shape)

            new_filename = '{}-{:03d}.png'.format(os.path.join(tmp_path, get_filename_only(filename)), count)
            count = count + 1
            cv2.imwrite(new_filename, new_frame)
    cap.release()
    print("Done!")

def model_load():
    return [load_model('trained_models/best_model_7.h5')]

def predictor():
    input_size = 128
    pred_datagen = ImageDataGenerator(
        rescale = 1/255    #rescale the tensor values to [0,1]
    )

    pred_generator = pred_datagen.flow_from_directory(
        directory = 'd_f',
        classes=['cr_face'],
        target_size = (input_size, input_size),
        color_mode = "rgb",
        class_mode = None,
        batch_size = 1,
        shuffle = False
    )
    # tf.compat.v1.disable_eager_execution()
    # tf.function(experimental_relax_shapes=True)
    # load the saved model that is considered the best
    # best_model = load_model('/content/drive/MyDrive/Colab Notebooks/weights/best_model.h5')
    tf.function(experimental_relax_shapes=True)
    pred_generator.reset()
    preds = best_model[0].predict(
        pred_generator,
        
        verbose = 1
    )

    test_results = pd.DataFrame({
        "Filename": pred_generator.filenames,
        "Prediction": preds.flatten()
    })
    return test_results

# def model_create():
#     efficient_net = EfficientNetB0(
#         weights = 'imagenet',
#         input_shape = (input_size, input_size, 3),
#         include_top = False,
#         pooling = 'max'
#     )

#     model = Sequential()
#     model.add(efficient_net)
#     model.add(Dense(units = 512, activation = 'relu'))
#     model.add(Dropout(0.5))
#     model.add(Dense(units = 128, activation = 'relu'))
#     model.add(Dense(units = 1, activation = 'sigmoid'))
#     model.summary()

#     # Compile model
#     model.compile(optimizer = Adam(lr=0.0001), loss='binary_crossentropy', metrics=['accuracy'])
#     return model

def dtctr_gen():
    detector = [MTCNN()]
    return detector

def crop_face_img(image):
    # image = cv2.cvtColor(cv2.imread(os.path.join(tmp_path, frame)), cv2.COLOR_BGR2RGB)
    # image = im_lis[len(im_lis)-1]
    # tf.compat.v1.disable_eager_execution()
    # tf.function(experimental_relax_shapes=True)
    results = detector[0].detect_faces(image)
    print('Face Detected: ', len(results))
    count = 0
    for result in results:
        bounding_box = result['box']
        print(bounding_box)
        confidence = result['confidence']
        print(confidence)
        if len(results) < 2 or confidence > 0.95:
            margin_x = bounding_box[2] * 0.3  # 30% as the margin
            margin_y = bounding_box[3] * 0.3  # 30% as the margin
            x1 = int(bounding_box[0] - margin_x)
            if x1 < 0:
                x1 = 0
            x2 = int(bounding_box[0] + bounding_box[2] + margin_x)
            if x2 > image.shape[1]:
                x2 = image.shape[1]
            y1 = int(bounding_box[1] - margin_y)
            if y1 < 0:
                y1 = 0
            y2 = int(bounding_box[1] + bounding_box[3] + margin_y)
            if y2 > image.shape[0]:
                y2 = image.shape[0]
            print(x1, y1, x2, y2)
            crop_image = image[y1:y2, x1:x2]
            # new_filename = '{}-{:02d}.png'.format(os.path.join(faces_path, get_filename_only(frame)), count)
            new_filename = "d_f/cr_face/img" + str(count) + ".png"
            count = count + 1
            # cv2.imwrite(new_filename, cv2.cvtColor(crop_image, cv2.COLOR_RGB2BGR))
            cv2.imwrite(new_filename, crop_image)
        else:
            print('Skipped a face..')

def crop_face_vid():
    # path_file = pathlib.Path(file_path)
    # filename = str(path_file.name)
    # base_path = str(path_file.parent)
    # tmp_path = os.path.join(base_path, get_filename_only(filename))
    tmp_path = "d_f/vid_img"
    print('Processing Directory: ' + tmp_path)
    frame_images = [x for x in os.listdir(tmp_path) if os.path.isfile(os.path.join(tmp_path, x))]
    # faces_path = os.path.join(tmp_path, 'faces')
    faces_path = "d_f\cr_face"
    # print('Creating Directory: ' + faces_path)
    # os.makedirs(faces_path, exist_ok=True)
    print('Cropping Faces from Images...')
    # detector = MTCNN()
    for frame in frame_images:
        print('Processing ', frame)
        
        image = cv2.cvtColor(cv2.imread(os.path.join(tmp_path, frame)), cv2.COLOR_BGR2RGB)
        results = detector[0].detect_faces(image)
        print('Face Detected: ', len(results))
        count = 0
        
        for result in results:
            bounding_box = result['box']
            print(bounding_box)
            confidence = result['confidence']
            print(confidence)
            if len(results) < 2 or confidence > 0.95:
                margin_x = bounding_box[2] * 0.3  # 30% as the margin
                margin_y = bounding_box[3] * 0.3  # 30% as the margin
                x1 = int(bounding_box[0] - margin_x)
                if x1 < 0:
                    x1 = 0
                x2 = int(bounding_box[0] + bounding_box[2] + margin_x)
                if x2 > image.shape[1]:
                    x2 = image.shape[1]
                y1 = int(bounding_box[1] - margin_y)
                if y1 < 0:
                    y1 = 0
                y2 = int(bounding_box[1] + bounding_box[3] + margin_y)
                if y2 > image.shape[0]:
                    y2 = image.shape[0]
                print(x1, y1, x2, y2)
                crop_image = image[y1:y2, x1:x2]
                new_filename = '{}-{:02d}.png'.format(os.path.join(faces_path, get_filename_only(frame)), count)
                count = count + 1
                cv2.imwrite(new_filename, cv2.cvtColor(crop_image, cv2.COLOR_RGB2BGR))
            else:
                print('Skipped a face..')

def main():
    # print(tf.__version__)
    # crop_face('D:/movies/fake_vid/WhatsApp Video 2021-03-26 at 1.05.16 PM.mp4')
    # tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

    # physical_devices = tf.config.list_physical_devices('CPU')
    # print(physical_devices)
    # tf.config.experimental.set_memory_growth(physical_devices[0], True)
    # vid_img('D:/movies/fake_vid/WhatsApp Video 2021-03-26 at 1.05.16 PM.mp4')
    # detector = dtctr_gen()
    # img = cv2.cvtColor(cv2.imread("C:/Users/DELL/Downloads/deepfake_database1/deepfake_database/deepfake_database/train_test/df/df00144.jpg"), cv2.COLOR_BGR2RGB)
    # # crop_face_img(detector, img)
    # crop_face_img(img)
    # # best_model = model_load()
    # # test_results = predictor(best_model)
    # test_results = predictor()
    # print(type(test_results), test_results, "\n")
    # for tr in test_results.itertuples():
    #     print(type(tr))
    #     print(tr, "\n------\n")
    #     print(type(tr.Filename), type(tr[2]))
    #     print(tr[1])
    # filepath = "D:\movies/fake_vid/testvid.mp4"
    # vid_img(filepath)
    crop_face_vid()



if __name__=="__main__":
    main()
# for filename in metadata.keys():
#     print(filename)
#     if (filename.endswith(".mp4")):
#         tmp_path = os.path.join(base_path, get_filename_only(filename))
#         print('Creating Directory: ' + tmp_path)
#         os.makedirs(tmp_path, exist_ok=True)
#         print('Converting Video to Images...')
#         count = 0
#         video_file = os.path.join(base_path, filename)
#         cap = cv2.VideoCapture(video_file)
#         frame_rate = cap.get(5) #frame rate
#         while(cap.isOpened()):
#             frame_id = cap.get(1) #current frame number
#             ret, frame = cap.read()
#             if (ret != True):
#                 break
#             if (frame_id % math.floor(frame_rate) == 0):
#                 print('Original Dimensions: ', frame.shape)
#                 if frame.shape[1] < 300:
#                     scale_ratio = 2
#                 elif frame.shape[1] > 1900:
#                     scale_ratio = 0.33
#                 elif frame.shape[1] > 1000 and frame.shape[1] <= 1900 :
#                     scale_ratio = 0.5
#                 else:
#                     scale_ratio = 1
#                 print('Scale Ratio: ', scale_ratio)
 
#                 width = int(frame.shape[1] * scale_ratio)
#                 height = int(frame.shape[0] * scale_ratio)
#                 dim = (width, height)
#                 new_frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
#                 print('Resized Dimensions: ', new_frame.shape)
 
#                 new_filename = '{}-{:03d}.png'.format(os.path.join(tmp_path, get_filename_only(filename)), count)
#                 count = count + 1
#                 cv2.imwrite(new_filename, new_frame)
#         cap.release()
#         print("Done!")
#     else:
#         continue