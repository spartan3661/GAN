import lmdb
import numpy as np
from PIL import Image
import io

lmdb_path = "C:/Users/Springfrost/Documents/My Documents/AI Projects/GAN Mnist/data/bridge_val_lmdb"


env = lmdb.open(lmdb_path, readonly=True, lock=False)
counter = 1
with env.begin(write=False) as txn:
    cursor = txn.cursor()
    for key, value in cursor:
        image = Image.open(io.BytesIO(value))
        
        image.show()
        
        # Convert to numpy array if needed
        img_array = np.array(image)

        print(f"Image size: {image.size}")
        counter += 1
        if counter >= 30:
            break