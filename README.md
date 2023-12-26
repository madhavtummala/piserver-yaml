#  <img src="https://github.com/madhavtummala/piserver/assets/29799995/277c0e0d-3a7c-4f7d-a71f-3f532e77fa54" alt="Raspberry Pi Logo" width="20px"> PiServer <img src="https://github.com/madhavtummala/piserver/assets/29799995/277c0e0d-3a7c-4f7d-a71f-3f532e77fa54" alt="Raspberry Pi Logo" width="20px">

<img src="https://upload.wikimedia.org/wikipedia/en/thumb/1/15/Pi-hole_vector_logo.svg/1200px-Pi-hole_vector_logo.svg.png" width="60px" alt="Pi-hole"> <img src="https://raw.githubusercontent.com/dperson/openvpn-client/master/logo.png" width="80px" alt="OpenVPN Client"> <img src="https://static-00.iconduck.com/assets.00/sonarr-icon-1024x1024-wkay604k.png" width="80px" alt="Sonarr"> <img src="https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/radarr.png" width="80px" alt="Radarr"> <img src="https://avatars2.githubusercontent.com/u/6733935?v=3&s=200" width="80px" alt="Deluge"> <img src="https://i.redd.it/uybguvnj1p821.png" width="80px" alt="Jellyfin"> <img src="https://e1.pngegg.com/pngimages/261/453/png-clipart-macos-app-icons-plex-media-server.png" width="80px" alt="Plex"> <img src="https://github.com/immich-app/immich/raw/main/design/immich-logo.svg" width="80px" alt="Immich">

---

| Container Name           | Image                                             | Description                                      |
|--------------------------|---------------------------------------------------|--------------------------------------------------|
| **Essentials** |
| [pihole/pihole](https://github.com/pi-hole/pi-hole)                   | pihole/pihole                                     | Local DNS server that can block ad traffic        |
| [LinuxServer/endlessh](https://github.com/linuxserver/docker-endlessh)                 | lscr.io/linuxserver/endlessh                      | Honeypot for hackers on port 2222                 |
| **Media Server** |
| [dperson/openvpn-client](https://github.com/dperson/openvpn-client)                      | dperson/openvpn-client                            | Provides network connection for Jackett           |
| [LinuxServer/docker-jackett](https://github.com/linuxserver/docker-jackett)               | linuxserver/jackett                                | Connects to torrent websites to search for torrents|
| [LinuxServer/docker-sonarr](https://github.com/linuxserver/docker-sonarr)                 | linuxserver/sonarr                                 | Organizes TV show downloads using Jackett         |
| [LinuxServer/docker-radarr](https://github.com/linuxserver/docker-radarr)                 | linuxserver/radarr                                 | Organizes movie downloads using Jackett           |
| [LinuxServer/docker-deluge](https://github.com/linuxserver/docker-deluge)                 | linuxserver/deluge                                 | Torrent client used by Radarr and Sonarr          |
| [toddrob/searcharr](https://github.com/toddrob99/searcharr)                              | toddrob/searcharr                                  | User-facing bot for movie/series requests         |
| [madhavtummala/linker](https://github.com/madhavtummala/docker-linker)                 | madhavtummala/linker                               | Creates soft links for Plex and Transmission      |
| [filebrowser/filebrowser](https://github.com/filebrowser/filebrowser)                | filebrowser/filebrowser                            | SCP alternative and browsing UI                   |
| [LinuxServer/docker-jellyfin](https://github.com/linuxserver/docker-jellyfin)             | lscr.io/linuxserver/jellyfin                      | Open-source alternative to Plex                   |
| **Immich Service** |
| [immich-app/immich-server](https://github.com/immich-app/immich)                | ghcr.io/immich-app/immich-server                  | Main server for Immich application                |
| [immich-app/immich-microservices](https://github.com/immich-app/immich)                | ghcr.io/immich-app/immich-server                  | Microservices for Immich application             |
| [immich-app/immich-machine-learning](https://github.com/immich-app/immich-machine-learning) | ghcr.io/immich-app/immich-machine-learning        | Machine learning component for Immich             |
| [Redis](https://redis.io/)                                                       | redis:6.2-alpine                                   | Redis service for caching                         |
| [tensorchord/pgvecto-rs](https://github.com/tensorchord/pgvecto-rs)                  | tensorchord/pgvecto-rs:pg14-v0.1.11                | PostgreSQL database for Immich                    |
| **Passive Income** |
| [chashtag/picash](https://github.com/chashtag/picash)                               | chashtag/picash                                   | Manages earnapp, honeygain, and traffic monetizer |
| [packetstream/psclient](https://github.com/packetstream/psclient)                    | packetstream/psclient:latest                      | Packet Stream client for network sharing          |
| [iproyal/pawns-cli](https://github.com/iproyal/pawns-cli)                           | iproyal/pawns-cli:latest                          | Pawns app (formerly iproyals) CLI                |
| [mrcolorrain/bitping](https://github.com/mrcolorrain/bitping)                        | mrcolorrain/bitping                               | Bitping with unofficial bitpingd instead of bitping-node |
| **Extra / Misscellaneous** |
| [LinuxServer/docker-transmission](https://github.com/linuxserver/docker-transmission) | linuxserver/transmission                           | Handles seeding completed downloads from Deluge   |
| [LinuxServer/docker-plex](https://github.com/linuxserver/docker-plex)                 | lscr.io/linuxserver/plex                           | Plex server for organizing and providing a UI     |
| [taxel/plextraktsync](https://github.com/taxel/plextraktsync)                        | ghcr.io/taxel/plextraktsync                       | Syncs watched content between Plex and Trakt     |
| [taxel/plextraktsync](https://github.com/taxel/plextraktsync)                        | ghcr.io/taxel/plextraktsync                       | Scrobbles watched content from Plex to Trakt     |
| [ghcr.io/madhavtummala/tiendadoc](https://github.com/madhavtummala/tiendadoc)                | ghcr.io/madhavtummala/tiendadoc                   | Telegram bot for tagging and searching documents  |
| [containrrr/watchtower](https://github.com/containrrr/watchtower)                      | containrrr/watchtower                             | Automatically updates Docker containers          |
| [rclone/rclone](https://github.com/rclone/rclone)                                  | rclone/rclone                                     | Syncs encrypted Arrakis to Landsraad (IITBBS)     |
| [dperson/samba](https://github.com/dperson/samba)                                  | dperson/samba                                     | Samba client for offline cache browsing           |
| [p3terx/aria2-pro](https://github.com/P3TERX/Aria2-Pro-Docker)                       | p3terx/aria2-pro                                  | Aria2 with web interface for managing downloads  |
| [p3terx/ariang](https://github.com/P3TERX/Aria2-Pro-Docker)                           | p3terx/ariang                                     | Aria2 backend                   |


## Setup

### Install Ubuntu Server 20.04 (arm64) - [Instructions](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#1-overview)

### Install Docker - [Instructions](https://docs.docker.com/engine/install/)

### Install Docker-Compose (latest version) - [Instructions](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)

### Setup remote access

If its just you going to use this entire system, using [Tailscale](https://tailscale.com) seems easiest. After installing the clients on all your devices, you will have a static ip assigned to your raspi and can access it from any device.  

#### If you have a public server (oracle cloud was life time free)
If you want the system to be available for more than one user, but don't want to deal with the google authentication - you can use zerotier or the open source branch of tailscale - [Headscale](https://github.com/juanfont/headscale). 

Instead if you don't want to bother with installing clients on each user, you can setup tailscale for connecting the public server and your raspi. And then setup nginx reverse proxy on the public server for a more seamless forwarding of requests for anyone.

###  Setup MergerFS / Mounts - etc/fstab
apt-get install ntfs-3g, try nfs3 (in-kernel) if you can
```
sudo blkid (get UUID)
```
fstab entries
```
UUID=XXXXXXXXXXXXX /mnt/passport ntfs-3g async,nobootwait,big_writes,noatime,nodiratime,nofail,umask=007,uid=1000,gid=1003 0 0

UUID=YYYYYYYYYYYYY /mnt/seagate ntfs-3g async,nobootwait,big_writes,noatime,nodiratime,nofail,umask=007,uid=1000,gid=1003 0 0

/mnt/passport:/mnt/seagate /mnt/data fuse.mergerfs direct_io,defaults,allow_other,minfreespace=50G,fsname=mergerfs,cache.files=partial,dropcacheonclose=true,category.create=mfs 0 0
```
If you have a bigger array of disks, use `snapRAID` as well

### Start the containers
Fill the values for .env
```
mv example.env .env
docker-compose up -d
docker-compose -f passive-income.yaml up -d
```

### Overclock to upto 2.147GHz
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

## Common Tips

### Powered USB with Raspi
Buy only from list [here](https://elinux.org/RPi_Powered_USB_Hubs). If not, cut the red wire (5v) of the usb hub wire that connects to raspi port to prevent backflow.

### rclone mounts (from gdrive) with a cache on hdds
```
[Unit]
Description=Landsraad Movies
After=network-online.target mnt-seagate.mount
Requires=network-online.target mnt-seagate.mount

[Service]
Type=notify
ExecStart= \
/usr/bin/rclone mount \
    --config=/home/ubuntu/dune/config/rclone/rclone.conf \
    --dir-cache-time 30m \
    --vfs-cache-mode full \
    --cache-dir /mnt/seagate/cache1 \
    --vfs-cache-max-size 1000G \
    --vfs-write-back 30m \
    --vfs-cache-max-age 720h \
    --log-level INFO \
    --log-file /home/ubuntu/dune/config/rclone/movies.log \
    --allow-other \
    --allow-non-empty \
    --vfs-read-ahead 256M \
    --uid 1000 \
    --gid 1000 \
    arrakis:MOVIES /mnt/seagate/MOVIES
ExecStop=/bin/fusermount -u /mnt/seagate/MOVIES
Restart=on-failure
RestartSec=15

[Install]
WantedBy=default.target
```

### static ip (you won't need if you use tailscale)
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

### stop default dns for pihole (if needed)
```bash
sudo systemctl disable systemd-resolved.service
sudo systemctl stop systemd-resolved
```

### if you installed docker through snap (please don't)
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
