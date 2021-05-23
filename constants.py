import bpy

resolutions = [
    { "name": "720p", "width": 1280.0, "height": 720.0 },
    { "name": "1080p", "width": 1920.0, "height": 1080.0 },
    { "name": "WQHD", "width": 2560.0, "height": 1440.0 },
    { "name": "UHD", "width": 3840.0, "height": 2160.0 },
    { "name": "256²", "width": 256.0, "height": 256.0 },
    { "name": "1024²", "width": 1024.0, "height": 1024.0 }
]

scales = [ ["¼", 1/4], ["½", 1/2], ["1", 1], ["2", 2], ["4", 4] ]

# ⁰¹²³⁴⁵⁶⁷⁸⁹
samples = [
    {"name": "4", "value": 16.0},
    {"name": "5", "value": 32.0},
    {"name": "6", "value": 64.0},
    {"name": "7", "value": 128.0},
    {"name": "8", "value": 256.0},
    {"name": "9", "value": 512.0},
    {"name": "10", "value": 1024.0},
    {"name": "11", "value": 2048.0},
    {"name": "12", "value": 4096.0},
    {"name": "13", "value": 8192.0},
    {"name": "14", "value": 16384.0},
    {"name": "15", "value": 32768.0},
    {"name": "16", "value": 65536.0},
    {"name": "24", "value": 16777216.0}
]
