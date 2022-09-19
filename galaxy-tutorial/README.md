### create galaxy directories
```sh
mkdir -pv galaxy-tutorial/{playbooks,vars}
```

### install ansible master
```sh
sudo apt install ansible
python3 -m pip -V
python3 -m pip install --user ansible
ansible --version
ssh-keygen -t rsa
```

### prepare nodes
```sh
sudo apt update
sudo apt install python3
sudo apt install openssh-server -y
sudo /etc/init.d/ssh start
sudo adduser --shell /bin/bash --gecos "" ansible
sudo echo "ansible ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
```

### ssh test
```sh
ssh ansible@172.25.0.2
ssh ansible@172.25.0.3
```

### disable & enable password login
```sh
sudo usermod -L ansible # disable password
sudo usermod -U ansible # enable password
```

### copy ssh public key to nodes
```sh
ssh-copy-id ansible@172.25.0.2
ssh-copy-id ansible@172.25.0.3
```

### install ansible galaxy nginx role
```sh
ansible-galaxy install stouts.nginx
```