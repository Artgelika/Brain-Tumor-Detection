import os
import cv2            
from tqdm import tqdm
from sklearn.utils import shuffle 
import numpy as np  

class LoadingPhotos:
    def __init__(self, name):
        self.name = name
        self.X_set, self.y_set, self.set_of_data = [],[],[]

    def loading(self):
        self._correct_path()
        self._load_data()
        self._create_set_data()
        self._preparing_sets()
        return self.X_set, self.y_set

    def _correct_path(self):
        self.path = PATH + "\\" + self.name
        return self.path 

    def _load_data(self):
        try:
            self.dataset = os.listdir(self.path)  
            return self.dataset
        except FileNotFoundError:
            print("File not exist") 

    def _label_creator(self, img): 
        word_label = img[0] 
        assert len(self.specific_letters) == 3
        numbers_spec = [i for i in range(len(self.specific_letters))]

        for i in range(len(self.specific_letters)):
            if word_label == self.specific_letters[i]: return numbers_spec[i] 
    
    def _create_set_data(self):
        self.specific_letters = list(set([x[0] for x in self.dataset])) 
        for img in tqdm(self.dataset):
            try:
                label = self._label_creator(img) 
                path = os.path.join(self.path, img)
                img = cv2.resize(cv2.imread(path, cv2.IMREAD_GRAYSCALE), IMG_SIZE)
                self.set_of_data.append([np.array(img), np.array(label)])

            except Exception as e:
                print(e)

        self.set_of_data[:] = shuffle(self.set_of_data)

    def _preparing_sets(self):
        for feature, label in self.set_of_data:
            self.X_set.append(feature)
            self.y_set.append(label)