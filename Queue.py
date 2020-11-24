names = [ "john, julia, mike, judy, miranda, amanda, grace, bella, kaitie, greg" ]
queue= []

print("\nInitial queue")
print(queue)

for x in names:
    queue.append('john')
    queue.append('julia') 
    queue.append('mike') 
    queue.append('judy') 
    queue.append('miranda') 
    queue.append('amanda') 
    queue.append('grace') 
    queue.append('bella')
    queue.append('kaitie') 
    queue.append('greg')
    print('\nQueue with added elements')
    print (queue)
   
for x in queue:
    print("\nElements dequeued from queue") 
    print(queue.pop(0)) 
for x in queue:
    print("\nElements dequeued from queue") 
    print(queue.pop(0))
for x in queue:
    print("\nElements dequeued from queue") 
    print(queue.pop(0))
for x in queue:
    print("\nElements dequeued from queue") 
    print(queue.pop(0))
for x in queue:
    print("\nElements dequeued from queue") 
    print(queue.pop(0))

print("\nQueue after removing elements") 
print(queue) 

