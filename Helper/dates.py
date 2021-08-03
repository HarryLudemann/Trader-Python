import datetime

def get_dates(Months):
    """
    Gets start and end date, current date and current date - Months Arg
    :param Months int:
    :return 2 strings:
    """
    # Current date
    end_date = datetime.datetime.now().strftime("%Y-%m-%d")  
    # Current Date - Get_Months months
    start_date = datetime.datetime.strptime(end_date, "%Y-%m-%d") - datetime.timedelta(days=30*Months)  

    # start date correction 
    start_date = start_date.strftime("%Y-%m-%d")                                # format date
    end_day = str( datetime.datetime.strptime(end_date, "%Y-%m-%d").day )       # get days of end date
    if len(end_day) == 1:    end_day = '0' + end_day                            # ensure date format - eg date is 03 not 3
    start_date = start_date[:-2] + end_day                                      # set start date to end dates day

    return start_date, end_date


