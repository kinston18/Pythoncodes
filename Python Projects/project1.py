#Adventure Game

print("Welcome to Adventure Park")
name = input("Enter Name: ")
print("Hello", name )
age = int(input("Enter Age: "))


if age >= 12:
    print("You are welcome to the game!!!")

    play = input("Do you want to play(yes/no)? ").lower()
    if play == "yes":
        print("Let's begin")
        health = 15
        print("You are starting with", health, "health")

        choices = input("First choice.....Left or Right(left/right)?")
        if choices == "left":
           ans = input("Nice, you follow the path and reach a lake.....Do you want to swim across or go around(across/around)? ")


           if ans == "around":
              print("You went aroud and reached the other side of the lake.")
           elif ans == "across":
               print("You managed to get across the lake, but were bit by a fish and lost 5 health.")
               health -= 5
               print("Now you have", health, "health remaining")

           ans = input("You notice a house and a river. Which do you go to(river/house)? ")
           if ans == "house":
               print("You go the house and are greated by the owner......He doesn't like you and you loose 5 health")
               health -= 5
               print("Now you have", health, "health remaining")

               if health <= 0 :
                   print("oooppsss!!!!! You now have zero health, so you loose....")
               else:
                   print("You have survived....You win!!!")

           else:
               print("You fell in the river and lost....")
        else:
            print("You fell down and lost....")
    else:
        print("No worries!! Catch you later...")
else:
    print("Sorry!! You aren't old enough to play")

