@echo off

IF EXIST "config.py" (

echo buduje venv...
python -m venv venv

echo instaluje potrzebne biblioteki z requirements.txt...
venv\Scripts\pip.exe install -r requirements.txt

echo instaluje baze danych...
venv\Scripts\python.exe setup.py

echo wrzucam dane testowe...
venv\Scripts\python.exe testdata.py

echo Gotowe. Uruchom "venv\Scripts\python.exe main.py" z linii polecen

) ELSE (

echo config.py not found && pause

)

pause
