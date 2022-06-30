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
    city = input(" choose a city to analyze(chicago, new york city, washington)").lower()
    while city not in CITY_DATA.keys():
         print('please enter a valid city')
         city = input(" choose a city to analyze(chicago, new york city, washington)").lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january','february','march','april','may','june','all']
    month = input("which month :('january','february','march','april','may','june','all')").lower()
    while month not in months :
        print('please enter a valid month')
        month = input("which month :('january','february','march','april','may','june','all')").lower()

            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    while True:
         day = input("which day('saturday','sunday','monday','tuesday','wednesday','thursday','friday','all')").lower()
         if day in days :
                break
         else:
                  print('please enter a valid day')


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
    #load data file to data frame
    df = pd.read_csv(CITY_DATA[city])
    #convert Start Time column to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #get month and day from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour
  
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        #filter by month
        df = df[df['month'] == month]
        #filter by date
    if day != 'all':
       days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
       df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the common month is : {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('the common day is : {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('the common start hour is : {}'.format(df['Hour'].mode()[0]))

    print("\n This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the common start station is : {}'.format(df['Start Station'].mode()[0]))
    

    # TO DO: display most commonly used end station
    print('the common end station is : {}'.format(df['End Station'].mode()[0]))
    

    # TO DO: display most frequent combination of start station and end station trip
    df['route']=df['Start Station']+","+df['End Station']
    print('the common route is : {}'.format(df['route'].mode()[0]))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time : ',(df['Trip Duration'].sum()).round())

    # TO DO: display mean travel time
    print('average travel time : ',(df['Trip Duration'].mean()).round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame())
    # TO DO: Display counts of gender
    if city != 'washington': 
        print(df['Gender'].value_counts().to_frame())
    # TO DO: Display earliest, most recent, and most common year of birth
        print('the common year of birth is : ',int(df['Birth Year'].mode()[0]))
        print('the earliest year of birth is : ',int(df['Birth Year'].min()))
        print('the recent year of birth is : ',int(df['Birth Year'].max()))
    else: 
        print('no data')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
       
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    print('raw data is available')
    i = 0
    display_raw = input ('may you want to have a look on the raw data? type yes or no?').lower()
    while display_raw == 'yes':
           if i+5 < df.shape[0]:
               print(df.iloc[i:i+5])
           i += 5
           display_raw = input ('may you want to have a look on more 5 raws data? type yes or no?').lower()
         
            
def main():
     while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('thanks:)')
            break
            
if __name__ == "__main__":
    main() 
    
               
