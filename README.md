## Docker compose
```sh
docker compose up -d
```

## Conneccting ansible shel (ansible controller)
```sh
docker exec -it ansible /bin/bash
```

## show docker container ip iaddress
```sh
docker inspect remote-one | grep IPAddress
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

## Copy public key to worker nodes
```sh
ssh-copy-id -i /root/.ssh/ansible.pub remote-one
```

## Create working directory in ansible controller
```sh
mkdir /root/my_workdir
```

## Create invontery list in working directory
```sh
nano /root/my_workdir/invontery
```
```sh
[group1]
host1 ansible_host=remote-one ansible_user=root ansible_password=password
host2 ansible_host=remote-two ansible_user=root ansible_password=password
```

## ping all invontery
```sh
ansible all --key-file /root/.ssh/ansible -i invontery -m ping
```
## Ansible ad hoc commands
```sh
ansible [host-pattern] -m [module] -a “[module options]”
ansible-inventory --list
ansible --list-hosts all
ansible all -i hosts --limit host2 -a "/bin/echo hello"
ansible all -i hosts -m ansible.builtin.copy -a "src=./hosts dest=/tmp/hosts"
```

## setting default config file
```sh
nano /root/my_workdir/ansible.cfg
```
```sh
[defaults]
inventory = inventory
private_key_file = /root/.ssh/ansible
```

```sh
ansible all -m ping
```

## ansible interactive commands
```sh
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

## playbook commands
```sh
ansible-playbook --ask-become-pass <filename>.yml
ansible-playbook -i inventory.cfg <filename>.yml -b  // [b] become root on the remote nodes
ansible-playbook -i inventory.cfg  --limit <ip address> <filename>.yml
ansible-playbook --list-tags apache-install/playbook.yml // list tags
ansible-playbook --tags web_servers --ask-become-pass apache-install/playbook.yml  // run selected tag
```
## Install Ansible on Debian/Ubuntu systems
```sh
python3 -m pip -V
python3 -m pip install --user ansible
ansible --version
python3 -m pip show ansible
```
## Install Ansible using pip
```sh
sudo apt-get update 
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
ansible –version
```