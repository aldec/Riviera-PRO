# **Post-Link Recompile of an AI Engine Application**

# **Lab 1: Direct AI Engine Recompile Makefile Flow**

## **Steps**

**Step 1.** Phase 1: Compile AI Engine application and PL Kernels and Link the System

**Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

**Step 3.** Generating a Code Coverage HTML report

## **Steps 1.  Phase 1: Compile AI Engine application and PL Kernels and Link the System** 

  **1.** Update the paths in the file `system_riviera.cfg`

  **2.** To build the design please follow the steps described [here](https://github.com/Xilinx/Vitis-Tutorials/blob/2022.1/AI_Engine_Development/Feature_Tutorials/15-post-link-recompile/DirectRecompileMakefile_Flow.md) and then go to **Step 2.** or use the short version below:

  To build the design run the following command
  
  `make kernels aie link`
  
  If you want to use a macro prepared to display important signals on Waveform and with the possibility of using Code Coverage, then use the file vitis_design_wrapper_sim_wrapper_simulate.do located on GitHub instead of the one generated in Vitis-Tutorials/AI_Engine_Development/Feature_Tutorials/15-post-link-recompile/WithoutIntermediatePlatform/sim/behav_waveform/riviera/. The results shown below are generated using the vitis_design_wrapper_sim_wrapper_simulate.do file from GitHub.

## **Step 2.** Launching Emulation with the Riviera-PRO Waveform GUI

  **1.** To launch emulation with the Riviera-PRO Waveform GUI run the following command.  

  `make clean phase1 package run_emu`
  
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

## **Step 3.** Generate Code Coverage HTML report

  **1.** Update path in:
  
  `acdb report -noinfo -db code_coverage.acdb -replace_path <Example_path>/05-AI-engine-versal-integration <Example_path>/05-AI-engine-versal-integration/_x/link/vivado/vpl/prj/ -html -o code_coverage_report.html` 
  
  **2.** Run `acdb report` to generate the report in html format 
  
  **3.** Open `code_coverage_report.html`
  
  - Sample Summary
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/f866f11f-056e-461c-95fc-6a5f96e684b9)

  - Sample Statement

  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/9a0472a2-f9f3-45da-a551-055a98d2a13f)

  




