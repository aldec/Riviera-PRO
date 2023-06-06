# **Python and C++ External Traffic Generators for AI Engine Simulation and Emulation Flows**

## **Steps**

**Step 1.** Building the Design

**Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

**Step 3.** Generating a Code Coverage HTML report

## **Steps 1: Build Design** 

  **1.** Update the paths in the file `system_riviera.cfg`
  
  **2.** Make sure that `check_op` file is executable

  **3.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/tree/2022.1/AI_Engine_Development/Feature_Tutorials/16-external-traffic-generator-aie) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make TARGET=hw_emu EXTIO=true TRAFFIC_GEN=PYTHON clean aie xclbin host package`
  
  If you want to use a macro prepared to display important signals on Waveform and with the possibility of using Code Coverage, then use the file vitis_design_wrapper_sim_wrapper_simulate.do located on GitHub instead of the one generated in Vitis-Tutorials/AI_Engine_Development/Feature_Tutorials/12-axis-traffic-generator/sw/sim/behav_waveform/riviera/. The results shown below are generated using the vitis_design_wrapper_sim_wrapper_simulate.do file from GitHub.

## **Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

  **1.** To launch emulation with the Riviera-PRO Waveform GUI run the following command.  

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

  **6.** Expand signal groups on Waveform.

  - S2MM - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/d97259fc-828b-4735-8de7-6413755aa543)

  - DDR4 - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/c81a0e76-f1a4-4405-ab4b-eeb32bcc9334)

  **7.** Stop simulation.

  Type the `endsim` command in the console.

## **Step 3.** Generate Code Coverage HTML report

  **1.** Update path in:
  
  `acdb report -noinfo -db code_coverage.acdb -replace_path <Example_path>/16-external-traffic-generator-aie <Example_path>/16-external-traffic-generator-aie/_x/link/vivado/vpl/prj/ -html -o code_coverage_report.html` 
  
  **2.** Run `acdb report` to generate the report in html format 
  
  **3.** Open `code_coverage_report.html`
  
  - Sample Summary
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/6df0dec5-03ed-46a3-86d2-17609ed5e4dc)

  - Sample Statement

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/f38f3f2d-2e6a-46fd-b7c7-82d20c803389)

  





