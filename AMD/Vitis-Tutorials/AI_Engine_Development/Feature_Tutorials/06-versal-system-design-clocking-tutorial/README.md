# **Versal System Design Clocking**

## **Steps**

**Step 1.** Building the Design

**Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

## **Steps 1: Build Design** 

  **1.** Update the paths in the file `system_riviera.cfg`

  **2.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/tree/2022.1/AI_Engine_Development/Feature_Tutorials/06-versal-system-design-clocking-tutorial) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make aie kernels xclbin host package`
  
  If you want to use a macro prepared to display important signals on Waveform and with the possibility of using Code Coverage, then use the file vitis_design_wrapper_sim_wrapper_simulate.do located on GitHub instead of the one generated in Vitis-Tutorials/AI_Engine_Development/Feature_Tutorials/05-AI-engine-versal-integration/sw/sim/behav_waveform/riviera/. The results shown below are generated using the vitis_design_wrapper_sim_wrapper_simulate.do file from GitHub.

## **Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

  **1.** To launch emulation with the Riviera-PRO Waveform GUI run the following command.  

  `make run_emu`
  
  **2.** Do `run -all` in Riviera-PRO when simulator is ready.

  **3.** When appear: 

  `root@versal-rootfs-common-20221:~#`

  type in the following commands to launch the tutorial application:
```
  mount /dev/mmcblk0p1 /mnt
  cd /mnt
  export XILINX_XRT=/usr
  ./host.exe a.xclbin
```
  **4.** After some time the test should succeed.

  **5.** To exit QEMU press `Ctrl+A, x`
