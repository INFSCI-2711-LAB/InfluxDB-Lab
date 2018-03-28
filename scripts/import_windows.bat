@echo off
title InfluxDB import demo

set data="%~dp0\..\data\*.txt"

echo.
echo Start importing!
echo.

FOR %%f IN (%data%) DO influx.exe -import -path=%%f -precision=h -database=air

echo.
echo Import finished
echo.
pause
