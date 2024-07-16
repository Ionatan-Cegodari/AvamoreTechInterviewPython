# Import necessary libraries
import datetime

# static values used for the calculations
redemptionStatementDate = datetime.date(2024, 4, 23)
dateOfLoan = datetime.date(2023, 1, 15)
finalyMaturityDate = datetime.date(2024, 3, 24)
finishDate = datetime.date(2024, 4, 24)
facility_b = 250000
facility_c = 25000
arrangementFee = 5000
defaultInterestRate = 2.0

#this is setting the dates for build draw downs, so this one is used for checking the date
buildDrawdownsDates = [
    datetime.date(2023, 2, 14),
    datetime.date(2023, 3, 25),
    datetime.date(2023, 5, 3),
    datetime.date(2023, 6, 11),
    datetime.date(2023, 7, 20),
    datetime.date(2023, 8, 28),
    datetime.date(2023, 10, 6),
    datetime.date(2023, 11, 14),
    datetime.date(2023, 12, 23),
    datetime.date(2024, 1, 31)]
#then this one is used for getting the actual draw down for the specified data, this makes it more dynamic as you can change the draw down amount as not all of them are going to be the same all the time
buildDrawdowns = [
    (datetime.date(2023, 2, 14), 25000),
    (datetime.date(2023, 3, 25), 25000),
    (datetime.date(2023, 5, 3), 25000),
    (datetime.date(2023, 6, 11), 25000),
    (datetime.date(2023, 7, 20), 25000),
    (datetime.date(2023, 8, 28), 25000),
    (datetime.date(2023, 10, 6), 25000),
    (datetime.date(2023, 11, 14), 25000),
    (datetime.date(2023, 12, 23), 25000),
    (datetime.date(2024, 1, 31), 25000)]

#same concept as the above 2
capitalRepaymentDates = [datetime.date(2024,2,23)]
capitalRepayment = [(datetime.date(2024,2,23), 100000)]

#this function is the function that is used for the draw downs and getting the price aka the 25000 by passing through the specific date it wants from the list
def DrawDown (iteration):
#the x is used to basically iterate through the list and set the 25000 draw down value to the dropDownNum
    dates = datetime
    dropDownNum = 0
    x = 0
    for build in buildDrawdowns[iteration]:
        if(x == 0):
            dates = build
            x+=1
        else:
            dropDownNum = build

    return dropDownNum

#this again does the same thing as the def DrawDown however for the capital repayments
def CapitalRepayment (piteration):
    dates = datetime
    dropDownNum = 0
    x = 0
    for build in capitalRepayment[piteration]:
        if(x == 0):
            dates = build
            x+=1
        else:
            dropDownNum = build

    return dropDownNum

#this runs the actual calculation and does all of the maths, by using the data passed through the parameters to calculate the total end value
def ChooseCalc (pfacility_a, pcontractualMonthlyRate, pbeginningOfDefaultPeriod, pendOfDefaultPeriod):
    # calculation variables
    interestRetention = facility_c - arrangementFee
    impliedDailyRegularRate = pcontractualMonthlyRate / 30
    annualRate = pow(1 + 0.03/100, 365) - 1 * 0.1
    impliedDailyDefaultRate = defaultInterestRate / 30

    # for the foreach loop
    openingPB = pfacility_a + arrangementFee
    closingPB = 0
    interestBalance = 20000
    drawDown = 0
    dailyInterest = 0
    accruedDailyInterest = 0
    paymentsRecieved = 0
    buildDrawDownsIteration = 0 # this iteration is made for the drawDown so that each date that gets called the correct drawdown amount is pulled incase the darwdown amount changes for a certain date
    capitalRepaymentIteration = 0 # used for the same as the buildDrawDownsIteration variable

    print("The range of dates:")
    # Calculate the differences using range()
    for delta in range((pendOfDefaultPeriod - dateOfLoan).days + 1):

        result_date = dateOfLoan + datetime.timedelta(days=delta)

        if (result_date in buildDrawdownsDates):
            drawDown = DrawDown(buildDrawDownsIteration)
            buildDrawDownsIteration += 1
        else:
            drawDown = 0

        if (result_date in capitalRepaymentDates):
            paymentsRecieved = CapitalRepayment(capitalRepaymentIteration)
            capitalRepaymentIteration += 1
        else:
            paymentsRecieved = 0

        if (accruedDailyInterest >= interestRetention):
            interestBalance = accruedDailyInterest

        if (result_date >= pbeginningOfDefaultPeriod):
            dailyInterest = (openingPB + drawDown + interestBalance) * (impliedDailyDefaultRate / 100)
        else:
            dailyInterest = (openingPB + drawDown + interestBalance) * (impliedDailyRegularRate / 100)

        accruedDailyInterest += dailyInterest

        closingPB = (openingPB + drawDown) - (paymentsRecieved)

        print(result_date)
        print(int(dailyInterest))
        print(openingPB)
        print(int(interestBalance))
        print("Total Interest Due:", round(accruedDailyInterest))
        print("---------------------------------")

        openingPB = closingPB
    return round(accruedDailyInterest)

# the dynamic variables that you can change and are passed through to the ChooseCalc function
facility_a = 100000
contractualMonthlyRate = 0.8
beginningOfDefaultPeriod = datetime.date(2024, 3, 24)
endOfDefaultPeriod = datetime.date(2024,4,23)
#calls the function
ChooseCalc(facility_a, contractualMonthlyRate, beginningOfDefaultPeriod, endOfDefaultPeriod)


