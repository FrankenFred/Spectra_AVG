# Spectra_AVG
Script is designed to average multiple spectra recorded under same base file name – here “ICCD_X_Y.txt”, where X = base file number and Y = frame or spectra number. The script reads in all files with the same X and different Y, averages the spectra, and exports a two column average file “AVG_CCD_X.txt”, containing the wavelength and average intensity. Input files must be two columns – pixel and intensity. Wavelength calibration is applied in the processing and so the wavelength calibration and center wavelength for the CCD must be set in the python file prior to analysis. Base file name does not need to be “ICCD_”, and this can be adjusted in the Python file.

For example, 20 spectra recorded in the same SPE file – when exported to ASCII from WinSpec32, each frame can be exported as a separate “*.txt” file.

SPE file: “ICCD_1.SPE” (contains 20 frames, or separate spectra)
Text files: “ICCD_1_1.txt”, “ICCD_1_2.txt”…. “ICCD_1_20.txt”

### Example process:
* Make sure WinSpec has exported the SPE files require to ASCII – separate file per frame, 2 column (pixel, intensity)
* Check “CCD_Cal_sort.py” is configured correctly (wavelength calibration, base file name etc.)
* Copy the spectra text files required into the same directory as the  “CCD_Cal_sort.py” Python script.
* Run “CCD_Cal_sort.py” – can be double clicked or run from Terminal/Command line.
* Script currently has no printed output – so no message, no problem.
* “AVG_CCD_X.txt” files should appear with same X as input files.

