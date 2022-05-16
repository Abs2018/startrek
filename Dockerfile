# Select a Python image
FROM python:3.11-rc-bullseye

# Update the packages.
RUN apt update
# Install applications
RUN apt install mariadb-server sudo -y

RUN mysql -sfu root <<EOS UPDATE mysql.user SET Password=PASSWORD('stgame') WHERE User='root'; DELETE FROM mysql.user WHERE User=''; DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1'); DROP DATABASE IF EXISTS test; DELETE FROM mysql.db  WHERE Db='test' OR Db='test\\_%'; FLUSH PRIVILEGES; EOS

# Install SSH Server
# RUN apt install openssh-server sudo -y
# RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 test
# RUN echo 'test:test' | chpasswd
# RUN service ssh start
# EXPOSE 22
# RUN sudo systemctl enable ssh

# Set the working directory in the container
WORKDIR /usr/src/startrek
# Cop the requirements.txt file and install all application requirements
COPY ./src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application into the container
# COPY . .
# Run the following command on bootup
# CMD [ "python", "./your-daemon-or-script.py" ]
CMD [ "/bin/bash" ]
#CMD ["/usr/sbin/sshd","-D"]