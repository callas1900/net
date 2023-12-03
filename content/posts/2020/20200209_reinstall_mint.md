+++
title = "linux mint re-setup after clean installation"
date = "2020-02-09"
author = ""
cover = ""
tags = ["linux mint"]
keywords = ["", ""]
description = "linux mint の調子がおかしくなったので、再インストールしたあとの現状復帰を大まかにまとめてみました。"
showFullContent = false
draft = false
+++

linux mint の調子がおかしくなったので、クリーンインストールし直しました。
ついでにその時の手順を今後のために書き留めておきます。

# 1. Install essentail applications

- brave browser
- dropbox

# 2. Change keyboard settings

## activate japanese input
1. open input method
1. install Japanese input method
1. select fcitx
1. logout then login

## change keymaps

open keyboard in the cinnamon menu.
- capslock to ctrl

open fcitx option in the cinnamon menu.
- left bottom ctrl to input method changer


# 3. Make symbolic links

I stored lots of configuration file in Dropbox.
After finising sync of Dropbox, I can make symbolic lincs from files in Dropbox.

```bash
$ cd #back to home directory for just in case.
$ ln -s ~/Dropbox/develop/.vimrc .
$ ln -s ~/Dropbox/develop/.vim .
$ ln -s ~/Dropbox/develop/.tmux.conf .
$ ln -s ~/Dropbox/env/linux/.bashrc .
$ ln -s ~/Dropbox/env/linux/.bash_aliases .
$ ln -s ~/Dropbox/env/.gitconfig .
```
# 4. Set-up ssh things

I'm using Dropbox to store ssh keys with encfs.  
encfs encrypts my directory which includes the keys, I can get the keys by using encfs.

## get keys

install encfs.
```bash
$ sudo apt install encfs
```

creat directories as mount points.
```bash
$ sudo mkdir -p /mnt/encfs/ssh_keys
$ sudo mkdir -p /mnt/encfs/pgp
$ sudo chmod 777 /mnt/encfs/ssh_keys
$ sudo chmod 777 /mnt/encfs/pgp
```

mount encrypted directory by my function in .bash_alias.

```bash
$ ecnfs_mount
```

copy keys if needed.

```bash
$ cp /mnt/encfs/ssh_keys/razer_blade/id_rsa* .
```

**! Don't forget to change key's permission to 600!**

## config

```bash
$ ln -s ~/Dropbox/env/ssh_config/razer_blade_ssh_config config
```
# 5. Install basic apps
```bash
$ sudo apt install git silversearch-ag thefuck
```
- [install linux brew](https://docs.brew.sh/Homebrew-on-Linux)

```bash
$ brew install z fzf
```
# 6. Install Fonts
## for terminal

- [Source Code Pro](https://github.com/adobe-fonts/source-code-pro/releases)

## for web browser

- noto sans jp(google font)

# 7. Make system faster

Now, essentail part is almost done.
Let's make it more confortable by reading below links.

1. https://easylinuxtipsproject.blogspot.com/p/first-mint-cinnamon.html
2. https://easylinuxtipsproject.blogspot.com/p/speed-mint.html


# 8. turn off bluetooth

I'm using bluetooth sometimes but almost time I don't use.
So turn off bluetooth at starting-up is good for me.
I used below way.

[How To Disable Bluetooth At Startup On Linux?](https://etechshout.com/disable-bluetooth-at-startup-on-linux/)

> 1. First of all, click on the Start Menu and type Startup Applications to search it
> 1. Now, click on Startup Applications
> 1. Click on the + icon at the bottom of the “Startup Applications” window
> 1. Now, Click on “Custom command.”
> 1. Add any name/description (whatever you want like disable bluetooth etc..)
> 1. Now, in the next step enter the command as rfkill block bluetooth
> 1. That’s it! Now, click on Add and you are done!

# install extra applications

## graphics 
- inkscape
- darktable
- gThumb
