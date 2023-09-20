# Referat Thema Nummer 7

## Django

- https://docs.djangoproject.com/en/4.2/intro/overview/#

## [Start me up](https://www.youtube.com/watch?v=SGyOaCXr8Lw)
#### 1. Falls du Vs Code benutzt und auf deinem System eine Docker Engine läuft.

- Öffne das Projekt als Devcontainer
- Starte den Entwicklungsserver 

        cd djangoApp/
        python3 manage.py runserver


- Du solltest nun unter 127.0.0.1:8000 den Entwicklungsserver erreichen können

---
#### 2. Falls du lokal arbeitest und VsCode nutzt.

  - Öffne den Workspace, welchen du im .vscode Ordner findest
  - Verifiziere, dass du eine gültige Python3.11.X Installation auf deinem System hast

        python3 -V
            
        -> Python 3.11.5

- Drücke Strg+alt+P und führe den Task **Erstinstallation** aus

- Starte den Entwicklungsserver 

        cd djangoApp/
        python3 manage.py runserver

- Du solltest nun unter 127.0.0.1:8000 den Entwicklungsserver erreichen können        
---
#### 3. Falls du lokal arbeitest und kein VsCode nutzt.

- Öffne das Projekt
- Verifiziere, dass du eine gültige Python3.11.X Installation auf deinem System hast

        python3 -V
        
        -> Python 3.11.5

- Installiere die Abhängigkeiten

        python3 -m pip install -r requirements.txt

- Migriere die Datenbank 


        cd djangoApp/
        python3 manage.py migrate

- Starte den Entwicklungsserver 

        python3 manage.py runserver

- Du solltest nun unter 127.0.0.1:8000 den Entwicklungsserver erreichen können        


### Anlagen zu diesem Abschnitt

[Der Entwicklungsserver](https://docs.djangoproject.com/en/4.2/intro/tutorial01/#the-development-server)
[Datenbanken installieren](https://docs.djangoproject.com/en/4.2/intro/tutorial01/#the-development-server)
    
---
#### 4. Falls du einen DevContainer benutzen möchtest aber kein VsCode nutzt.

- Öffne das Projekt als Devcontainer

- Führe das PostCreateCommand aus

        sh ./.devcontainer/postCreateCommand.sh

- Starte den Entwicklungsserver 

        python3 manage.py runserver

- Außerdem solltest du den Port 8000 deines Containers nach außen öffnen
- Du solltest nun unter 127.0.0.1:8000 den Entwicklungsserver erreichen können        
---