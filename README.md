# WAB
Webove aplikace: Backend
## Hello world service
 - Used project manager: PDM (https://pdm.fming.dev/latest/)
    - Command to install PDM: (Invoke-WebRequest -Uri https://pdm.fming.dev/install-pdm.py -UseBasicParsing).Content | python -
    - Commands
    - pdm
    - pdm init
    - pdm install fastapi
    - pdm add "uvicorn[standard]"
    - pdm install
    - download python
    - uvicorn main:app --reload
    - pdm add -d pytest

 - Rest Framework: FastAPI
Docker Container
  - Docker Image
    - copy.soubor
    - run soubor
    - install pdm
    - install configy
    - run pdm install
    - src
    - uvicorn
