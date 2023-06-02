# **Versal Emulation Waveform Analysis**

Step 1. Update the paths in the file system_riviera.cfg

Step 2. Please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/tree/2022.1/AI_Engine_Development/Feature_Tutorials/11-ai-engine-emulation-waveform-analysis) or use a short version:

  Step 2.1. Build design
  
  **make aie aiesim kernels xclbin host package**
  
  Step 2.2. If you want to use a macro prepared to display important signals on Waveform and with the possibility of using Code Coverage, then use the file vitis_design_wrapper_sim_wrapper_simulate.do located on GitHub instead of the one generated in Vitis-Tutorials/AI_Engine_Development/Feature_Tutorials/11-ai- engine-emulation-waveform-analysis/sw/sim/behav_waveform/riviera/. The results shown below are generated using the vitis_design_wrapper_sim_wrapper_simulate.do file from GitHub.
  
  Step 2.3. Launching Emulation with Riviera-PRO
  
  **make run_emu**
  
Step 3. Do **run -all** in Riviera-PRO when simulator is ready.

Step 4. When appear: 

**root@versal-rootfs-common-20221:~# **

type in the following commands to launch the tutorial application:

**mount /dev/mmcblk0p1 /mnt**

**cd /mnt**

**./host.exe a.xclbin**

Step 5. After some time the test should succeed.

![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/1f474eed-dfce-4136-87b1-bb30faf95924)

Step 6. To exit QEMU press Ctrl+A, x

Step 7. Expand signal groups on Waveform.

  - CIPS - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/e1d77a08-7a7c-465b-8209-11e2d12fb718)
  
  - NOISE - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/5d6ee09e-49f5-43ed-b9d7-56451a08d568)
  
  - S2MM - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/3ea7aa3c-67a4-4054-b5af-1e27f3252901)

  - DDR4 - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/0b998bed-6f2f-4064-8caf-c860964b2cb8)

Step 8. Stop simulation.

Type the **endsim** command in the console.

Step 9. Generate Code Coverage HTML report.

  Step 9.1. Update path in:
  
  acdb report -noinfo -db code_coverage.acdb -replace_path <Example_path>/11-ai-engine-emulation-waveform-analysis <Example_path>/11-ai-engine-emulation-waveform-analysis/_x/link/vivado/vpl/prj -html -o code_coverage_report.html 
  
  Step 9.2. Run **acdb report** to generate the report in html format 
  
  Step 9.3. Open code_coverage_report.html
  
  - Sample Summary
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/22157b9e-3763-4bdd-a517-c7e92031def3)

  - Sample Statement

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/5fd13fd9-1bec-47e7-8c66-b92cf69554ad)

  


