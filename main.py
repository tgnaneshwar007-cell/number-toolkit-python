def get_numbers():
    n = int(input("How many numbers do you want to enter? "))

    nums = ()

    for i in range(n):
        value = int(input(f"Enter number {i + 1}: "))
        nums = nums + (value,)

    return nums


def show_menu():
    print("\n========== NUMBER TOOLKIT ==========")
    print("1. Show Original Tuple")
    print("2. Show Even Numbers")
    print("3. Show Odd Numbers")
    print("4. Calculate Sum")
    print("5. Find Pair for Target")
    print("6. Show Tuple Information")
    print("7. Exit")


def find_pair(nums, target):
    seen = {}

    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in seen:
            return seen[needed], i

        seen[nums[i]] = i

    return None


print("\nWelcome to Number Toolkit!")

nums = get_numbers()

while True:
    show_menu()

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Original Tuple:", nums)

    elif choice == 2:
        result = ()

        for i in nums:
            if i % 2 == 0:
                result = result + (i,)

        print("Even Tuple:", result)

    elif choice == 3:
        result = ()

        for i in nums:
            if i % 2 != 0:
                result = result + (i,)

        print("Odd Tuple:", result)

    elif choice == 4:
        total = 0

        for i in nums:
            total = total + i

        print("Sum:", total)

    elif choice == 5:
        target = int(input("Enter target: "))

        pair = find_pair(nums, target)

        if pair:
            i, j = pair

            print("Pair found!")
            print("Indices:", i, "and", j)
            print("Values:", nums[i], "+", nums[j], "=", target)

        else:
            print("No pair found for target", target)

    elif choice == 6:
        first, *middle = nums

        print("Tuple:", nums)
        print("Length:", len(nums))
        print("First value:", first)
        print("Remaining values:", middle)

        if nums:
            print("Maximum:", max(nums))
            print("Minimum:", min(nums))

    elif choice == 7:
        print("Thank you for using Number Toolkit!")
        break

    else:
        print("Invalid choice. Please select 1-7.")