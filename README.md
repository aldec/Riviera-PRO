# Running AMD Vitis™ In-Depth Tutorials with Riviera-PRO

1. Requirements
   - Vivado/Vitis 2022.1
   - Petalinux 2022.1
   - Riviera-Pro 2022.10 or newer

2. Simulator Library
   - Generate Xilinx simulation libraries using tutorial below:

     
	 
	 

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
