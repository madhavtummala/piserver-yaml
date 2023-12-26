#  <img src="https://assets.stickpng.com/images/584830fecef1014c0b5e4aa2.png" alt="Raspberry Pi Logo" width="20px"> PiServer <img src="https://assets.stickpng.com/images/584830fecef1014c0b5e4aa2.png" alt="Raspberry Pi Logo" width="20px">

| Container Name           | Image                                             | Description                                      |
|--------------------------|---------------------------------------------------|--------------------------------------------------|
| **Essentials** |
| pihole                   | pihole/pihole                                     | Local DNS server that can block ad traffic        |
| endlessh                 | lscr.io/linuxserver/endlessh                      | Honeypot for hackers on port 2222                 |
| **Media Server** |
| vpn                      | dperson/openvpn-client                            | Provides network connection for Jackett           |
| jackett                  | linuxserver/jackett                                | Connects to torrent websites to search for torrents|
| sonarr                   | linuxserver/sonarr                                 | Organizes TV show downloads using Jackett         |
| radarr                   | linuxserver/radarr                                 | Organizes movie downloads using Jackett           |
| deluge                   | linuxserver/deluge                                 | Torrent client used by Radarr and Sonarr          |
| telegram_bot             | toddrob/searcharr                                  | User-facing bot for movie/series requests         |
| linker                   | madhavtummala/linker                               | Creates soft links for Plex and Transmission      |
| filebrowser              | filebrowser/filebrowser                            | SCP alternative and browsing UI                   |
| jellyfin                 | lscr.io/linuxserver/jellyfin                      | Open-source alternative to Plex                   |
| **Immich Service** |
| immich-server            | ghcr.io/immich-app/immich-server                  | Main server for Immich application                |
| immich-microservices     | ghcr.io/immich-app/immich-server                  | Microservices for Immich application             |
| immich-machine-learning  | ghcr.io/immich-app/immich-machine-learning        | Machine learning component for Immich             |
| redis                    | redis:6.2-alpine                                   | Redis service for caching                         |
| database                 | tensorchord/pgvecto-rs:pg14-v0.1.11                | PostgreSQL database for Immich                    |
| **Passive Income** |
| picash                   | chashtag/picash                                   | Manages earnapp, honeygain, and traffic monetizer |
| psclient                 | packetstream/psclient:latest                      | Packet Stream client for network sharing          |
| pawns-cli                | iproyal/pawns-cli:latest                          | Pawns app (formerly iproyals) CLI                |
| bitping                  | mrcolorrain/bitping                               | Bitping with unofficial bitpingd instead of bitping-node |
| **Extra** |
| transmission             | linuxserver/transmission                           | Handles seeding completed downloads from Deluge   |
| plex-server              | lscr.io/linuxserver/plex                           | Plex server for organizing and providing a UI     |
| trakt-sync               | ghcr.io/taxel/plextraktsync                       | Syncs watched content between Plex and Trakt     |
| trakt-scrobble           | ghcr.io/taxel/plextraktsync                       | Scrobbles watched content from Plex to Trakt     |
| tiendadoc                | ghcr.io/madhavtummala/tiendadoc                   | Telegram bot for tagging and searching documents  |
| watchtower               | containrrr/watchtower                             | Automatically updates Docker containers          |
| drive_sync               | rclone/rclone                                     | Syncs encrypted Arrakis to Landsraad (IITBBS)     |
| samba                    | dperson/samba                                     | Samba client for offline cache browsing           |
| aria2-pro                | p3terx/aria2-pro                                  | Aria2 with web interface for managing downloads  |
| ariang                   | p3terx/ariang                                     | Web-based frontend for Aria2                     |

## Setup

### Install Ubuntu Server 20.04 (arm64) - [Instructions](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#1-overview)



### static ip
/etc/netplan/01-netcfg.yaml
```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.0.88/24
      gateway4: 192.168.0.1
      nameservers:
          addresses: [8.8.8.8, 1.1.1.1]
```

### automount ntfs-3g
apt-get install ntfs-3g
```
sudo blkid (get UUID)
```
/etc/fstab
```
LABEL=writable  /        ext4   defaults        0 0
LABEL=system-boot       /boot/firmware  vfat    defaults        0       1
UUID=C4E216FCE216F302 /mnt/volume ntfs-3g async,big_writes,make-shared,noatime,nodiratime,nofail,uid=1000,gid=1000,umask=007 0 0
```

### overclock
```bash
sudo apt install neofetch gparted
snap install rpi-imager
```
/boot/firmware/config.txt
```
over_voltage=6
arm_freq=2147
gpu_freq=700
v3d_freq=750
```

### stop default dns for pihole (if needed)
```bash
sudo systemctl disable systemd-resolved.service
sudo systemctl stop systemd-resolved
```

### install docker through snap
```bash
sudo apt install snapd
sudo snap install docker
export PATH=/snap/bin:$PATH > ~/.bashrc
docker --version
docker.compose --version
```
To use without root permissions
```bash
sudo addgroup --system docker
sudo adduser $USER docker
newgrp docker
sudo snap disable docker
sudo snap enable docker
```

### docker commands
clear all logs
```bash
docker ps -q | xargs -d $'\n' sh -c 'for arg do : > $(docker inspect --format='{{.LogPath}}' "$arg"); done'
```
update all containers
```bash
docker-compose pull
docker-compose up --force-recreate --remove-orphans --build -d
docker system prune
```
stop all containers
```
docker ps -q | xargs docker stop
```

### nfs server
```
sudo vim /etc/exports
sudo exportfs -a
sudo systemctl restart nfs-kernel-server

/mnt/passport 100.85.246.28(ro,all_squash,anonuid=1000,anongid=1003,no_subtree_check) 100.120.117.42(ro,all_squash,anonuid=1000,anongid=1003,no_subtree_check) 100.108.217.55(rw,all_squash,anonuid=1000,anongid=1003,no_subtree_check)
/mnt/processing 100.120.117.42(rw,sync,no_subtree_check)
```

### nfs client

```
sudo vim /etc/fstab

100.86.73.62:/mnt/passport /mnt/arrakis  nfs      defaults    0       0
100.86.73.62:/mnt/processing /mnt/processing nfs defaults 0 0
```

On MAC: Go to server: `nfs://100.86.73.62`

### hevc encoding

```
HandBrakeCLI -i "$input_file" -o "$output_file" --preset-import-file "$custom_preset" --preset="HEVC"
```
