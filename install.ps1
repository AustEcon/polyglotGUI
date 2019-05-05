pip install virtualenv
python.exe -m virtualenv ..\my_env
..\my_env\Scripts\activate
pip install -r .\requirements.txt
python.exe .\polyglotGUI\polyglot_GUI.py
Read-Host -Prompt "Press Enter to exit"
