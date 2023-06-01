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
   
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/9a57cea3-abb5-44f2-b05b-1deb8abb721d)
  
  Figure 2: Compile Simulation Libraries: Simulator, Language and Library selection. 
  
  2.10. Under the Compiled library location, select the directory where you want the compiled libraries to be saved. Under the Simulator executable path, provide the path to the directory containing the riviera file in the Riviera-PRO installation directory. Under the GCC executable path, provide the path to the directory containing the gcc file in the Riviera-PRO installation directory.
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/95f74d99-1efa-4635-bf9d-66ca63e65d3c)
  
  Figure 3: Compile Simulation Libraries: Compiled library location, Simulator executable path and GCC executable path.
  
  2.11. By default, all the IP modules available in the Vivado IP Catalog are selected for compilation. You can change that behavior by clearing the Compile Xilinx IP check box. When cleared, only the basic simulation libraries are compiled. You may also want to enable recompilation of libraries already present in the output directory. To do so, select the Overwrite the current pre-compiled libraries check box.
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/1ae687b1-48b2-4390-ba25-8dec3d47f0d8)

  Figure 4: Compile Simulation Libraries: Compile Xilinx IP and Overwrite the current pre-compiled libraries. 
  
  2.12. When you have specified all of your settings, select Compile.
  
  ![image](https://github.com/maciejpasierbek/Riviera-PRO/assets/38097741/601f2e07-a089-4eb4-a592-fc4b7a76fdf0)

  Figure 5: Compile Simulation Libraries: Compile.



     
