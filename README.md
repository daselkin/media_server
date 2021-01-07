# Media Box Server

I bought a goddamn Bose Soundbar, expecing high-quality audio speakers to play my FLAC files.
It was only after installing it that I found out that the excellent hardware is backed by shoddy IOT software, that won't allow me to play my own media from my own computer or phone using my own media player.

I solve this by having an old Ubuntu machine connected to the Soundbar via DLNA.
This project covers the server side, allowing clients on local network to adjust volume and play tracks. 

## Dependencies
To run properly, the server machine needs pactl (PulseAudio) and Audacious.