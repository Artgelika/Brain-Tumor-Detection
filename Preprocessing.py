import LoadingData
import Paths
import Visualizations
import pickle
import numpy as np
import os

def normalize_data(data_to_normalize:np.array):
    return np.dot(data_to_normalize, 1/np.max(data_to_normalize))

def saving_data(set_to_saving:str, set_dump:list):
    pickle_out = open(set_to_saving, "wb")
    pickle.dump(set_dump, pickle_out)
    pickle_out.close()

def preprocessing_func():
    print("Loading new data!")

    CT_dataset = LoadingData.LoadingPhotos("CT_dataset")
    X_CT_dataset, y_CT_dataset = CT_dataset.loading()
    class_names_general = list(set([x[0] for x in os.listdir(Paths.CT_dataset_all)]))
    assert len(X_CT_dataset) == len(y_CT_dataset)

    print("Before normalizing:\n")
    Visualizations.printed_data(X_CT_dataset, y_CT_dataset)

    print("After normalizing:\n")
    X_CT_dataset = normalize_data(np.array(X_CT_dataset,  dtype="float32"))
    Visualizations.printed_data(X_CT_dataset, y_CT_dataset)
    
    Visualizations.visualize_photos(X_CT_dataset, y_CT_dataset, class_names_general, Paths.one_size)

    saving_data("X_CT_data", X_CT_dataset)
    saving_data("y_CT_data", y_CT_dataset)