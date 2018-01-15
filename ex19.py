def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a nice lil shindig")
    print("Get a blanket.\n")

print("We can just give the function numbers directly")

cheese_and_cracks = int(input("How many cheeses you got??"))
boxes_of_cracks = int(input("How many boxes of crackers you got??"))

cheese_and_crackers(cheese_and_cracks, boxes_of_cracks)

print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)

print("And we can combine both too dawg")
cheese_and_crackers(cheese_and_cracks+100, boxes_of_cracks*5)
