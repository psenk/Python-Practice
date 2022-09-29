fb_test_input = [1,2,3,4,5,6,7,8,9,10]

fb_dict = {3: "fizz", 5: "buzz", 7: "bang"}

divisible_list = [3, 5, 7]

output_list = ""

for i in fb_test_input:
    temp = ""
    for key in divisible_list:
        if i % key == 0:
            temp = fb_dict[key]
    if not temp:
        temp = i
    output_list += str(temp) + " "

print(output_list)