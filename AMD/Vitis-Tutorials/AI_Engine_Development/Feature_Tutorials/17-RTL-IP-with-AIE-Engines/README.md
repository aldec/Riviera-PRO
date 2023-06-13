# **Using RTL IP with AI Engines**

## **Steps**

**Step 1.** Building the Design

**Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

**Step 3.** Generating a Code Coverage HTML report

**Step 4.** Advanced Dataflow

## **Steps 1: Build Design** 

  **1.** Update the paths in the file `system_riviera.cfg`

  **2.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/tree/2022.1/AI_Engine_Development/Feature_Tutorials/17-RTL-IP-with-AIE-Engines) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make polar_clip.xo kernels aie xclbin host package`
  
  If you want to use a macro prepared to display important signals on Waveform and with the possibility of using Code Coverage or Advanced Dataflow, then use the file vitis_design_wrapper_sim_wrapper_simulate.do located on GitHub instead of the one generated in Vitis-Tutorials/AI_Engine_Development/Feature_Tutorials/17-RTL-IP-with-AIE-Engines/sw/sim/behav_waveform/riviera/. The results shown below are generated using the vitis_design_wrapper_sim_wrapper_simulate.do file from GitHub.

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
  ./host.exe a.xclbin
```
  **4.** After some time the test should succeed.

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/d0397fd2-71ff-40eb-ba1f-8f4f91af27d1)

  **5.** To exit QEMU press `Ctrl+A, x`

  **6.** Expand signal groups on Waveform.
  
  - CIPS - Sample signals
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/87dd5fb3-188a-427b-8bb0-59a9a6fbef78)

  - S2MM - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/dd9dc2c8-f9d8-403b-9b92-61824348e271)

  - DDR4 - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/cddf3735-119c-4cda-93f0-5c63dd6ac861)
  
  - AI ENGINE - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/2d7559d5-29c2-4b56-b570-5dae03cbc00a)

  **7.** Go to Step.4 if you want use Advanced Dataflow. Otherwise type the `endsim` command in the console.

## **Step 3.** Generate Code Coverage HTML report

  **1.** Update path in:
  
  `acdb report -noinfo -db code_coverage.acdb -replace_path <Example_path>/17-RTL-IP-with-AIE-Engines <Example_path>/17-RTL-IP-with-AIE-Engines/_x/link/vivado/vpl/prj/ -html -o code_coverage_report.html` 
  
  **2.** Run `acdb report` to generate the report in html format 
  
  **3.** Open `code_coverage_report.html`
  
  - Sample Summary
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/a7e612af-87c7-4cb0-96d4-77dc788ecfcc)

  - Sample Statement

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/4c44348e-885e-45f5-a532-3c19d23b441a)

## **Step 4.** Advanced Dataflow

  **1.** Select from Waveform interesting signal. Right-click on it then `Add to` and `Dataflow`

  **2.** The Dataflow window displays interconnects of an active design. The primary purpose is to explore the connectivity of the design. Below is an example fragment of Dataflow window on the signal from the module S2MM
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/c2d2d6c8-2bc8-4063-98ed-d403d502c9ec)




