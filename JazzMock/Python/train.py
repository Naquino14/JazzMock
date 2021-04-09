﻿import os

import gpt_2_simple as gpt2
import sys
from datetime import datetime

model_name = "355M"
if not os.path.isdir(os.path.join("models", model_name)):
    print(f"Downloading {model_name} model...")
    gpt2.download_gpt2(model_name=model_name)

file_name = "dataset.csv"  # File name of dataset

sess = gpt2.start_tf_sess()

gpt2.finetune(
    sess,
    dataset=file_name,
    model_name='355M',  # Model you have already downloaded
    steps=-1,  # -1 will do unlimited. Enter number of iterations otherwise
    restore_from='latest',  # Also allows 'fresh' which will overwrite old training
    run_name='test',  # The name to pull or create a checkpoint under
    print_every=50,  # Print iterations every X numebr
    sample_every=150,  # Generate a text sample ever X number of iter.
    save_every=100,  # Save a snapshot every X number of iter.
    learning_rate=0.0001,  # Lower to 0.00001 if you are not getting massive changes in results
    batch_size=1  # Keep at 1 or 2, will use up more memory if you raise this
)
