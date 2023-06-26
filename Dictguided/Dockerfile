FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update --allow-releaseinfo-change && apt-get install -y libgbm-dev -y \
    software-properties-common dirmngr -y \
    build-essential -y \
    libgl1-mesa-glx libxrender1 libfontconfig1 -y \
    libglib2.0-0 -y \
    libsm6 libxext6 libxrender-dev -y \
    nano wget screen -y \
    gnupg2 -y \
    libgl1-mesa-glx -y \
    git -y \
    python3.7 python3.7-dev zip

ENV PATH="/root/anaconda3/bin:$PATH" FORCE_CUDA="1" \
    TORCH_CUDA_ARCH_LIST="Kepler;Kepler+Tesla;Maxwell;Maxwell+Tegra;Pascal;Volta;Turing" \
    PYTHONPATH="$PYTHONPATH:/vietscenetext_framework/libs/str_fewer_labels"

RUN apt install -y python3.7-distutils curl && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py &&     python3.7 get-pip.py --user


RUN python3.7 -m pip install --upgrade pip && python3.7 -m pip install torch==1.5.1 torchvision==0.6.1 \
    && python3.7 -m pip install pyyaml==5.4.1 ninja yacs cython matplotlib tqdm opencv-python shapely scipy tensorboardX pyclipper Polygon3 weighted-levenshtein editdistance easydict \
    && python3.7 -m pip install git+https://github.com/facebookresearch/detectron2.git@9eb4831f742ae6a13b8edb61d07b619392fb6543 \
    && python3.7 -m pip install dict_trie nvidia-ml-py3

WORKDIR /
