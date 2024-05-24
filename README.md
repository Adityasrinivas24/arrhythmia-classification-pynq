# Low Precision Neural Network for Arrhythmia detection on FPGA

## Contents

- Introduction
- Requirements
- Usage
- FAQ and Issues
- Acknowledgement
- Citation


## Introduction 
The goal of this project is to deploy accurate, unbiased neural networks, which can be used in hospitals to detect arrhythmia at early stages, with processing on low-power, cheap and edge hardware to preserve privacy of patients.

**Neural Net Architecture**

<img src="https://github.com/Adityasrinivas24/ecg-classification-pynq/blob/main/assets/model-architecture.png" width="300" height="450">

## Requirements
- An ubuntu PC or VM(8GB RAM minimum) with sudo access (Tested on Ubuntu 20.04 Focal Fossa)
- A PYNQ supported board connected to the internet via ethernet (Tested on PYNQ-Z2)
- SD Card (16GB minimum)
- Ethernet cable
- Micro USB cable

Note: For Installing and setting up environment refer to `SETUP.md`

## Usage

`cd /path/to/finn ` \
`./run-docker.sh notebook` \
`cd notebooks` \
`git clone git@github.com:Adityasrinivas24/ecg-classification-pynq.git`

Install required packages outside docker environment

`pip3 install -r requirements.txt`


**Pretrained Models**

| Model | Specification  | ONNX |
|-------------| ------------- | ------------- |
|EcgNet| W2A2 | [ECGNet W2A2](https://github.com/Adityasrinivas24/ecg-classification-pynq/blob/main/onnx_models/ecgnet_w2a2_export.onnx) |
|EcgNet| W4A4 | [EcgNet W4A4](https://github.com/Adityasrinivas24/ecg-classification-pynq/blob/main/onnx_models/ecgnet_w4a4_export.onnx) |
|HeartNet| W4A4 | [Heartnet W4A4](https://github.com/Adityasrinivas24/ecg-classification-pynq/blob/main/onnx_models/heartnet_w4a4_export.onnx) |

### Notebooks

**Outside the Docker Environment** \
`1-ecgnet-train-test` trains and validates a quantized neural network to classify ecg images 

**In the Docker Environment** \
`2-ecgnet-onnx-export` exports the model to finn compatible onnx format \
`3-ecgnet-finn-compile` has all the steps required to compile design using finn 

**On PYNQ** \
`4-ecgnet-pynq-deploy` contains details on pynq deployment and results 

## FAQ and Issues
Resolve the NewConnectionError raised by pip during library installations in PYNQ refer [this discussion](https://stackoverflow.com/questions/52815784/python-pip-raising-newconnectionerror-while-installing-libraries)

Other FAQs and Issues can be found [here](https://github.com/nhma20/brevitas_finn_fpga/tree/main?tab=readme-ov-file#misc)

## Acknowledgement

```
@software{brevitas,
  author       = {Alessandro Pappalardo},
  title        = {Xilinx/brevitas},
  year         = {2022},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.3333552},
  url          = {https://doi.org/10.5281/zenodo.3333552}
}
```

```
@inproceedings{finn,
author = {Umuroglu, Yaman and Fraser, Nicholas J. and Gambardella, Giulio and Blott, Michaela and Leong, Philip and Jahre, Magnus and Vissers, Kees},
title = {FINN: A Framework for Fast, Scalable Binarized Neural Network Inference},
booktitle = {Proceedings of the 2017 ACM/SIGDA International Symposium on Field-Programmable Gate Arrays},
series = {FPGA '17},
year = {2017},
pages = {65--74},
publisher = {ACM}
}

```

    
