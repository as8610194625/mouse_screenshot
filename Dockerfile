FROM python:3
WORKDIR /mouse_print
COPY . /mouse_print
RUN pip install pyautogui pyinstaller