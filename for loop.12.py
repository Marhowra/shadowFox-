jumping_jacks = 0

for i in range(1, 11):
    jumping_jacks += 10
    print("You completed", jumping_jacks, "jumping jacks.")

    if jumping_jacks == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ")

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ")

        if skip == "yes" or skip == "y":
            print("You completed a total of", jumping_jacks, "jumping jacks.")
            break
        else:
            print("Keep going!")
            print("Remaining jumping jacks:", 100 - jumping_jacks)
    else:
        print("Remaining jumping jacks:", 100 - jumping_jacks)