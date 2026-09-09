@echo off
cd /d "%~dp0"

echo Starting EcoSort AI...

start "" /B venv\Scripts\python.exe -m streamlit run app.py --server.port 8501

timeout /t 5 /nobreak > nul

start "" http://localhost:8501

exit
