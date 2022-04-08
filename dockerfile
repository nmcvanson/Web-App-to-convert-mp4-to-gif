FROM ubuntu
RUN apt update
RUN apt install -y python3
RUN apt install -y ffmpeg
RUN apt install -y python3-pip
RUN apt install -y sqlite3
RUN pip3 install dataset
RUN pip3 install flask
WORKDIR /home/lab3
ENTRYPOINT sh -c "ls; pwd; python3 site.py"