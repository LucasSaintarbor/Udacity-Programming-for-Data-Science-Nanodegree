"""
Created on Mon Mar 01 17:38:16 2021

@author: Lucas Saintarbor
"""

# Online Resources Referenced
# https://www.askpython.com/python/examples/python-user-input
# https://www.shanelynn.ie/select-data-pandas-iloc-loc-rows-and-columns-dataframe/
# https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python

import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', ' all']

DAY_DATA = ['monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday', 'all']

YES_NO = ['yes', ' no', 'end']

def get_filters():
    '''
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by
        (str) day - name of the day of week to filter by
    """
    '''

    print('\nHello! Let\'s explore some US bikeshare data!')

    print('\nNote: To end this program, type "end"')
<<<<<<< HEAD
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

||||||| 2f05c20
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
=======

    # TO DO: get user input for one city (chicago, new york city, washington). This will return the data for one city. HINT: Use a while loop to handle invalid inputs

>>>>>>> documentation
    city_name = ''

    while city_name.lower() not in CITY_DATA:
<<<<<<< HEAD

        city_name = input("\nWhat city are you interested in analyzing? (E.g. Input either chicago, new york city, washington). To end this program, type 'end'\n")

||||||| 2f05c20
        
        city_name = input("\nWhat city are you interested in analyzing? (E.g. Input either chicago, new york city, washington)\n")
        
=======

        city_name = input("\nWhat city are you interested in analyzing? (E.g. Input either chicago, new york city, washington)\n")

>>>>>>> documentation
        if city_name.lower() in CITY_DATA:
            #We were able to get the name of the city to analyze data.
            city = CITY_DATA[city_name.lower()]

        elif city_name.lower() == 'end':
            raise SystemExit

        else:
            #We were not able to get the name of the city to analyze data so we continue the loop.
            print("Sorry we were not able to get the name of the city. Input either chicago, new york city or washington.\n")

<<<<<<< HEAD
    # TO DO: get user input for month (all, january, february, ... , june)

||||||| 2f05c20
    # TO DO: get user input for month (all, january, february, ... , june)
    
=======
    # TO DO: get user input for one month (all, january, february, ... , june). This will get data for the specified month.

>>>>>>> documentation
    month_name = ''

    while month_name.lower() not in MONTH_DATA:
<<<<<<< HEAD

        month_name = input("\nWhat is the name of the month to filter data? (E.g. Input january, february, ... , june). To end this program, type 'end'\n")

||||||| 2f05c20
        
        month_name = input("\nWhat is the name of the month to filter data? (E.g. Input january, february, ... , june)\n")
        
=======

        month_name = input("\nWhat is the name of the month to filter data? (E.g. Input january, february, ... , june)\n")

>>>>>>> documentation
        if month_name.lower() in MONTH_DATA:
            #We were able to get the name of the month to analyze data.
            month = month_name.lower()

        elif month_name.lower() == 'end':
            raise SystemExit

        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Sorry we were not able to get the name of the month to filter data, input january, february, ... , june.\n")

<<<<<<< HEAD
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

||||||| 2f05c20
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
=======
    # TO DO: get user input for one day of the week (all, monday, tuesday, ... sunday). This will return data for the specified day.

>>>>>>> documentation
    day_name = ''

    while day_name.lower() not in DAY_DATA:
<<<<<<< HEAD
        day_name = input("\nWhat is the name of the day to filter data? (E.g. Input monday, tuesday, ... sunday). To end this program, type 'end'\n")

||||||| 2f05c20
        day_name = input("\nWhat is the name of the day to filter data? (E.g. Input monday, tuesday, ... sunday)\n")
       
=======
        day_name = input("\nWhat is the name of the day to filter data? (E.g. Input monday, tuesday, ... sunday)\n")

>>>>>>> documentation
        if day_name.lower() in DAY_DATA:
            #We were able to get the name of the month to analyze data.
            day = day_name.lower()

        elif day_name.lower() == 'end':
            raise SystemExit

        else:
            #We were not able to get the name of the month to analyze data so we continue the loop.
            print("Sorry we were not able to get the name of the day to filter data, input monday, tuesday, ... sunday.\n")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    '''
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    '''
    # load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.dayofweek
    df['Hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        day = DAY_DATA.index(day)
        df = df.loc[df['Weekday'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print("\nThe most common month from the given fitered data is: " + MONTH_DATA[common_month].title())

    #TO DO: display the most common day of week
    common_day_of_week = df['Weekday'].mode()[0]
    print("\nThe most common day of week from the given fitered data is: " + str(common_day_of_week))

    # TO DO: display the most common start hour
    common_start_hour = df['Hour'].mode()[0]
    print("\nThe most common start hour from the given fitered data is: " + str(common_start_hour))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station from the given fitered data is: " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\nThe most commonly used end station from the given fitered data is: " + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("\nThe most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\nThe total travel time from the given fitered data is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nThe mean travel time from the given fitered data is: " + str(mean_travel_time))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe count of user types from the given fitered data is: \n" + str(user_types))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("\nThe count of user gender from the given fitered data is: \n" + str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('\nEarliest birth from the given fitered data is: {}\n'.format(earliest_birth))
        print('\nMost recent birth from the given fitered data is: {}\n'.format(most_recent_birth))
        print('\nMost common birth from the given fitered data is: {}\n'.format(most_common_birth) )

    print("\nThis took %s seconds.\n" % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    #print(df.head())
    #row_num = 0
    view_raw_data = ' '


    start_time = time.time()

    while view_raw_data.lower() not in YES_NO:

       view_raw_data = input('\nWould you like to view some of the raw data? Enter yes or no.\n')

    while view_raw_data.lower() in YES_NO:

       if view_raw_data.lower() == 'no':
            return

       elif view_raw_data.lower() == 'yes':

            print('\n The first 20 rows of the data is displayed below: \n')
            print(df.iloc[0:20])
            print('\n Getting your Stats now \n')
            print("\nThis took %s seconds.\n" % (time.time() - start_time))
            print('-'*40)
            break

       elif view_raw_data.lower() == 'end':
            raise SystemExit

       else:
            #We were not able to get the name of the city to analyze data so we continue the loop.
            print("Sorry we were not able to get the name of the city. Input either chicago, new york city or washington.\n")
            break


def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)


        restart = input('\nWould you like to restart or end your analysis? Enter yes to restart or no to end your analysis.\n')

        while True:
            if restart.lower() == 'yes':
                break
            elif restart.lower() != 'yes':
                print("You have chosen to end this program. Thank you.")
                raise SystemExit


if __name__ == "__main__":
    main()
