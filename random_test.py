import random

def generate_random_4digit():
    return ''.join(random.choice('01') for _ in range(4))

def generate_string_with_pattern(num_patterns, num_randoms):
    pattern = '1001'
    res_list = []
    res_list_no_space = []
    for i in range(num_randoms):
        result = []
        res_no_space = []
        for i in range(1, num_patterns + 1):
            
            if i % 4 == 0:
                result.append(pattern)
                res_no_space.append(pattern)
                result.append('\t')
            else:
                result.append(generate_random_4digit())
                res_no_space.append(generate_random_4digit())
                result.append(' ')
        res_list.append("".join(result))
        res_list_no_space.append("".join(res_no_space))
    return res_list, res_list_no_space

# Generate the string with 20 4-digit patterns
generated_string, gen_str_no_space = generate_string_with_pattern(num_patterns=20, num_randoms=100)

output_path = '100_generated.txt'
with open(output_path, 'w+') as f:
    for s in generated_string:
        f.write(str(s)+"\n")
    
output_path = '100_generated_no_space.txt'
with open(output_path, 'w+') as f:
    for s in gen_str_no_space:
        f.write(str(s)+"\n")