#Your entry us always be below 25
#If above
#prints you're wrong
#If below
#You qualify

#Receive entry
#check entry
#print status

stand_age = "twentyfive"
entry_age = ""
entry_count = 0
entry_limit = 4
out_count = False

while entry_age != "twentyfive" and not (out_count) :
    if entry_count <= 4:
       entry_age = raw_input("Enter your age: ")
       entry_count += 1
    else:
        out_count = True


if out_count:
    print ("out of turn")
else:
    print ("No way")