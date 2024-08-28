echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="A:\Ansys\ANSYS Inc\ANSYS Student\v242\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "A:\Ansys\ANSYS Inc\ANSYS Student\v242\fluent\ntbin\win64\tell.exe" DESKTOP-1N5CMU3 61993 CLEANUP_EXITING
timeout /t 1
"A:\Ansys\ANSYS Inc\ANSYS Student\v242\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="DESKTOP-1N5CMU3" (%KILL_CMD% 16684) 
if /i "%LOCALHOST%"=="DESKTOP-1N5CMU3" (%KILL_CMD% 8788) 
if /i "%LOCALHOST%"=="DESKTOP-1N5CMU3" (%KILL_CMD% 11268) 
if /i "%LOCALHOST%"=="DESKTOP-1N5CMU3" (%KILL_CMD% 17760) 
if /i "%LOCALHOST%"=="DESKTOP-1N5CMU3" (%KILL_CMD% 19776) 
if /i "%LOCALHOST%"=="DESKTOP-1N5CMU3" (%KILL_CMD% 7036)
del "C:\Users\mtthl\OneDrive\Documents\Education\Masters Thesis\git\APG_tranpsort\Patrick_CFD\Mesh\cleanup-fluent-DESKTOP-1N5CMU3-19776.bat"
