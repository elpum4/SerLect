del dist /f /q
del build /f /q
pyinstaller SerLect.spec
copy SerLect.ini Dist\SerLect\.
cd dist\SerLect
pause