muffins = 2
cupcakes = 2

buying = input("do you want a muffin or a cupcake? Enter 0 to exit")

while buying != "0":
    if buying == "muffin" and muffins > 0 :
        muffins = muffins - 1
    if buying == "cupcake" and cupcakes > 0 :
        cupcakes = cupcakes - 1
    if muffins == 0:
        print("muffins out of stock")
    if cupcakes == 0:
        print("cupcakes out of stock")
    buying = input("do you want a muffin or a cupcake? Enter 0 to exit")


print("we have muffins left:", muffins, "we have cupcakes left:", cupcakes)

     
