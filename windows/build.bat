
copy installer.iss ..

cd ..

python setup.py py2exe -w --icon images\kodos_icon.ico

"c:\program files\inno setup 4\ISCC.exe" "installer.iss"
