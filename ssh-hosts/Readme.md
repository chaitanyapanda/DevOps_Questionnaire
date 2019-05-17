# ssh-hosts
Steps:
1. clone the repo
2. change to the cloned directory
3. Make sure ansible is installed on the source server. Installation can be done by running the  command
`sudo yum install -y ansible` for RHEL Systems (or) `sudo apt-get install ansible -y` for Debian systems.  
4. Add all the servers to the `hosts`. `hosts` should be in below format:
```
[ssh_servers]
pandachaitanya1c
pandachaitanya2c
pandachaitanya3c
```
5. Run the below command using the hosts file:  <br>
`ansible-playbook -i hosts --private-key ~/developer_key sshrun.yml`
I enabled the Password-less sudo for the `developer` user on my server to run the above command. If your `developer` user doesnt has the password-less sudo. Run the below command instead of above one. <br>
`ansible-playbook -i hosts --private-key ~/developer_key sshrun.yml -k` <br>
`-k -> Prompts for sudo password while executing the command`
