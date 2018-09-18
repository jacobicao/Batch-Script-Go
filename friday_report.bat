@echo off
cd /d D:\Doc
set a=%date:~12,1%
if "%a%"=="一" set a=1
if "%a%"=="二" set a=2
if "%a%"=="三" set a=3
if "%a%"=="四" set a=4
if "%a%"=="五" set a=5
if "%a%"=="六" set a=-1
if "%a%"=="日" set a=-2
set /a DaysAgo=%a%-5
call :DateToDays %date:~0,4% %date:~5,2% %date:~8,2% PassDays
set /a PassDays-=%DaysAgo%
call :DaysToDate %PassDays% DstYear DstMonth DstDay
set YYYYmmdd=%DstYear%%DstMonth%%DstDay%
if not exist %YYYYmmdd%.txt (
  echo #开始写周报# > %YYYYmmdd%.txt
  msg %username% /TIME:5 周末马上要开始啦，赶紧写个周报吧!
) else (
  msg %username% /TIME:5 周末马上要开始啦，赶紧检查下周报吧！
)
ping localhost -n 3 -w 1000 > nul
start notepad %YYYYmmdd%.txt
goto :eof



:DateToDays %yy%%mm%%dd% days
setlocal ENABLEEXTENSIONS
set yy=%1&set mm=%2&set dd=%3
if 1%yy% LSS 200 if 1%yy% LSS 170 (set yy=20%yy%) else (set yy=19%yy%)
set /a dd=100%dd%%%100, mm=100%mm%%%100
set /a z=14-mm,z/=12,y=yy+4800-z,m=mm+12*z-3,j=153*m+2
set /a j=j/5+dd+y*365+y/4-y/100+y/400-2472633
endlocal&set %4=%j%&goto :EOF


:DaysToDate %days% yy mm dd
setlocal ENABLEEXTENSIONS
set /a a=%1+2472632,b=4*a+3,b/=146097,c=-b*146097,c/=4,c+=a
set /a d=4*c+3,d/=1461,e=-1461*d,e/=4,e+=c,m=5*e+2,m/=153,dd=153*m+2,dd/=5
set /a dd=-dd+e+1,mm=-m/10,mm*=12,mm+=m+3,yy=b*100+d-4800+m/10
(if %mm% LSS 10 set mm=0%mm%)&(if %dd% LSS 10 set dd=0%dd%)
endlocal&set %2=%yy%&set %3=%mm%&set %4=%dd%&goto :EOF
