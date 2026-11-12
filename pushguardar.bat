@echo off
echo === Iniciando automatizacion de Git ===

pip freeze > requirements.txt && git add . && git commit -m "pagina 131 Configuracion puerto 8000 %DATE% a las %TIME%" && git push origin main

echo === Proceso terminado ===
pause
