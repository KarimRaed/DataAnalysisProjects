import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = (input(' The city is (chicago/ new york city/ washington):')).lower()
        if city !='chicago' and city !='washington' and city !='new york city':
            print('That\' s not a valid city name!')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    month = (input(' Specifiy the month [all, january, february, ... , june]:')).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = (input(' Specifiy the day of the week [all, monday, tuesday, ... sunday]:')).lower()

    print('-'*40)
    return city, month, day

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

    df = pd.read_csv(CITY_DATA[city])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # First, we need to convert the Start time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    common_month = df['Start Time'].dt.month.mode()[0]
    months_name = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months_name[common_month-1]
    print('The most commn month is:', month.title())

    # TO DO: display the most common day of week
    common_day = df['Start Time'].dt.weekday.mode()[0]
    weekdays = ['monday', 'tuesday', 'wedensday','thursday','friday','sunday','saturday']
    day  = weekdays[common_day]
    print('The most commn day of the week is:', day.title())

    # TO DO: display the most common start hour
    print('The most commn starting hour:', df['Start Time'].dt.hour.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    print()
    # Initial function to estimate the time that this fuction will take
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used Start Station:', df['Start Station'].value_counts().idxmax())
    print()
    # TO DO: display most commonly used end station
    print('The most commonly used End Station:', df['End Station'].value_counts().idxmax())
    print()
    # TO DO: display most frequent combination of start station and end station trip
    x = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent combination of start station and end station trip', x)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print('The total travel time is :', df['Trip Duration'].sum(), 'sec.')

    # TO DO: display mean travel time
    print('The average travel time is :', df['Trip Duration'].mean(), 'sec.')


    print("\nThis took %s seconds." % (time.time() - start_time), 'sec.')
    print('-'*40)


def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df.groupby(['User Type'])['User Type'].count())
    print()

    # TO DO: Display counts of gender
    print(df.groupby(['Gender'])['Gender'].count())
    print()

    # TO DO: Display earliest, most recent, and most common year of birth
    print('The earliest year of birth is :', int(df['Birth Year'].min()))
    print('The most recent year of birth is :', int(df['Birth Year'].max()))
    print('The most common year of birth is :', int(df['Birth Year'].mode()[0]))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        start_loc = 0
        keep_asking = True
        while (keep_asking):
            pd.set_option('display.max_columns',None)
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5
            view_display = input("Do you wish to print more 5 lines?: (yes/no) ").lower()
            if view_display =='no':
                keep_asking = False

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
