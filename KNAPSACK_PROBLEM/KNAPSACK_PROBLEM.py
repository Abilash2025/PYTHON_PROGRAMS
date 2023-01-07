def knapsack_problem(no_of_obj, weight_of_objects, profit_of_objects, knapsack_capacity):
    
    profit_to_weight = [] * no_of_obj

    for i in range(0, no_of_obj):
        profit_to_weight.append(profit_of_objects[i] / weight_of_objects[i])

    maximum_profit_to_weight = 0
    
    flag = 1
    
    X = [0] * no_of_obj
    
    storage_used = 0

    while flag != 0:

        for i in range(0, no_of_obj):
            if profit_to_weight[i] >= profit_to_weight[maximum_profit_to_weight]:
                maximum_profit_to_weight = i

        profit_to_weight[maximum_profit_to_weight] = 0

        if weight_of_objects[maximum_profit_to_weight] + storage_used <= knapsack_capacity:
            X[maximum_profit_to_weight] = "1"
            storage_used = storage_used + weight_of_objects[maximum_profit_to_weight]

        else:
            X[maximum_profit_to_weight] = (knapsack_capacity - storage_used) / weight_of_objects[
                maximum_profit_to_weight]
            flag = 0

    print("\n")
    print("X : ", end=" ")

    for i in range(0, no_of_obj):
        print(f"{X[i]} ", end=" ")

    total_profit = 0
    for i in range(0, no_of_obj):
        total_profit += (float(X[i]) * profit_of_objects[i])

    print("\n")
    print(f"Total profit : {total_profit}")


weight_of_knapsack = int(input("Weight of knapsack : "))

no_of_objects = int(input("Number of objects : "))

weights_of_objects = []*no_of_objects

profits_of_objects = []*no_of_objects

for i in range(no_of_objects):
    weights_of_objects.append(float(input(f"Weight of object " + str(i + 1) + " : ")))
    profits_of_objects.append(float(input(f"profit of object " + str(i + 1) + " : ")))

knapsack_problem(no_of_objects, weights_of_objects, profits_of_objects, weight_of_knapsack)
