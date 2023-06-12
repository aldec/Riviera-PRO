# **AI Engine Debug Walkthrough Tutorial - From Simulation to Hardware**

## **Steps**

**Step 1.** Building the Design

**Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

## **Steps 1: Build Design** 

  **1.** Update the paths in the file `system_riviera.cfg`
  
  **2.** Download beamformer data from [here](https://www.xilinx.com/bin/public/openDownload?filename=beamformer_d) and extract to ./09-debug-walkthrough

  **3.** To build the design run the following command
  
  `make aie aiesim xsa host package`

## **Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

  **1.** To launch emulation with the Riviera-PRO Waveform GUI run the following command.  

  `make run_hw_emu`
  
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

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/545ca629-d3c5-4e8c-b574-ed095727f689)

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/15783178-c800-450c-b589-dcabe792d32c)

  **5.** To exit QEMU press `Ctrl+A, x`

  **6.** Expand signal groups on Waveform.

  - S2MM - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/d97259fc-828b-4735-8de7-6413755aa543)

  - DDR4 - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/c81a0e76-f1a4-4405-ab4b-eeb32bcc9334)
  
  - AI ENGINE  - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/d67d0ba9-a430-4235-9511-8ba90e61a0ae)
  
  **7.** Type the `endsim` command in the console.

