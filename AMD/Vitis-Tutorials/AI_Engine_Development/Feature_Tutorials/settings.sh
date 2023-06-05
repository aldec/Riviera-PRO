#! /bin/bash
#Set up your PLATFORM_REPO_PATHS environment variable based upon where you downloaded the platform.
export PLATFORM_REPO_PATHS=

#Set up your platform
export PLATFORM=${PLATFORM_REPO_PATHS}/xilinx_vck190_base_202210_1/xilinx_vck190_base_202210_1.xpfm

#Set up your ROOTFS to point to xilinx-versal-common-v2022.1/rootfs.ext4.
export ROOTFS=${PLATFORM_REPO_PATHS}/rootfs.ext4

#Set up your IMAGE to point to xilinx-versal-common-v2022.1/Image.
export IMAGE=${PLATFORM_REPO_PATHS}/Image

#Set up your LM_LICENSE_FILE to point to Xilinx license
export LM_LICENSE_FILE=

#Set up your ALDEC_LICENSE_FILE to point to Riviera-PRO license
export ALDEC_LICENSE_FILE=

#Set up your PATH to point to builded XRT
export PATH=<Petalinux_path>/Petalinux/2022.1/sysroots/x86_64-petalinux-linux/usr/bin/aarch64-xilinx-linux:<XRT_path>/XRT/build/Release/opt/xilinx/xrt/include/:$PATH

#Set up your SYSROOT to point to sysroots in Petalinux
export SYSROOT=<Petalinux_path>/Petalinux/2022.1/sysroots

#Set up environment for XRT
cd <XRT_path>/XRT/build/Release/opt/xilinx/xrt
source setup.sh

#Set up environment for SDKTARGETSYSROOT, CC, CXX and CPP
export SDKTARGETSYSROOT=<Petalinux_path>/Petalinux/2022.1/sysroots/cortexa72-cortexa53-xilinx-linux
export CC="aarch64-xilinx-linux-gcc  -mcpu=cortex-a72.cortex-a53 -march=armv8-a+crc -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security --sysroot=$SDKTARGETSYSROOT"
export CXX="aarch64-xilinx-linux-g++  -mcpu=cortex-a72.cortex-a53 -march=armv8-a+crc -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security --sysroot=$SDKTARGETSYSROOT"
export CPP="aarch64-xilinx-linux-gcc -E  -mcpu=cortex-a72.cortex-a53 -march=armv8-a+crc -fstack-protector-strong  -O2 -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security --sysroot=$SDKTARGETSYSROOT"

#Set up environment for Vitis
cd <Vitis_path>/Vitis/2022.1
source settings64.sh

#Set up environment for PYTHONPATH
export PYTHONPATH=${XILINX_VIVADO}/data/emulation/hw_em/lib/python/:${XILINX_VIVADO}/data/emulation/ip_utils/xtlm_ipc/xtlm_ipc_v1_0/python/:${PYTHONPATH}

#Set up environment for DSPLIB_ROOT
export DSPLIB_ROOT=<Vitis_Libraries_path>/Vitis_Libraries/dsp/
