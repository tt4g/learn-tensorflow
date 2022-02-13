FROM tensorflow/tensorflow:2.8.0-jupyter

RUN python -m pip install --upgrade pip \
    && python -m pip install scikit-learn==1.0.2 \
    tensorflow-hub==0.12.0 tensorflow-datasets==4.5.2 \
    seaborn==0.11.2 \
    # Install pyyaml and h5py for saving model.
    pyyaml==6.0 h5py==3.6.0 \
    # Debung Jupiter notebook on Visual Studio Code.
    ipykernel==6.9.0
