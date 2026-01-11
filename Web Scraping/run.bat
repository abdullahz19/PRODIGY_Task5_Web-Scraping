@echo off
REM Web Scraper - Quick Start Batch Script
REM This script activates the virtual environment and runs the scraper

echo.
echo ========================================
echo WEB SCRAPER - SETUP AND RUN
echo ========================================
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
    echo Virtual environment created.
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Install/Update packages
echo.
echo Installing required packages...
pip install -q requests beautifulsoup4 pandas lxml

echo.
echo ========================================
echo Select what to run:
echo ========================================
echo 1. Quick Start Test (books.toscrape.com)
echo 2. Interactive Examples
echo 3. Test Scraper
echo 4. Exit
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    python quickstart.py
) else if "%choice%"=="2" (
    echo.
    python examples.py
) else if "%choice%"=="3" (
    echo.
    python test_scraper.py
) else if "%choice%"=="4" (
    echo Goodbye!
) else (
    echo Invalid choice.
)

echo.
pause
