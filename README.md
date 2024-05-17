# ECGNet: Low Precision Neural Net for ECG Classificiation on FPGA

## Contents

- [Introduction](## Introduction)
- [Requirements](## Requirements)
- [Usage](## Usage)
- [FAQ and Issues]()
- [Citation]()
- [Contributing]()



## Introduction 
The goal of this project is to deploy accurate, unbiased neural networks, which can be used in hospitals to detect arrhythmia at early stages, with processing on low-power, cheap and edge hardware to preserve privacy of patients.

## Requirements
- An ubuntu PC or VM(8GB RAM minimum) with sudo access
- A PYNQ supported board connected to the internet via ethernet (Tested with PYNQ-Z2)
- SD Card (16GB minimum)
- Ethernet cable
- Micro USB cable

Note: For Installing and setting up environment refer to `SETUP.md`

## Usage

Install required packages 

`pip3 install -r requirements.txt`

To use the jupyter notebook interface use

`cd /path/to/finn ` \
`./run-docker.sh notebook` \
`cd notebooks` \
`git clone git@github.com:Adityasrinivas24/ecg-classification-pynq.git`

**Architecture**

![Model Definition](assets/model-definition.png)

**Pretrained Models**

| Model | Specification  | ONNX |
|-------------| ------------- | ------------- |
|EcgNet| 2W2A | []() |
|EcgNet| 4W4A | []() |
<!-- |HeartNet| 4W4A | []() | -->

### Notebooks

**Outside the Docker Environment** \
`1-ecgnet-train-test` trains and validates a quantized neural network to classify ecg images 

**In the Docker Environment** \
`2-ecgnet-onnx-export` exports the model to finn compatible onnx format \
`3-ecgnet-finn-compile` has all the steps required to compile design using finn 

**On PYNQ** \
`4-ecgnet-pynq-deploy` contains details on pynq deployment and results 

## Issues
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

    