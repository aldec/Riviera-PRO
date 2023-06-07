# **Runtime Parameter Reconfiguration**

## **Steps**

**Step 1.** Building the Design

**Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

## **Steps 1: Build Design** 

# **Synchronous Update of Scalar RTP**

  **1.** `cd 03-rtp-reconfiguration/step1`

  **2.** Update the paths in the file `system_riviera.cfg`

  **3.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/blob/2022.1/AI_Engine_Development/Feature_Tutorials/03-rtp-reconfiguration/step1_sync_scalar.md) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make aie aiesim kernels host package`
  
# **Asynchronous Update of Array RTP**

  **1.** `cd 03-rtp-reconfiguration/step2`

  **2.** Update the paths in the file `system_riviera.cfg`

  **3.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/blob/2022.1/AI_Engine_Development/Feature_Tutorials/03-rtp-reconfiguration/step2_async_scalar.md) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make aie aiesim package`
  
# **Asynchronous Update of Scalar RTP**

  **1.** `cd 03-rtp-reconfiguration/step3`

  **2.** Update the paths in the file `system_riviera.cfg`

  **3.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/blob/2022.1/AI_Engine_Development/Feature_Tutorials/03-rtp-reconfiguration/step3_async_array.md) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  ```
  make aie 
  make aiesim 
  make -C pl_kernels
  ```
  
# **Asynchronous Update of Array RTP for AI Engine Kernel**

  **1.** `cd 03-rtp-reconfiguration/step4`

  **2.** Update the paths in the file `system_riviera.cfg`

  **3.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/blob/2022.1/AI_Engine_Development/Feature_Tutorials/03-rtp-reconfiguration/step4_async_aie_array.md) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make aie aiesim host`
  
# **Asynchronous Array RTP Update and Read for AI Engine Kernel**

  **1.** `cd 03-rtp-reconfiguration/step5`

  **2.** Update the paths in the file `system_riviera.cfg`

  **3.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/blob/2022.1/AI_Engine_Development/Feature_Tutorials/03-rtp-reconfiguration/step5_async_array_update_read.md) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make aie aiesim host`  

## **Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

  **Step 2.** is the same for all previous steps.

  **1.** To launch emulation with the Riviera-PRO Waveform GUI run the following command.  

  `make run_hw_emu`  
  
  **2.** Add specific signals on Waveform e.g.
  ```
  wave -vgroup "AI ENGINE" sim:/vitis_design_wrapper_sim_wrapper/vitis_design_wrapper_i/vitis_design_i/ai_engine_0/*
  wave -vgroup "DDR4" -rec sim:/vitis_design_wrapper_sim_wrapper/vitis_design_wrapper_i/vitis_design_i/noc_ddr4/*
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
  
  # **Synchronous Update of Scalar RTP**
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/2dccf03f-b4d5-41cf-a95b-cee712e6f6d0)

  **5.** To exit QEMU press `Ctrl+A, x`

  **6.** Expand signal groups on Waveform.
  
  - AI ENGINE- Sample signals
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/f4349897-2a4a-4156-8d06-b8ff4f5e7a96)
  
  - DDR4 - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/556b4a90-63ef-40b6-a1cd-ca1dce112e71)
  
  # **Asynchronous Update of Array RTP**
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/a06f333a-2e24-4049-b01a-bbdffaa7e0b5)

  **5.** To exit QEMU press `Ctrl+A, x`

  **6.** Expand signal groups on Waveform.
  
  - AI ENGINE- Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/b5a8e5c8-907d-47a7-8dde-271e63525b5f)
  
  - DDR4 - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/1112762e-7703-4883-b60b-70720222a0b4)
  
  # **Asynchronous Update of Scalar RTP**
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/d7640668-734c-4762-ba60-f1f993da612f)

  **5.** To exit QEMU press `Ctrl+A, x`

  **6.** Expand signal groups on Waveform.
  
  - AI ENGINE- Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/65f74fef-db7e-4c3d-90b8-caf071911898)
  
  - DDR4 - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/a66f28f4-dbd4-49d2-9c52-2783f1c62e48)
  
  # **Asynchronous Update of Array RTP for AI Engine Kernel**
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/b8b2b42a-416a-4adc-a67f-f68ed6faacc6)

  **5.** To exit QEMU press `Ctrl+A, x`

  **6.** Expand signal groups on Waveform.
  
  - AI ENGINE- Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/1205b782-0bbb-4a29-b10d-6cc6f0ff66d2)
  
  - DDR4 - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/8f522103-e233-437b-9971-6ada3237f6e3)
 
   # **Asynchronous Array RTP Update and Read for AI Engine Kernel**
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/a00e4829-c030-4b8b-b8a7-17d7b09ce1c5)

  **5.** To exit QEMU press `Ctrl+A, x`

  **6.** Expand signal groups on Waveform.
  
  - AI ENGINE- Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/55f20be5-3f24-48dd-b9c9-61f8ce008493)
  
  - DDR4 - Sample signals

   ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/61550d2a-6052-4d95-957f-b2f9e3c5aea3)
  
  **7.** Stop simulation.

  Type the `endsim` command in the console.

  





