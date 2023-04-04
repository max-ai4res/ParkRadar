#
# Configuro le variabili d'ambiente base per 4Park
#

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

BATCH_SIZE = 32
AUTOTUNE = tf.data.AUTOTUNE

# caricamento dei dataset di traing / test da file system
def load_ds(data_folder=None, subset=None):
    if data_folder == None:
        return None
    
    if subset == None or subset == 'full':
        vsplit = 0.0
    else:
        vsplit = 0.2

    return tf.keras.utils.image_dataset_from_directory(
        data_folder,
        labels='inferred',
        label_mode='binary',
        class_names=('free', 'busy'),
        color_mode='rgb',
        batch_size=BATCH_SIZE,
        image_size=(150,150),
        shuffle=True,
        seed=311,
        validation_split=vsplit,
        subset=subset,
        interpolation='bilinear',
        follow_links=False,
        crop_to_aspect_ratio=False    
    )

def info_ds(name, ds):
    bsize = tf.data.experimental.cardinality(ds)
    print(f'{name} [{len(ds.file_paths)}]')