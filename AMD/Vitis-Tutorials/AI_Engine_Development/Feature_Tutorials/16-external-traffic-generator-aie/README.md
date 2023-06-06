# **Python and C++ External Traffic Generators for AI Engine Simulation and Emulation Flows**

## **Steps**

**Step 1.** Building the Design with 

**Step 2.** Launching Emulation with the Riviera-PRO GUI

## **Steps 1: Build Design** 

  **1.** Update the paths in the file `system_riviera.cfg`
  
  **2.** Make sure that `check_op` file is executable

  **3.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/tree/2022.1/AI_Engine_Development/Feature_Tutorials/16-external-traffic-generator-aie) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make TARGET=hw_emu EXTIO=true TRAFFIC_GEN=PYTHON clean aie xclbin host package`

## **Step 2.** Launching Emulation with the Riviera-PRO GUI

  **1.** To launch emulation with the Riviera-PRO GUI run the following command.  

  `make TARGET=hw_emu EXTIO=true TRAFFIC_GEN=PYTHON run_emu`
  
  **2.** Do `run -all` in Riviera-PRO when simulator is ready.

  **3.** When appear: 

  `root@versal-rootfs-common-20221:~#`

  type in the following commands to launch the tutorial application:
```
  mount /dev/mmcblk0p1 /mnt
  cd /mnt
  ./host.exe a.xclbin
```

  **4.** After some time the test should finished.

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/ec7bfce4-c9b4-4d7d-9033-80e2327e9344)

  **5.** To exit QEMU press `Ctrl+A, x`
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/bff80d3a-d9d7-4e75-8308-5a88a59cef9f)

  





