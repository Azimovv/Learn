def bottles_of_beer(beer):
    """
    recursion of old "bottles of beer on the wall" song
    :param beer: beers on the wall (int)
    """
    if beer < 1:
        print ("No more beer, you need to go to a hospital. You have alcohol poisoning")
        return
    tmp = beer
    beer -= 1
    print ("{} bottles of beer on the wall. {} bottles of beer. "
           "Take one down, pass it around, {} bottles of beer on the wall".format(tmp, tmp, beer))
    bottles_of_beer(beer)


bottles_of_beer(99)

print('\n')
print('\n')


def one_digit_sum(num):
    """
    Add any non-negative number's digits until a sum appears
    that only has one digit
    :param num: starting number (int)
    :return: single digit int
    """
    num = str(num)
    if len(num) == 1:
        return int(num)
    sum = 0
    for n in num:
        sum += int(n)
    return one_digit_sum(sum)


print (one_digit_sum(99))