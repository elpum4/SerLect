del dist /f /q
del build /f /q
pyinstaller --path=d:\temp\eclipse\LibA5\A5 SerLect.py -w --icon=serial.ico  --exclude Click 
copy SerLect.ini Dist\SerLect\.
cd dist\SerLect
pause