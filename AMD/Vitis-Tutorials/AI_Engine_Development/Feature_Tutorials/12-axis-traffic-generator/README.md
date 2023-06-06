# **AXIS External Traffic Generator Feature Tutorial**

## **Steps**

**Step 1.** Building the Design

**Step 2.** Launching Emulation with the Riviera-PRO GUI


## **Steps 1: Build Design** 

  **1.** Update the paths in the file `system_riviera.cfg`
  
  **2.** Download DSP Vitis Library
  
   `./env_setup.sh`

  **3.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/tree/2022.1/AI_Engine_Development/Feature_Tutorials/12-axis-traffic-generator) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make aie xclbin host package`
  
  If you want to use a macro prepared to using Code Coverage, then use the file vitis_design_wrapper_sim_wrapper_simulate.do located on GitHub instead of the one generated in Vitis-Tutorials/AI_Engine_Development/Feature_Tutorials/12-axis-traffic-generator/sw/sim/behav_waveform/riviera/. The results shown below are generated using the vitis_design_wrapper_sim_wrapper_simulate.do file from GitHub.

## **Step 2.** Launching Emulation with the Riviera-PRO GUI

  **1.** To launch emulation with the Riviera-PRO GUI run the following command.  

  `make run_emu`
  
  **2.** Do `run -all` in Riviera-PRO when simulator is ready.

  **3.** When appear: 

  `root@versal-rootfs-common-20221:~#`

  type in the following commands to launch the tutorial application:
```
  cd /run/media/mmcblk0p1
  export XILINX_XRT=/usr
  ./host.exe a.xclbin
```

  **4.** After some time the test should succeed.

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/bc03c823-c663-4161-ab23-fb3c009879a0)
  
  **5.** A matplotlib window will appear that looks as follows:
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/a9d5415d-7640-47dd-8bee-55477ce21c2a)

  **6.** To exit QEMU press `Ctrl+A, x`

  **7.** Stop simulation.

  Type the `endsim` command in the console.


  




