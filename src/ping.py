from re import findall
from subprocess import PIPE, Popen


def ping(nodes, times_to_ping):
    for ip in nodes:
        data = "Results: \n"
        output = Popen(f"ping {ip} -n {times_to_ping}" , stdout=PIPE, encoding="utf-8")
        for line in output.stdout:
            print(data + "\n")
            data += line
            ping_test = findall("TTL", data)

        if ping_test:
            print(f"{ip}: Sucessfully pinged!")
        else:
            print(f"{ip}: Failed to Pinged")

    return data



    
