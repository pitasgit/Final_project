# Final_project
Instalarea si rularea proiectului se face dupa cum urmeaza:

A) Se descarca si instaleaza Google Chrome, proiectul a fost conceput pentru utilizarea cu acesta
B) Se descarca si instaleaza Python
C) Se descarca si instaleaza Pycharm Community Edition
D) Se descarca si instaleaza git
E) In folderul care se doreste a fi clonat, se apasa click dreapta si Git BASH Here
F) Se scrie comanda: git clone https://github.com/pitasgit/Final_project si se apasa ENTER
G) In aplicatia Pycharm deschidem proiectul prin apasarea File-> Open-> my_final_project
H) In terminalul din josul paginii se instaleaza librariile necesare:
	pip install behave + Enter si asteptam confirmarea instalarii
	pip install -U selenium + Enter si asteptam confirmarea instalarii
	pip install webdriver-manager + Enter si asteptam confirmarea instalarii
	pip install behave-html-formatter + Enter si asteptam confirmarea instalarii
I) Cu ajutorul comenzii behave -f html -o report.html --tags=@smoke se genereaza raportul 
J) Raportul va fi accesat din meniul Tree Project prin click dreapta -> Open in -> Browser -> Chrome. 
cu ajutorul -f se selecteaza formatul fisierului output iar cu -o se seteaza numele fisierului output.
