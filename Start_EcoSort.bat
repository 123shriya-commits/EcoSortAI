@echo off

cd /d "C:\Users\Shriya mishra\OneDrive\Desktop\EcoSortAI"

echo Starting EcoSort AI...

start "" /B venv\Scripts\python.exe -m streamlit run app.py --server.port 8501

echo Please wait...

timeout /t 5 /nobreak > nul

start "" http://localhost:8501

exit