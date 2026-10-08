def get_prime_factors(num):
    factors = []
    divisor = 2
    active_num = num
    for i in range(num, 1, -1):
        print("START---------------------------------------------------")
        print("i: ", i)
        print("num: ", num)
        print("divisor: ", divisor)
        if active_num % divisor == 0:
            print("active_num: ", active_num)
            
            factors += [divisor]
            active_num = active_num/divisor
            print(factors)
        else:
            
            divisor += 1
        print("END---------------------------------------------------")

    return factors

# commands used in solution video for reference
if __name__ == '__main__':
    # print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    # print(get_prime_factors(13))  # [13]
    print(get_prime_factors(60))  # [2, 2, 3, 5]
