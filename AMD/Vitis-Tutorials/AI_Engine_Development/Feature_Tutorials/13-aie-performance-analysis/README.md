# **AI Engine Performance and Deadlock Analysis Tutorial**

## **Steps**

**Step 1.** Building the Design

**Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

## **Steps 1: Build Design** 

# **AI Engine Graph Execution and Measurement**

  **1.** `cd 13-aie-performance-analysis/testcase_ssfifo`

  **2.** Update the paths in the file `system_riviera.cfg`

  **3.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/blob/2022.1/AI_Engine_Development/Feature_Tutorials/13-aie-performance-analysis/aie_execution_measurement.md) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make aie aiesim package TARGET=hw`
  
# **AI Engine Deadlock Analysis**

  **1.** `cd 13-aie-performance-analysis/testcase_nofifo_hang`

  **2.** Update the paths in the file `system_riviera.cfg`

  **3.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/blob/2022.1/AI_Engine_Development/Feature_Tutorials/13-aie-performance-analysis/aie_hang_analysis.md) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make aiesim` 

## **Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

  **Step 2.** is the same for all previous steps.

  **1.** To launch emulation with the Riviera-PRO Waveform GUI run the following command.  

  `make run_hw_emu`  
  
  **2.** Add specific signals on Waveform e.g.
  ```
  wave -vgroup "DDR4" -rec sim:/vitis_design_wrapper_sim_wrapper/vitis_design_wrapper_i/vitis_design_i/noc_ddr4/*
	wave -vgroup "S2MM" -rec sim:/vitis_design_wrapper_sim_wrapper/vitis_design_wrapper_i/vitis_design_i/s2mm_1/*
	wave -vgroup "MM2S" -rec sim:/vitis_design_wrapper_sim_wrapper/vitis_design_wrapper_i/vitis_design_i/mm2s_1/*
	wave -vgroup "AI ENGINE" sim:/vitis_design_wrapper_sim_wrapper/vitis_design_wrapper_i/vitis_design_i/ai_engine_0/*
  ```
  **3.** Do `run -all` in Riviera-PRO when simulator is ready.

  **4.** When appear: 

  `root@versal-rootfs-common-20221:~#`

  type in the following commands to launch the tutorial application:
```
  mount /dev/mmcblk0p1 /mnt
  cd /mnt
  ./host.exe a.xclbin
```
  **5.** After some time the test should succeed.
  
  # **AI Engine Graph Execution and Measurement**
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/46cdc9f9-fac5-4761-8996-0cefc1e98daa)

  **5.** To exit QEMU press `Ctrl+A, x`

  **6.** Expand signal groups on Waveform.
  
  - DDR4- Sample signals
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/63978c21-814c-4395-8d23-1e4534783595)
  
  - S2MM - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/ee4d3431-f80d-4fed-a847-509db765a8df)

  - MM2S- Sample signals
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/96f395b2-b1bc-48fb-a73d-7ceb68334a8d)
  
  - AI ENGINE - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/dcefb86f-d798-4624-986b-903df094c865) 
  
  # **AI Engine Deadlock Analysis**
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/029b25a6-1667-4e5b-9317-239c414c3823)

  **5.** To exit QEMU press `Ctrl+A, x`

  **6.** Expand signal groups on Waveform.
  
  - DDR4- Sample signals
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/878fcc16-144a-41cf-9098-59778a1365a8)
  
  - S2MM - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/407a8815-5a66-4e86-b01a-7d22891fa42c)

  - MM2S- Sample signals
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/9f356a41-f348-4d87-89f9-d8da78e195ae)
  
  - AI ENGINE - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/3a0c7747-350e-4ff5-bf6f-f43d442425fd)

  Type the `endsim` command in the console.

  





