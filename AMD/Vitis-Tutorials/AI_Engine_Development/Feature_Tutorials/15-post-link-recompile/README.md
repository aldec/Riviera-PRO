# **Post-Link Recompile of an AI Engine Application**

# **Lab 1: Direct AI Engine Recompile Makefile Flow**

## **Steps**

**Step 1.** Phase 1: Compile AI Engine application and PL Kernels and Link the System

**Step 2.** Phase 1: Launching Emulation with the Riviera-PRO Waveform GUI

**Step 3.** Phase 1: Generating a Code Coverage HTML report

**Step 4.** Phase 2: Recompile the AI Engine Application, Package the New System, and Rerun Hardware Emulation

**Step 5.** Phase 2: Launching Emulation with the Riviera-PRO Waveform GUI

**Step 6.** Phase 2: Generating a Code Coverage HTML report

## **Steps 1.  Phase 1: Compile AI Engine application and PL Kernels and Link the System** 

  **1.** Update the paths in the file `system_riviera.cfg` in /15-post-link-recompile/Files/HwLink directory

  **2.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/blob/2022.1/AI_Engine_Development/Feature_Tutorials/15-post-link-recompile/DirectRecompileMakefile_Flow.md) and then go to **Step 2.** or use the short version below:

  To build the design run the following commands
  ```
  cd 15-post-link-recompile/WithoutIntermediatePlatform/
  make kernels aie link host package
  ```
  
  If you want to use a macro prepared to display important signals on Waveform and with the possibility of using Code Coverage, then use the file vitis_design_wrapper_sim_wrapper_simulate.do located on GitHub instead of the one generated in Vitis-Tutorials/AI_Engine_Development/Feature_Tutorials/15-post-link-recompile/WithoutIntermediatePlatform/sim/behav_waveform/riviera/. The results shown below are generated using the vitis_design_wrapper_sim_wrapper_simulate.do file from GitHub.

## **Step 2.** Phase 1: Launching Emulation with the Riviera-PRO Waveform GUI

  **1.** To launch emulation with the Riviera-PRO Waveform GUI run the following command.  

  `make run_emu`
  
  **2.** Do `run -all` in Riviera-PRO when simulator is ready.

  **3.** After `run -all` the test will run automatically. Below are the results: 

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/11c4ff92-5532-4a87-8037-63fd75d2a0b6)
  
  **4.** After some time the following should be displayed:

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/9706a16c-77d1-4c7b-aba1-9a30b2f7d597)

  **5.** Expand signal groups on Waveform.

  - CIPS - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/8ba1ac0a-426f-43b3-8615-7b892fe8d3aa)

  - DDR4 - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/7a7ab2c9-8471-4e48-a080-2215dbf4d13e)

  **6.** Stop simulation.

  Type the `endsim` command in the console.

## **Step 3.** Phase 1: Generate Code Coverage HTML report

  **1.** Update path in:
  
  `acdb report -noinfo -db code_coverage.acdb -replace_path <Example_path>/15-post-link-recompile <Example_path>/15-post-link-recompile/WithoutIntermediatePlatform/_x/link/vivado/vpl/prj -html -o code_coverage_report.html` 
  
  **2.** Run `acdb report` to generate the report in html format 
  
  **3.** Open `code_coverage_report.html`
  
  - Sample Summary
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/be1db294-20e3-4fdf-bf14-1b3c5d1cdbae)

  - Sample Statement

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/2f33c003-c366-4cdc-a8b2-b8f73b45b610)

## **Steps 4.  Phase 2: Recompile the AI Engine Application, Package the New System, and Rerun Hardware Emulation** 

  **1.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/blob/2022.1/AI_Engine_Development/Feature_Tutorials/15-post-link-recompile/DirectRecompileMakefile_Flow.md) and then go to **Step 5.** or use the short version below:

  To build the design run the following commands

  `make aie2 package2`
  
  If you want to use a macro prepared to display important signals on Waveform and with the possibility of using Code Coverage, then use the file vitis_design_wrapper_sim_wrapper_simulate.do located on GitHub instead of the one generated in Vitis-Tutorials/AI_Engine_Development/Feature_Tutorials/15-post-link-recompile/WithoutIntermediatePlatform/sim/behav_waveform/riviera/. The results shown below are generated using the vitis_design_wrapper_sim_wrapper_simulate.do file from GitHub.

## **Step 5.** Phase 2: Launching Emulation with the Riviera-PRO Waveform GUI

  **1.** To launch emulation with the Riviera-PRO Waveform GUI run the following command.  

  `make run_emu`
  
  **2.** Do `run -all` in Riviera-PRO when simulator is ready.

  **3.** After `run -all` the test will run automatically. Below are the results: 

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/f6a1f01f-fd3c-4950-8c6f-5c6c11b64e71)
  
  **4.** After some time the following should be displayed:

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/c2f04481-690f-4a0b-8279-65420e76bf7c)

  **5.** Expand signal groups on Waveform.

  - CIPS - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/8ba1ac0a-426f-43b3-8615-7b892fe8d3aa)

  - DDR4 - Sample signals

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/7a7ab2c9-8471-4e48-a080-2215dbf4d13e)

  **6.** Stop simulation.

  Type the `endsim` command in the console.

## **Step 6.** Phase 2: Generate Code Coverage HTML report

  **1.** Update path in:
  
  `acdb report -noinfo -db code_coverage.acdb -replace_path <Example_path>/15-post-link-recompile <Example_path>/15-post-link-recompile/WithoutIntermediatePlatform/_x/link/vivado/vpl/prj -html -o code_coverage_report.html` 
  
  **2.** Run `acdb report` to generate the report in html format 
  
  **3.** Open `code_coverage_report.html`
  
  - Sample Summary
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/be1db294-20e3-4fdf-bf14-1b3c5d1cdbae)

  - Sample Statement

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/2f33c003-c366-4cdc-a8b2-b8f73b45b610)
  




