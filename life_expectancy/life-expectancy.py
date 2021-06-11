def get_stats(year=0):
    """ get stats from the .csv:
    skip the first line of the file, and iterate line by line
    find the life expectancy (line[3] given the .csv structure)
    calculate average, lowest and highest ages
    """
    # variables to find
    num_of_countries = 0
    cumulative_age_sum = 0
    max_age = {
        'country': 'Name',
        'year': 1900,
        'age': 0.0  # make this too small
    }
    min_age = {
        'country': 'Name',
        'year': 1900,
        'age': 150.0  # make this too big
    }
    avg_age = 0.0

    # open file
    with open('life_expectancy\life-expectancy.csv') as open_file:

        # skip first line
        next(open_file)

        # start counting
        for line in open_file:

            # get the age
            strip_line = line.strip()
            data = strip_line.split(',')
            age = float(data[3])

            # if we're only looking at a certain year, and a non-zero year has been provided, skip all the other years
            if year != 0 and int(data[2]) != year:
                next(open_file)
            elif year != 0 and int(data[2]) == year:
                # add the age to cumulative to calc average later
                num_of_countries += 1
                cumulative_age_sum += age

            # if the age is higher than the previous high, then it is the new highest age
            if age > max_age["age"]:
                max_age["age"] = age
                max_age["country"] = data[0]
                max_age["year"] = data[2]
            # if the age is lower than the last one, then it is the new lowest age
            if age < min_age["age"]:
                min_age["age"] = age
                min_age["country"] = data[0]
                min_age["year"] = data[2]

    if year != 0:
        # get the average age
        avg_age = cumulative_age_sum/num_of_countries
        return max_age, min_age, avg_age
    else:
        return max_age, min_age


def main():
    """ main funct. """

    year_of_interest = int(input('Enter the year of interest: '))

    max_age, min_age = get_stats()
    print(
        f'The overall max life expectancy is: {max_age["age"]} from {max_age["country"]} in {max_age["year"]}')
    print(
        f'The overall min life expectancy is: {min_age["age"]} from {min_age["country"]} in {min_age["year"]}')

    # now for the year
    max_age, min_age, avg_age = get_stats(year_of_interest)

    print(f'\nFor the year {year_of_interest}:')
    print(f'The average life expectancy across the world was {avg_age:.3f}')
    print(
        f'The max life expectancy was in {max_age["country"]} with {max_age["age"]}')
    print(
        f'The min life expectancy was in {min_age["country"]} with {min_age["age"]}')


if __name__ == '__main__':
    main()
