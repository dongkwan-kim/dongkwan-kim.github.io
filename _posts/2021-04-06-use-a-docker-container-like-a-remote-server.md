---
title: 'Use a Docker Container like a Remote Server'
date: 2021-04-06
permalink: /blogs/use-a-docker-container-like-a-remote-server/
tags:
  - Machine Learning Engineering
summary: ""
---

This post describes how to use a Docker container like a single isolated remote server.
Some of the content focuses on using NVIDIA GPUs, so you can omit the details if you are not interested in this.

## Preliminary

- In this article, your server will be a remote machine (or host machine) and your laptop will be a local machine.
- You have to install the Docker first on your remote machine. (Or ask the root to do this).
- You do not have to be a root of the host machine to follow this post.
- But you have to know what Docker is and how it works. See overview documentations: [[English]](https://docs.docker.com/get-started/overview/) [[Korean]](https://smjeon.dev/etc/docker-overview/).

## Instruction

Pull an image you want to use in your remote machine.
In this post, it is `nvidia/cuda:10.2-cudnn8-devel-ubuntu18.0`.

```bash
# In the remote machine,
docker pull nvidia/cuda:10.2-cudnn8-devel-ubuntu18.04
```

Create a container based on this image.
```bash
# In the remote machine,
docker run -ti \
  --runtime=nvidia \
  --name $container_name \
  -p $ssh_port:22 -p $tensorboard_or_jupyter_port:6006 \
  -v $mount_dir:$mount_dir \
  --ipc=host \
  -d nvidia/cuda:10.2-cudnn8-devel-ubuntu18.04 /bin/bash
```
- If you want to use GPUs in the container, you have to specify `--runtime=nvidia`.
- You have to forward 22 port (ssh) to your own port.
- If you want to use a Tensorboard or Jupyter, you have to forward additional ports for these.
- If you want to use file systems in the host machine, you have to bind mount a volume (`-v $mount_dir:$mount_dir`) using absolute paths.
- If you want to use multiple subprocesses (`num_workers` > 1) in `DataLoader`, it is recommend to put `--ipc=host`.
- If you want to use a specific set of GPUs, use `--gpus` argument. (e.g., `--gpus '"device=0,1,2,3"'`).

Now attach your container.
```bash
# In the remote machine,
docker attach $container_name
```

In the container, install whatever you need. Below is my preferred list, but do not forget to install the following packages: `openssh-server ssh`.
```bash
# In the container of the remote machine,
apt-get update
apt-get install vim git sudo curl screen software-properties-common
apt-get install openssh-server ssh  # important!

# To install python 3.7. If you do not want to use python3.7, you can skip it, or install other versions.
add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get install python3.7 python3-pip python3.7-dev
```

You might want to login the container with a password, then turn off `PubkeyAuthentication`. If you skip this step, you cannot log in to your container with your id and password.
```bash
# In the container of the remote machine,
sed 's/PubkeyAuthentication/#PubkeyAuthentication/g' /etc/ssh/sshd_config > ~/sshd_config.tmp
cat ~/sshd_config.tmp > /etc/ssh/sshd_config
rm ~/sshd_config.tmp
service ssh restart  # important!
```

Create a user account and make it a root.
```bash
# In the container of the remote machine,
adduser $user_name
usermod -aG sudo $user_name
su $user_name
```

Configure user-specific settings: git global configuration, shell, bashrc/zshrc, or vimrc.

Turn off the shell you are working on, and turn on a new shell in the local machine.
Then access the container you created with the below command.
```bash
# In the local machine,
ssh -p $ssh_port $user_name@$host
``` 

If you want to use a Tensorboard or Jupyter, please follow [my other post](/blogs/tensorboard-in-a-docker-container/).


## Troubleshooting

### I cannot log in my containers after restarting them

You have to run `service ssh restart` after restarting containers.

### I cannot log in with given ports

If you see this warning:
```text
WARNING: IPv4 forwarding is disabled. Networking will not work
```

Run `sudo vi /etc/sysctl.conf` and add `net.ipv4.ip_forward=1`.
```text
# sysctl settings are defined through files in
# /usr/lib/sysctl.d/, /run/sysctl.d/, and /etc/sysctl.d/.
#
# Vendors settings live in /usr/lib/sysctl.d/.
# To override a whole file, create a new file with the same in
# /etc/sysctl.d/ and put new settings there. To override
# only specific settings, add a file with a lexically later
# name in /etc/sysctl.d/ and put new settings there.
#
# For more information, see sysctl.conf(5) and sysctl.d(5).

net.ipv4.ip_forward=1  # Here!
```
Then, restart network.
```bash
sudo systemctl restart network
```
