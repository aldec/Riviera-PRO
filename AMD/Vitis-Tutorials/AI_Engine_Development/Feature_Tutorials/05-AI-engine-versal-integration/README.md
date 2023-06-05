# **AI Engine Versal Integration**

## **Steps**

**Step 1.** Building the Design

**Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

**Step 3.** Generating a Code Coverage HTML report

## **Steps 1: Build Design** 

  **1.** Update the paths in the file `system_riviera.cfg`

  **2.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/tree/2022.1/AI_Engine_Development/Feature_Tutorials/05-AI-engine-versal-integration) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make TARGET=hw_emu aie sim kernels xsa host package`
  
  If you want to use a macro prepared to display important signals on Waveform and with the possibility of using Code Coverage, then use the file vitis_design_wrapper_sim_wrapper_simulate.do located on GitHub instead of the one generated in Vitis-Tutorials/AI_Engine_Development/Feature_Tutorials/05-AI-engine-versal-integration/sw/sim/behav_waveform/riviera/. The results shown below are generated using the vitis_design_wrapper_sim_wrapper_simulate.do file from GitHub.

## **Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

  **1.** To launch emulation with the Riviera-PRO Waveform GUI run the following command.  

  `make TARGET=hw_emu run_emu`
  
  **2.** Do `run -all` in Riviera-PRO when simulator is ready.

  **3.** When appear: 

  `root@versal-rootfs-common-20221:~#`

  type in the following commands to launch the tutorial application:
```
  cd /run/media/*1

  export XILINX_XRT=/usr

  ./host.exe a.xclbin
```
  **4.** After some time the test should succeed.

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/483afa0c-1787-4b06-9b49-e97276de1066)

  **5.** To exit QEMU press `Ctrl+A, x`

  **6.** Expand signal groups on Waveform.

  - S2MM - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/d97259fc-828b-4735-8de7-6413755aa543)

  - DDR4 - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/c81a0e76-f1a4-4405-ab4b-eeb32bcc9334)

  **7.** Stop simulation.

  Type the `endsim` command in the console.

## **Step 3.** Generate Code Coverage HTML report

  **1.** Update path in:
  
  `acdb report -noinfo -db code_coverage.acdb -replace_path <Example_path>/05-AI-engine-versal-integration <Example_path>/05-AI-engine-versal-integration/_x/link/vivado/vpl/prj/ -html -o code_coverage_report.html` 
  
  **2.** Run `acdb report` to generate the report in html format 
  
  **3.** Open `code_coverage_report.html`
  
  - Sample Summary
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/f866f11f-056e-461c-95fc-6a5f96e684b9)

  - Sample Statement

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/9a0472a2-f9f3-45da-a551-055a98d2a13f)

  



