def bottles_of_beer():
    number_of_beer_bottles = 99

    while number_of_beer_bottles > 0:
        if number_of_beer_bottles == 2:
            print(f'{number_of_beer_bottles} bottles of beer on the wall, {number_of_beer_bottles} bottles of beer.')
            number_of_beer_bottles -= 1
            print(f'Take one down, pass it around, {number_of_beer_bottles} bottle of beer on the wall')

        elif number_of_beer_bottles == 1:
            print(f'{number_of_beer_bottles} bottle of beer on the wall, {number_of_beer_bottles} bottle of beer.')
            number_of_beer_bottles -= 1
            print(f'Take one down, pass it around, {number_of_beer_bottles} bottle of beer on the wall')

        print(f'{number_of_beer_bottles} bottles of beer on the wall, {number_of_beer_bottles} bottles of beer.')
        number_of_beer_bottles -= 1
        print(f'Take one down, pass it around, {number_of_beer_bottles} bottles of beer on the wall')


bottles_of_beer()
