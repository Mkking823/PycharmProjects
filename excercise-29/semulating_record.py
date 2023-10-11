import random


num_records = 1000

example_records = [
    "[NEW] tcp       6 120 SYN_SENT src=10.1.2.3 dst={ip1} sport=47800 dport=21 [UNREPLIED] src=203.0.113.47 dst={ip2} sport=21 dport=47800 helper=ftp",
            
    "[UPDATE] tcp      6 60 SYN_RECV src=10.1.2.3 dst={ip1} sport=47800 dport=21 src=203.0.113.47 dst={ip2} sport=21 dport=47800 helper=ftp",
            
    "[UPDATE] tcp      6 432000 ESTABLISHED src=10.1.2.3 dst={ip1} sport=47800 dport=21 src=203.0.113.47 dst={ip2} sport=21 dport=47800 [ASSURED] helper=ftp"
]
simulated_records=[]

for _ in range(num_records):
    dst_ip1= "203.0.113." + str(random.randint(1, 5))
    print(dst_ip1)
    dst_ip2= "203.0.113." + str(random.randint(1, 5))
    print(dst_ip2)

    for record in example_records:
        record=record.format(ip1=dst_ip1,ip2=dst_ip2)
        simulated_records.append(record)
output_file ="rupa.txt"
with open(output_file, "w")as file:
    for record in simulated_records:
        file.write(record + "\n")
print(f"{num_records}sets of example records have been generated{output_file}.")
