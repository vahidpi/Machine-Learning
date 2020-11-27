import os
import pickle  
import random
import numpy as np
import cv2


url = r'images/'
CATEGORIES=['Cat', 'Dog']
# image normalization
IMG_SIZE = 100

def read_X_y(data):
    random.shuffle(data)
    X=[]
    y=[]
    for features,labels in data:
        X.append(features)    
        y.append(labels)
    X=np.array(X)
    y=np.array(y)
    return X,y

def readImages(setName):
    data=[]
    for category in CATEGORIES:
        path = os.path.join(url,setName, category)
        label=CATEGORIES.index(category)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_arr=cv2.imread(img_path)
            if img_arr is not None: # check if image is valid
                img_arr=cv2.resize(img_arr,(IMG_SIZE,IMG_SIZE)) # resize image to 100*100
                data.append([img_arr,label])
    return data

def import_images():

    # Stroing images in related dataset (Train,Validation,Test)
    data_Train=readImages('Train')
    data_Test=readImages('Test')
    data_Val=readImages('Val')
    
    if len(data_Train)>0 and len(data_Test)>0 and len(data_Val)>0 :       
        print('The number of images: ')
        print('   - Training images: ',len(data_Train))
        print('   - Validation images: ',len(data_Val))
        print('   - Test images: ',len(data_Test))
    
        X_train,y_train=read_X_y(data_Train)
        X_test,y_test=read_X_y(data_Test)
        X_val,y_val=read_X_y(data_Val)
    
        pickle.dump(X_train,open('X_train.pkl','wb'))
        pickle.dump(X_val,open('X_val.pkl','wb'))
        pickle.dump(X_test,open('X_test.pkl','wb'))
        pickle.dump(y_train,open('y_train.pkl','wb'))
        pickle.dump(y_val,open('y_val.pkl','wb'))
        pickle.dump(y_test,open('y_test.pkl','wb'))
    
        print('Images are stored.')
    else:
        print('Error in image storing!')



    
