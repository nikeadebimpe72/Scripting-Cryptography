#!/usr/bin/env python3

#given the up how many subnetworks can be made??

import math

ip="10.1.2.0"
mask="255.0.0.0"
sub_net_wanted=int("8")


#copy the static IP portion 
    #10. x.z.y 
    #255.0.0.0

front=""
counter=0
for x in mask.split("."):
    if x == "255":
        front+=ip.split(".")[counter]+"."
        counter+=1
    else:
        break


        #middle
#what are the racurr_networknges?
#  2^x-1 < subnets_wanted 2^x
        #find what x is
bits_borrow=0
network_range=0
for x in range(0,7):
    if sub_net_wanted <= math.pow(2,x):# 5< 2^3
        bits_borrow=x
        network_range=int(256/math.pow(2,x)) #255/8 =63 
        break


type=""
msg=""
count=1
for curr_network in range(0,256,network_range):

    bottom_range=front+str(curr_network)
    top_range=front+str(curr_network+network_range-1)

    net_id=""
    first_host=""
    last_host=""
    bcast=""
    
    figs=len(top_range.split(".")) 
    match figs :
        case 4:
            net_id=bottom_range #first host

            x=bottom_range.split(".")
            x[3]=str(curr_network+1) #first host
            first_host=".".join(x)
            x=top_range.split(".")
            last_host=x[0]+"."+x[1]+"."+x[2]+"."+str(int(x[3])-1) #last host
            bcast=top_range
            type="a"
        case 2:
            net_id=bottom_range+".0.0" #first host
            first_host=bottom_range+".0.1" #first host
            last_host=top_range+".255.254" #last host
            bcast=top_range+".255.255"
            type="b"
        case 3:
            net_id=bottom_range+".0" #first host
            first_host=bottom_range+".1" #first host
            last_host=top_range+".254" #last host
            bcast=top_range+".255"
            type="c"

    msg+=f"Network Number {count}\n"
    msg+=f"\tnetwork ID: {net_id}\n"
    msg+=f"\tFirst Host: {first_host}\n"
    msg+=f"\tLast Host: {last_host}\n"
    msg+=f"\tBroad Cast: {bcast}\n"

    count+=1

print(f"This is a type {type.upper()} network with ip of {ip} mask of {mask} and desierd hosts of {sub_net_wanted}")
print(f"\tRanges are  incremented by {network_range}")
print(msg)