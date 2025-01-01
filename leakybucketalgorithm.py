storage=0
noofqueries=4
bucketsize=10
inputpktsize=4
outputpktsize=1
for i in range(0,noofqueries):
    sizeleft=bucketsize-storage
    if inputpktsize<=sizeleft:
        storage+=inputpktsize
    else:
        print("Packet loss=", inputpktsize)
    print(f"Bucket size={storage}out of bucket size={bucketsize}")
    storage-=outputpktsize
