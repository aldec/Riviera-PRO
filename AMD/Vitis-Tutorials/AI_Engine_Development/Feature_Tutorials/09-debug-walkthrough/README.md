# **AI Engine Debug Walkthrough Tutorial - From Simulation to Hardware**

## **Steps**

**Step 1.** Building the Design

**Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

## **Steps 1: Build Design** 

  **1.** Update the paths in the file `system_riviera.cfg`
  
  **2.** Download beamformer data from [here](https://www.xilinx.com/bin/public/openDownload?filename=beamformer_2022_1.ide.zip) and extract to ./09-debug-walkthrough

  **3.** To build the design run the following command
  
  `make aie aiesim xsa host package`

## **Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

  **1.** To launch emulation with the Riviera-PRO Waveform GUI run the following command.  

  `make run_hw_emu`
  
  **2.** Add specific signals on Waveform e.g.
  ```
  wave -vgroup "DDR4" -rec sim:/vitis_design_wrapper_sim_wrapper/vitis_design_wrapper_i/vitis_design_i/noc_ddr4/*
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

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/545ca629-d3c5-4e8c-b574-ed095727f689)

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/15783178-c800-450c-b589-dcabe792d32c)

  **6.** To exit QEMU press `Ctrl+A, x`

  **7.** Expand signal groups on Waveform.

  - DDR4 - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/758387d1-25f1-49a7-967e-861289ab0de4)
  
  - AI ENGINE  - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/fa00c205-902e-4a40-9890-d852771ed8eb)

  **7.** Stop simulation.
  
  Type the `endsim` command in the console.

