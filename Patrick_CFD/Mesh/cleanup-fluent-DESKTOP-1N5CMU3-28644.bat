echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="A:\Ansys\ANSYS Inc\ANSYS Student\v242\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "A:\Ansys\ANSYS Inc\ANSYS Student\v242\fluent\ntbin\win64\tell.exe" DESKTOP-1N5CMU3 51166 CLEANUP_EXITING
timeout /t 1
"A:\Ansys\ANSYS Inc\ANSYS Student\v242\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="DESKTOP-1N5CMU3" (%KILL_CMD% 29420) 
if /i "%LOCALHOST%"=="DESKTOP-1N5CMU3" (%KILL_CMD% 1812) 
if /i "%LOCALHOST%"=="DESKTOP-1N5CMU3" (%KILL_CMD% 1352) 
if /i "%LOCALHOST%"=="DESKTOP-1N5CMU3" (%KILL_CMD% 29448) 
if /i "%LOCALHOST%"=="DESKTOP-1N5CMU3" (%KILL_CMD% 28644) 
if /i "%LOCALHOST%"=="DESKTOP-1N5CMU3" (%KILL_CMD% 1416)
del "C:\Users\mtthl\OneDrive\Documents\Education\Masters Thesis\git\APG_tranpsort\Patrick_CFD\Mesh\cleanup-fluent-DESKTOP-1N5CMU3-28644.bat"
