
copy installer.iss ..

cd ..
python setup.py py2exe -w --icon images\kodos_icon.ico
x
"c:\program files\inno setup 4\ISCC.exe" "installer.iss"
