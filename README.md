#  Советую ставить эти dotfiles только на ноутбук с процессором и видеокартой от AMD и с CachyOS.

sudo pacman -S base-devel lvm2 dhcpcd net-tools iproute2 vim xorg bspwm sxhkd xorg-xinit git python3

sudo pacman -R linux-cachyos-lts linux-cachyos-lts-headers

HOOKS=(base systemd autodetect microcode kms modconf block keyboard sd-vconsole plymouth filesystems fsck udev keymap lvm2)

sudo mkinitcpio -p linux-cachyos

sudo rm /etc/grub.d/31_efi_bootnext

sudo nano /etc/default/grub

GRUB_DISABLE_SUBMENU="true"

sudo grub-mkconfig -o /boot/grub/grub.cfg

sudo nano /etc/X11/xinit/xinitrc    exec bspwm

git clone https://github.com/aArtVI1/bspwm-dotfiles-laptop

cd ~/bspwm-dotfiles-laptop

python3 Builder/install.py

sudo systemctl enable lightdm

sudo systemctl enable dhcpcd

sudo systemctl enable power-profiles-daemon

reboot
