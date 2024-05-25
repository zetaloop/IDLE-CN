@echo off
setlocal EnableDelayedExpansion

:: CD to 'idlecn_build' the build directory
cd /d %~dp0..\..
if not "%cd:~-12%" == "idlecn_build" (
    echo Please run this script in the idlecn_build directory
    exit /b 1
)
echo.
echo ^>^>^> Current directory: %cd%
echo.

:: Create backport patch
echo ^>^>^> Creating backport patch
cd IDLE-CN
cd base
git remote add upstream ../../cpython
git fetch upstream --no-tags
git format-patch -U0 --ignore-all-space upstream/main
cd ../..
echo.

:: Read release_versions.txt to get the versions
echo ^>^>^> Reading 'release_versions.txt' file...
set idlecn_release_error=False
for /f "tokens=1,2" %%a in (.\IDLE-CN\Tools\release_versions.txt) do (
    set idlecn_release_version=%%a
    call :make_release
    if !idlecn_release_error! == True (
        echo ^>^>^> Release [!idlecn_release_version!] failed.
        @REM exit /b 1
    )
    if !idlecn_release_error! == Skip (
        echo ^>^>^> Release [!idlecn_release_version!] skipped.
    )
    echo.
)
echo ^>^>^> Finished making releases :)
echo.
goto :eof


:: Function to make a release
:make_release
cmd /c exit
:: ↑ Reset errorlevel to 0
echo [Info] Making release for [%idlecn_release_version%]...
cd IDLE-CN
mkdir %idlecn_release_version%
if %errorlevel% neq 0 (
    echo [ERROR] Dir %idlecn_release_version% already exists, skip
    cd ..
    set idlecn_release_error=Skip
    goto :eof
)
cd %idlecn_release_version%
git init
git remote add upstream ../../cpython
git fetch upstream --no-tags
if %errorlevel% neq 0 (
    echo [ERROR] git init failed, err %errorlevel%
    cd ../..
    set idlecn_release_error=True
    goto :eof
)
git checkout -t upstream/%idlecn_release_version%
if %errorlevel% neq 0 (
    echo [ERROR] git checkout -t upstream/%idlecn_release_version% failed, err %errorlevel%
    cd ../..
    set idlecn_release_error=True
    goto :eof
)
:: git am ../base/*.patch
:: ↑ Windows does not support globbing
for %%f in (../base/*.patch) do (
    git apply --unidiff-zero --ignore-whitespace --reject --recount ../base/%%f
    if !errorlevel! neq 0 (
        echo [ERROR] Patch failed, err !errorlevel!
        cd ../..
        set idlecn_release_error=True
        goto :eof
    )
    git add .
    git commit -m "Backport patch %%f"
    if !errorlevel! neq 0 (
        echo [ERROR] Commit failed, err !errorlevel!
        cd ../..
        set idlecn_release_error=True
        goto :eof
    )
)
cd ../..
set idlecn_release_error=False
echo [Done] Release [%idlecn_release_version%] is ready.
goto :eof
