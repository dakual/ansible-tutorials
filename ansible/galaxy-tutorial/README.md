mkdir -pv galaxy-tutorial/{playbooks,vars}


docker run -d \
-v /var/run/docker.sock:/tmp/docker.sock \
-v /etc/hosts:/tmp/hosts \
--name docker-hoster \
dvdarias/docker-hoster


sudo apt install ansible
python3 -m pip -V
python3 -m pip install --user ansible
ansible --version

ssh-keygen -t rsa

ssh-copy-id ansible@172.25.0.2
ssh-copy-id ansible@172.25.0.3

$ sudo apt update
sudo apt install python3
$ sudo apt install openssh-server -y
/etc/init.d/ssh start
adduser --shell /bin/bash --gecos "" ansible
sudo visudo
ansible ALL=(ALL) NOPASSWD:ALL

ssh ansible@172.25.0.2
sudo usermod -L ansible # disable password
sudo usermod -U ansible # enable password



ansible-galaxy install stouts.nginx