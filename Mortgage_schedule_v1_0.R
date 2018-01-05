## Coding UTF-8
## Author: Andrew M. Telford
## Date: 05 jan 2018
## Version: 1.0

## This script calculates the time required to pay off a mortgage,
## and produces a schedule of the payments on a monthly basis

calc_schedule <- function() {
    schedule <- data.frame(Month=integer(),
                           Interest_paid=numeric(),
                           Principal_paid=numeric(),
                           New_balance=numeric(),
                           stringsAsFactors=FALSE)  
    P <- as.numeric(readline("Enter principal (and press enter): "))
    PMT <- as.numeric(readline("Enter monthly repayment amount (and press enter): "))
    r <- as.numeric(readline("Enter annual percentage rate (and press enter): "))/100
    schedule[1,1] <- 1 ## Month
    schedule[1,2] <- 0 ## Interest paid
    schedule[1,3] <- 0 ## Principal paid
    schedule[1,4] <- P*(1+r/365)^(365/12) ## New balance
    i <- 1 
    while (schedule[i,4] > 0) {
      i <- i+1
      schedule[i,1] <- i # Month
      schedule[i,2] <- schedule[i-1,4]*(1+r/365)^(365/12)-schedule[i-1,4]
      schedule[i,3] <- PMT-schedule[i,2]
      schedule[i,4] <- schedule[i-1,4]-schedule[i,3]
      if (i == 1000) {break} ## Control to avoid infinite loop
    }
    x <- readline(paste("The mortgage will be paid off in ",
                        schedule[i-1,1]/12,
                        " years\nThe last repayment will be: ",
                        round(PMT+schedule[i,4],2),
                        "\n(press enter to see payment schedule)"))
    return(schedule)
}

