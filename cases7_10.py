places={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name? ")
    response=input("If you could visit one place in the world,where\
 would you go? ")
    places[name]=response
    print('Thank you!')
    repeat=input("Would you like to let another person respond? (yes/n\
o)--please use lower case letters  ")
    if repeat=='no':
        polling_active=False
print("\n---Survey Results---")
for name, response in places.items():
    print(name.title() + " would like to go to " + response.title()+".")
