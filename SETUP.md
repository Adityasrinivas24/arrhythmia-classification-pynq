# SETUP

## Installation

- Docker Setup
- Install AMD Vivado and Vitis and Vitis HLS(2022.2)
- Finn Setup
- PYNQ Board Setup
  
### Docker Setup

Finn dataflow compiler requires a docker environment to run due to the complex number of packages involved. Docker is setup on Ubuntu 20.04 (Focal Fossa) LTS. 
1. [Linux Docker setup](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
2. [Post Installation Setup](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)

Verify docker is setup to run without root access 

`$ docker run hello-world`

### Install AMD Vivado and Vitis and Vitis HLS

This project is tested using finn == v0.10 along with Vivado (2022.2) version.

1. [Install Vitis Unified installer 2022.2 for linux](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vitis/archive-vitis.html) \
   
`cd path/to/Downloads/filename` \
`chmod +x filename.bin` \
`./filename.bin`
 
3. Select Vivado, Vitis, Vitis HLS using the radio buttons in the unified installer along with the Device specfic packages.

4. Choose Installation directory `tools/Xilinx`
5. `sudo nano ~/.bashrc` \
    Add these lines at the end

    `source /path/to/Xilinx/Vivado/2022.2/settings64.sh` \
    `source /path/to/Xilinx/Vitis_HLS/2022.2/settings64.sh` \
    `source /path/to/Xilinx/Vitis/2022.2/settings64.sh` 

4. Launch vivado and vitis using `vivado&` and `vitis&`

### Finn Setup

Finn requires some environment variables setup.
Make a temporary directory to store finn generated files \
`mkdir temp_finn`

`sudo nano ~/.bashrc` \
Add these lines at the end

`export FINN_XILINX_PATH=/path/to/Xilinx` \
`export FINN_XILINX_VERSION=2022.2` \
`export PLATFORM_REPO_PATHS=/tools/Xilinx/Vitis/2022.2/base_platforms` \
`export FINN_HOST_BUILD_DIR=/path/to/temp_finn`  \
`export VIVADO_PATH=/path/to/Xilinx/Vivado/2022.2` \
`export FINN_ROOT=/path/to/finn`  \
`export PYNQ_BOARD="Pynq-Z2"  #or any other supported board`


Clone the finn [github repository](https://github.com/Xilinx/finn)

`cd path/to/finn` \
`./run-docker.sh quicktest`

This will take a while depending on the machine. 

### PYNQ Board Setup
Follow the Setup shown [here](https://blog.umer-farooq.com/a-pynq-z2-guide-for-absolute-dummies-part-i-fun-with-leds-and-switches-47dd76abf9a9)

Once the jupyter notebook interface is up and running, follow this [simple tutorial](https://github.com/Xilinx/PYNQ-HelloWorld)

Simple Projects can be found [here](https://sceweb.sce.uhcl.edu/xiaokun/doc/OpenIC/OpenProject/SaralaCapstone/Sarala-Capstone-ObjectDetection-Tutorial-PYNQ.pdf)