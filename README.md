## Docker compose
```sh
docker compose up -d
```

## show docker container ip iaddress
```sh
docker inspect debian | grep IPAddress
```

## show ip address
```sh
hostname -I
```

## Create ansible controller ssh key
> ssh key path and filename: /root/.ssh/ansible
```sh
ssh-keygen -t ed25519 -C "Ansible Key"
```

### copy ssh public key to nodes
```sh
ssh-copy-id ansible@172.25.0.2
ssh-copy-id ansible@172.25.0.3
```

### disable & enable password login
```sh
sudo usermod -L ansible # disable password
sudo usermod -U ansible # enable password
```

### ssh test
```sh
ssh ansible@172.25.0.2
ssh ansible@172.25.0.3
```

## Create invontery list in working directory
```sh
nano /root/my_workdir/hosts
```
```sh
[group1]
debian ansible_host=172.25.0.2

[group2]
centos ansible_host=172.25.0.3

[group3]
ec2 ansible_host=18.193.75.239
```

## ping all invontery
```sh
ansible all -m ping
ansible all --key-file /root/.ssh/ansible -i invontery -m ping
```

## Ansible ad hoc commands
```sh
ansible [host-pattern] -m [module] -a “[module options]”
ansible-inventory --list
ansible --list-hosts all
ansible all -i hosts --limit host2 -a "/bin/echo hello"
ansible all -i hosts -m ansible.builtin.copy -a "src=./hosts dest=/tmp/hosts"

ansible [host|group|all] -m ping
ansible all -m command -a "/bin/echo hello world"
ansible all -a "/sbin/reboot" --become --ask-become-pass //reboot all nodes
ansible all -m apt -a name=hwinfo --become -K //install package
ansible all -m apt -a name="tmux state=latest" --become -K //upgare selected package
ansible all -m apt -a upgrade=dist --become -K //upgrade all nodes
ansible all -m gather_facts  // show node facts
ansible all -m gather_facts --tree /tmp/facts  // export node facts
ansible all -m gather_facts | grep ansible_distribution  // get node dist
ansible all -m setup -a 'filter=ansible_os_family'
ansible all -a "/sbin/reboot" -f 10 -u <username>
ansible all -m copy -a "src=/home/test.txt dest=/tmp/test.txt"
ansible all -m file -a "dest=/path/user1/new mode=777 owner=user1 group=user1 state=directory"
ansible all -m file -a "dest=/path/user1/new state=absent"
ansible all -m yum -a "name=httpd state=present"
```

## setting default config file
```sh
nano /root/my_workdir/ansible.cfg
```
```sh
[defaults]
inventory = hosts
private_key_file = ~/.ssh/ansible
remote_user = ansible
host_key_checking = False
```


## playbook commands
```sh
ansible-playbook --ask-become-pass <filename>.yml
ansible-playbook -i inventory.cfg <filename>.yml -b  // [b] become root on the remote nodes
ansible-playbook -i inventory.cfg  --limit <ip address> <filename>.yml
ansible-playbook --list-tags apache-install/playbook.yml // list tags
ansible-playbook --tags web_servers --ask-become-pass apache-install/playbook.yml  // run selected tag
```


## Install Ansible using apt
```sh
sudo apt-get update 
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
ansible –version
```

### Install Ansible using pip
```sh
python3 -m pip -V
python3 -m pip install --user ansible
ansible --version
```

### install nodes
```sh
sudo apt update
sudo apt install python3
sudo apt install openssh-server -y
sudo /etc/init.d/ssh start
sudo adduser --shell /bin/bash --gecos "" ansible
sudo echo "ansible ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
```