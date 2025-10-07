#! /usr/bin/env python3

#What is the current networks what are the ranges? 
    #How many users are online?
    #What range has the most users?


import os 
import math

def getNetWorkInfo():

    os.system("ifconfig eth0 |grep -e 'inet .*' >ip.txt")
    ip_line=open("ip.txt").read()
    ip_split=ip_line.strip().split(" ")
    ip=ip_split[1]
    mask=ip_split[4]
    bcast=ip_split[7]
    os.system("rm ip.txt")
    
    return ip,mask, bcast

def subnets_andThier_population():
    #i have the ip and the mask tell me the possible ranges if there are x subnets. 
    subnets_wanted=int("3") #input("how many subnets wanted?") )

    #how mnay bits do i need to borrow?
    network_ranges=0
    for a in range(0,7):
        subnets=math.pow(2,a)
        if subnets >= subnets_wanted:
            network_ranges=int(256/subnets)
            break

    x=getNetWorkInfo()
    ip=x[0]
    mask=x[1]
    bcast=x[2]

    ip_prefix= ip.split(".")
    num_255=0
    msg=""
    for a in mask.split("."):
        if int(a) ==255:
            msg+=ip_prefix[num_255]+"."
            num_255+=1
    ip_prefix=msg


    sub_net_ppl=0 #3
    busiest_subnet="" # 3 *range -> 127-192 is the busiest
    for current_range in range(0,255,network_ranges):
        split_ip=ip_prefix.rstrip().split(".")

        net_type=""
        subnet_id=0
        first_host=0
        last_host=0
        subnet_broadcast=0
        ppl_on=0

        if (num_255 ==3): #10.0.0. range
            net_type="C"
            subnet_id=ip_prefix+str(current_range)
            first_host=ip_prefix+str(current_range+1)
            last_host=ip_prefix+str(current_range+network_ranges-1)
            subnet_broadcast=ip_prefix+str(current_range+network_ranges)

            for host in range(current_range+1, current_range+network_ranges-1):
                online=os.system(f"ping -c1 -w2 {str(ip_prefix)+str(host)} >/dev/null 2>&1")
                if online == 0: #successs
                    ppl_on+=1
                    print(f"online: {str(ip_prefix)+str(host)}")
                    continue
            
            #check if buiser and num_ppl
            if ppl_on>sub_net_ppl:
                sub_net_ppl=ppl_on 
                busiest_subnet=f"{subnet_id} -> {sub_net_ppl} ->{last_host}"

        elif num_255 ==2 : #10.0 .range .first_host
            net_type=="B"
            subnet_id=ip_prefix+f"{current_range}.0"
            first_host=ip_prefix+f"{current_range}.1"
            last_host=ip_prefix+f"{current_range+network_ranges-1}.254"
            subnet_broadcast=ip_prefix+f"{network_ranges+current_range}.255"

        elif num_255 ==1 :#10.range .first_host. 0 / .last host. 255
            net_type=="A"
            subnet_id=ip_prefix+f"{current_range}.0.0"
            first_host=ip_prefix+f"{current_range}.0.1"
            last_host=ip_prefix+f"{current_range}.0.254"
            subnet_broadcast=ip_prefix+f"{current_range+network_ranges}.255.255"

    


        print(f" {subnet_id} {subnet_broadcast} {ppl_on}")

    print(busiest_subnet)

subnets_andThier_population()

# print (f"{ip} {mask} {bcast}")