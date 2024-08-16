from re import findall
from subprocess import PIPE, Popen


def ping(nodes, times_to_ping):
    good_pings = []
    bad_pings = []
    try:
        for ip in nodes:
            data = ""
            output = Popen(f"ping {ip} -n {times_to_ping}" , stdout=PIPE, encoding="utf-8")
        
            for line in output.stdout:
                data = data + line
            
                ping_test = findall("TTL", data)

            if ping_test:
                good_pings.append(ip)
            else:
                bad_pings.append(ip)
        
        print("Sucessful pings: \n")
        for x in good_pings:
            print(x)

        print('\n')

        print("Failed pings: \n")
        for x in bad_pings:
            print(x)

        print("done")
        return good_pings, bad_pings
    except Exception as e:
        return e





    
