rm -rf build/ 
rm -rf dist/
pyinstaller -F numpy-cv-test.py
./dist/numpy-cv-test
