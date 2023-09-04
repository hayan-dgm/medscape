import shlex
import subprocess
configs = ["gr-ath.prod.surfshark.comsurfshark_openvpn_tcp.ovpn","ge-tbs.prod.surfshark.comsurfshark_openvpn_tcp.ovpn","fr-bod.prod.surfshark.comsurfshark_openvpn_tcp.ovpn","dk-cph.prod.surfshark.comsurfshark_openvpn_tcp.ovpn","cy-nic.prod.surfshark.comsurfshark_openvpn_tcp.ovpn"]
# write the command to a variable
cmd = 'start /b cmd /c \"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe\" --connect '+configs[0]

# split the command to parameters (It's not a necessity, it's just a rule of good taste)
args = shlex.split(cmd)

# run and remember the process as 'x'
x = subprocess.Popen(args, shell=True)
z="tom"
# change the connection based on an if statement
if z == "potato":
    # change the connection
    cmd = 'start /b cmd /c \"C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe\" --connect '+configs[1]
    args = shlex.split(cmd)
    x = subprocess.Popen(args, shell=True)
else:
    # keep the current connection
    pass