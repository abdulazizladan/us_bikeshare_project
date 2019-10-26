""""
	Import time, pandas, numpy and sys libraries that are necessary for the program to run.
"""
import time
import pandas as pd
import numpy as np
import sys

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
    first_response = input('Hello Master Bruce. Shall we explore some US bikeshare data? : ')
    if first_response == 'y' or first_response == 'yes':
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        print("Please select a city: chicago, new york city OR washington.")
        city = input("Enter city name : ")
        city = city.lower()
        # get user input for month (all, january, february, ... , june)
        print("Please select a Month: january, february, march, april, may, june OR all.")
        month = input("Enter month : ")
        month = month.lower()
        # get user input for day of week (all, monday, tuesday, ... sunday)
        print("Please select a day of week : monday, tuesday, wednesday, thursday, friday, saturday, sunday OR all.")
        day = input("Enter day of week : ")
    
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
    cities = pd.read_csv(CITY_DATA[city])
    df = pd.DataFrame(cities)
    df['Station Combination'] = df['Start Station'] +  ' - ' + df['End Station']
    df['Start Month'] = pd.DatetimeIndex(df['Start Time']).month
    df['Start Hour'] = pd.DatetimeIndex(df['Start Time']).hour
    df['Start Day'] = pd.DatetimeIndex(df['Start Time']).hour
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print(df['Trip Duration'].mean())

    # display the most common month
    print("Most common month : \n\t" , df.groupby('Start Month', sort=True)['Start Month'].count().reset_index(name='Count').sort_values(by=['Count']).tail(1))

    # display the most common day of week
    print("Most common day : \n\t" , df.groupby('Start Day', sort=True)['Start Day'].count().reset_index(name='Count').sort_values(by=['Count']).tail(1))

    # display the most common start hour
    print("Most common month : \n\t" , df.groupby('Start Hour', sort=True)['Start Hour'].count().reset_index(name='Count').sort_values(by=['Count']).tail(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most used start station : \t" , df.groupby('Start Station', sort=True)['Start Station'].count().reset_index(name='Count').sort_values(by=['Count']).tail(1))

    # display most commonly used end station
    print("\nMost used end station : \t" , df.groupby('End Station', sort=True)['End Station'].count().reset_index(name='Count').sort_values(by=['Count']).tail(1))

    # display most frequent combination of start station and end station trip
    print("\nMost used combination of start station and end station : \t" , df.groupby('Station Combination', sort=True)['Station Combination'].count().reset_index(name='Count').sort_values(by=['Count']).tail(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("\tTotal travel time : " , df['Trip Duration'].sum())

    # display mean travel time
    print("\n\tMean travel time : " , df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("\nUser types : \n\tCustomer : \t" , (df['User Type']=='Customer').sum().sum(), " \n\tSubscriber : \t", (df['User Type']=='Subscriber').sum().sum())

    # Display counts of gender
    print("\nGender count : \n\tMale : \t\t" , (df['Gender']=='Male').sum().sum(), " \n\tFemale : \t", (df['Gender']=='Female').sum().sum())


    # Display earliest, most recent, and most common year of birth
    print("\nUsers years of birth : \n\tEarliest year of birth : \t" , (df['Birth Year']).min(), " \n\tMost recent year of birth : \t", (df['Birth Year']).max(), " \n\tMost common birth year : \t", df.groupby('Birth Year', sort=True)['Birth Year'].count().reset_index(name='Count').sort_values(by=['Count']).tail(1)['Birth Year'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        proceed_to_time_stats = input('\nWould you like to see some time statistics? : ')
        if proceed_to_time_stats == 'yes' or proceed_to_time_stats == 'y':
            time_stats(df)
        else: 
            print('Very well sir.')
        proceed_to_station_stats = input('\nHow about some station statistics, sir? : ')
        if proceed_to_station_stats == 'yes' or proceed_to_station_stats == 'y':
            station_stats(df)
        else: 
            print('Very good sir.')
        proceed_to_trip_duration_stats = input('Alright sir, how about some trip duration statistics sir? : ')
        if proceed_to_trip_duration_stats == 'y' or proceed_to_trip_duration_stats == 'yes':
            trip_duration_stats(df)
        else: 
            print('As you wish sir.')
        proceed_to_user_stats = input('\nMight I recommend some user statistics sir? : ')
        if proceed_to_user_stats == 'yes' or proceed_to_user_stats == 'y':
            user_stats(df)
        else: 
            print('Alright sir.')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
