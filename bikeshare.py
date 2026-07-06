import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

YES_OPTIONS = {"yes", "y"}
NO_OPTIONS = {"no", "n"}

MONTHS = {'all', 'january', 'february', 'march', 'april', 'may', 'june'}
DAYS = {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}


def ask_choice(question, valid_options):
    while True:
        ans = input(question).strip().lower()
        if ans in valid_options:
            return ans
        else:
            print(f'Invalid input. Choose from: {", ".join(valid_options)}')



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Getting the city from the user

    city_q = "Enter city name (options: chicago, new york city, washington): "
    city = ask_choice(city_q, CITY_DATA)

    # Getting the month from the user

    month_q = "Enter the month you would like to profile (all, january, february, ... , june): "
    month = ask_choice(month_q, MONTHS)

    # Getting the day from the user

    day_q = "Enter the day you would like to view (all, monday, tuesday, ... sunday): "
    day = ask_choice(day_q, DAYS)

    print(f"\nYou've chosen to view data for {city}, month: {month}, day: {day}\n")
    print('-'*40)
    return city, month, day


# Get the filtered dataframe
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Filter by city

    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day of week'] = df['Start Time'].dt.day_name()

    # Filter by month (by name)
    if month != 'all':
        df = df[df['month'] == month.title()] 


    # Filter by day (by name)
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day of week'] == day.title()]
    
    return df


# This function will evaluate user input for questions that require yes/no answers.
def user_input(question):
    """
    Prompts the user on whether they want to view output produced by function.
    
    Args:
        (str) question - the question used in `input()`
    Returns:
        (str) ans - The user's input; can be yes/y or no/n.
    """

    

    while True:
        ans = input(question).strip().lower()
        if ans in YES_OPTIONS:
            return ans
        elif ans in NO_OPTIONS:
            return ans
        else:
            print("Invalid input; please enter yes/y or no/n")


# Printing raw data 5 rows at a time.
def raw_data(df):
    """
    Displays the filtered dataframe 5 rows at each iteration upon the users prompt.
    """

    start_time = time.time()

    ## Generator function yields 5 rows of df at each prompt.
    def chunker(df, size):
        for i in range(0, len(df), size):
            yield df[i:i + size]

    

    counter = 1

    ans = user_input("Would you like to see the raw data?")
    if ans in YES_OPTIONS:
        for chunk in chunker(df, 5):
            if ans in YES_OPTIONS:
                try:
                    display(chunk)
                except Exception:
                    print(chunk)
                counter += 5
                if counter <= len(df):
                    ans = user_input("Print more rows?")
                else:
                    print("End of data.")
                    break
            elif ans in NO_OPTIONS:
                print("Stopped by user.")
                break
    elif ans in NO_OPTIONS:
        print("You've chosen not to display the raw data.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    start_time = time.time()

    # Printing time stats

    

    ans = user_input("Would you like to see the most frequent times of travel?")
    if ans in YES_OPTIONS:
        print('\nCalculating The Most Frequent Times of Travel...\n')

        ## Display the most common month
        print(f"The most travelled month is {df['month'].mode()[0]}")

        ## Display the most common day of week
        print(f"The most common day of week is {df['day of week'].mode()[0]}.")

        ## Display the most common start hour
        start_hour = df['Start Time'].dt.hour.mode()[0]
        display_hour = 12 if start_hour % 12 == 0 else start_hour % 12
        suffix = 'AM' if start_hour < 12 else 'PM'
        print(f'The most common start hour is {display_hour} {suffix}.')
            
    elif ans in NO_OPTIONS:
        print("You've chosen not to display the most frequent times of travel.")

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    start_time = time.time()

    # Printing time stats

    ans = user_input("Would you like to see the most the most popular stations and end-to-end trip points?")
    if ans in YES_OPTIONS:
        print('\nCalculating The Most Popular Stations and Trip...\n')

        ## TO DO: display most commonly used start station
        print(f"The most commonly used start station is {df['Start Station'].mode()[0]}.")

        ## Display most commonly used end station
        print(f"The most commonly used end station is {df['End Station'].mode()[0]}.")

        ## Display most frequent combination of start station and end station trip
        top_combo = df[['Start Station', 'End Station']].value_counts().idxmax()

        print(f"The most frequent combination of start station and end station is {top_combo[0]} to {top_combo[1]}.")
        
    elif ans in NO_OPTIONS:
        print("You've chosen not to display the most popular stations and trip.")
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    start_time = time.time()
    
    # Printing Trip Duration stats

    ans = user_input("Would you like to see statistics on trip duration?")
    if ans in YES_OPTIONS:
        print('\nCalculating Trip Duration...\n')

        ## Total travel time

        total_time = int(df['Trip Duration'].sum().round(0))

        minutes, seconds = divmod(total_time, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        months, days = divmod(days, 30)
        years, months = divmod(months, 12)

        print(f"Total travel time:\n{years}Y {months}M {days}D {hours}h {minutes}m {seconds}s\n")

        ## Travel time is in seconds so I divided by 60 to convert it to minutes

        avg_time = int(df['Trip Duration'].mean().round(0))

        minutes, seconds = divmod(avg_time, 60)
        hours, minutes = divmod(minutes, 60)
        
        print(f"Average travel time:\n{hours}h {minutes}m {seconds}s")
        
    elif ans in NO_OPTIONS:
        print("You've chosen not to display the total and average trip duration.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    start_time = time.time()

    
    if city == 'washington':
        print("No gender and age statistics for Washington. \n")

    elif city != 'washington':
        ans = user_input("Would you like to see statistics on Bikeshare users?")
        if ans in YES_OPTIONS:
            print("\nCalculating age and gender statitics ...\n")
            print("Gender: ")
            
            for index, value in df['Gender'].value_counts().items():
                print(f"{index}: {value}")
            
            print(f"\nThe oldest customer was born on {int(df['Birth Year'].min())}.")
            
            print(f"The youngest customer was born on {int(df['Birth Year'].max())}.")
            
            print(f"The most common year of birth is {int(df['Birth Year'].mode()[0])}.")
            
        elif ans in NO_OPTIONS:
            print("You've chosen not to display statistics on bikeshare users.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        print("\nYou have reached the end of the program.\n")
        
        restart = user_input('\nWould you like to restart? Enter yes or no.\n')
        if restart in NO_OPTIONS:
            break

if __name__ == "__main__":
	main()

