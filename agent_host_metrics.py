#!/usr/bin/env python3
import time,requests,subprocess,json,os
API="http://127.0.0.1:8080"  # später: externe Domain + Token
HOST=os.uname().nodename
def nstat():
    out = subprocess.check_output("nstat -az", shell=True, text=True, stderr=subprocess.DEVNULL)
    vals={}
    for line in out.splitlines():
        parts=line.split()
        if len(parts)>=2 and parts[0].startswith("Udp"):
            vals[parts[0]] = int(parts[1])
    return vals
def ethtool_errors(iface):
    try:
        out=subprocess.check_output(f"ethtool -S {iface}",shell=True,text=True,stderr=subprocess.DEVNULL)
        res={}
        for ln in out.splitlines():
            ln=ln.strip()
            if any(k in ln for k in ["rx_missed_errors","rx_errors","rx_dropped"]):
                k,v=[x.strip() for x in ln.split(":")]
                res[k]=int(v)
        return res
    except: return {}
def main():
    while True:
        payload={
          "host":HOST,
          "ts":int(time.time()),
          "nstat":nstat(),
          "if_enp1s0f0":ethtool_errors("enp1s0f0"),
          "if_enp1s0f1":ethtool_errors("enp1s0f1"),
        }
        try:
            requests.post(API+"/api/ingest/host",json=payload,timeout=3)
        except Exception as e:
            pass
        time.sleep(60)
if __name__=="__main__":
    main()
