def print_list_numbers(start_value:int, n:int, step:int)-> None:
    stop_value = start_value +n*step
    for i in range(start_value, stop_value, step):
        print(i)
 
 
 
 
start_value = int(input("enter a start value:>"))
amount = int(input("enter a amount"))
step_size = int(input("enter a pos step size:>"))
 
print_list_numbers(start_value, amount, step_size)