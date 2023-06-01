# Running AMD Vitis™ In-Depth Tutorials with Riviera-PRO

1. Requirements
   - Vivado/Vitis 2022.1
   - Petalinux 2022.1
   - Riviera-Pro 2023.04

2. Simulator Library
   Generate Xilinx simulation libraries using tutorial below:
   2.1. cd Riviera-PRO-2023.04-x64/etc
   2.2. source setenv
   2.3. source setgcc
   2.4. cd Xilinx/Vivado/2022.1/data/simmodels/riviera/
   2.5. ln -s 2021.04 2023.04
   2.6. Open Vivado.
   2.7. Go to Tools | Compile Simulation Libraries
 
  ![CompVivSimLib_fig1](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/b920c5d1-b591-4db7-9441-be2bebc4e553)
  
  Figure 1: Accessing the Compile Simulation Libraries.
  
   2.8. The Compile Simulation Libraries will open.
   2.9. Select Riviera-PRO under Simulator. Select the desired language and libraries.
   
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/4f31b36e-b6e8-4e15-800a-ca7708206a6c)
  
  Figure 2: Compile Simulation Libraries: Simulator, Language and Library selection. 
  
  2.10. Under the Compiled library location, select the directory where you want the compiled libraries to be saved. Under the Simulator executable path, provide the path to the directory containing the riviera file in the Riviera-PRO installation directory. Under the GCC executable path, provide the path to the directory containing the gcc file in the Riviera-PRO installation directory.
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/dd0533b7-4fcc-4b7a-bf5b-e1c0fb092573)
  
  Figure 3: Compile Simulation Libraries: Compiled library location, Simulator executable path and GCC executable path.
  
  2.11. By default, all the IP modules available in the Vivado IP Catalog are selected for compilation. You can change that behavior by clearing the Compile Xilinx IP check box. When cleared, only the basic simulation libraries are compiled. You may also want to enable recompilation of libraries already present in the output directory. To do so, select the Overwrite the current pre-compiled libraries check box.
  



     
	 
	 

3. Preparing co-simulation files
   1. **Modify config.sh script. Set the proper paths to Riviera-Pro simulator and Xilinx Petalinux tool.**
   2. Run `prepare_files.sh` script (this may take around 30 minutes for the petalinux project to be built)

      `./prepare_files.sh`

4. Running co-simulation

   **NOTE**: Make sure if simulation library for Riviera-Pro simulator is ready
   to use. If not, please rebuild the library under Vivado with Riviera-Pro.
   Check if path to the library for simulation is set correctly in the
   `riviera/sim_top_compile.do` file:

   ```tcl
   set XILINX_LIB_PATH "$env(RIVIERA_PATH)/Xilinx_lib"
   ```

   `./run_example_cosim.sh`

   - The QEMU process should appear in a new terminal window, and in the meantime, the co-simulation in Riviera should begin.

## Limitations:
- Windows is not supported.
- The supported platforms:
  - Red Hat Enterprise Workstation/Server 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.1, 8.2 (64-bit)
  - CentOS Workstation/Server 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.1, 8.2 (64-bit)
  - Ubuntu Linux Workstation/Server 16.04.5, 16.04.6, 18.04.1, 18.04.2, 18.04.3,
    18.04.4,18.04.5, 20.04, 20.04.1 (64-bit)
- The example has been verified to work with operating systems: CentOS 7.x and
  Ubuntu 20.04.
