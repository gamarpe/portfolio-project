@echo off
cls
echo ===================================================
echo   1. BAJANDO CODIGO Y DATOS DESDE GITHUB (PULL)
echo ===================================================
git pull

echo.
echo ===================================================
echo   2. INSTALANDO LIBRERIAS NUEVAS O ACTUALIZADAS
echo ===================================================
:: Compara el archivo requirements.txt e instala lo que falte
python -m pip install --upgrade --force-reinstall pip && pip install -r requirements.txt



echo.
echo [PROCESO TERMINADO] .
pause
