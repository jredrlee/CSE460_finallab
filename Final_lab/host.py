import json, rpc, serial, struct, sys



# color detection remote call for pink ballon
def exe_duck_detection(interface):
    result = interface.call("duck_detection")
    if result is not None and len(result):
        res = struct.unpack("<HHHH", result)
        print("Largest Color Detected: {} {} {} {}".format(res[0], res[1], res[2], res[3]))

if __name__ == "__main__":
    interface = rpc.rpc_network_master(slave_ip="192.168.0.7", my_ip="", port=0x1DBA)
    while(True):
        sys.stdout.flush()
        exe_duck_detection(interface)