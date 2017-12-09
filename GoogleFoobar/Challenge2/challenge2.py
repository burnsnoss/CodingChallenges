def answer(total_lambs):
    # The fibonacci sequence will be the stingiest method of payment
    # The most generous will be doubling the previous henchman's pay
    
    # Cast total_lambs as an int just in case
    total_lambs_int = int(total_lambs)
    
    # This is the base case for both ways of doing things, total_lambs = 10
    stingy_payments = [1, 1, 2, 3]
    generous_payments = [1, 2, 4]
    
    # Use these booleans to let us know when we've reached our goal
    #  payments in both the stingy and generous ways of paying out
    stingy_complete = False
    generous_complete = False
    
    # Initialize totals. Do not initialize them with the last payment,
    #  as we will add it in the while loop
    total_stingy = 4
    total_generous = 3
    
    while not stingy_complete or not generous_complete:

        # Steps in each loop:
        #  1. Total up the payments
        #  2. Check if payments are greater than total_lambs
        #     a. If yes, remove last payment
        #        i. If it is the generous method, see if you can't fit more lambs in the payments
        #     b. If no, add another payment via whichever method
    
        if not stingy_complete:
            # Total up the payments
            total_stingy += stingy_payments[-1]
            
            # If the totals are beyond what we can pay the henchmen,
            #  make the appropriate boolean True and finalize the payments list
            if total_stingy > total_lambs_int:
                stingy_complete = True
                total_stingy -= stingy_payments.pop()

            # Else, we can potentially pay the henchmen more
            # Add another payment to the payments list using the fibonacci sequence
            else:
                stingy_payments.append(stingy_payments[-2] + stingy_payments[-1])
            
        if not generous_complete:
            # Total up payments
            total_generous += generous_payments[-1]
            
            # Do the same as above but for the generous_payments
            if total_generous > total_lambs_int:
                # See if we can't add another henchman here and still follow the rules
                total_generous -= generous_payments.pop()

                # Take the lambs you have leftover. If you can give the last henchman
                #  these lambs and still follow the rules, then do it
                remaining_lambs = total_lambs_int - total_generous

                if remaining_lambs >= (generous_payments[-1] + generous_payments[-2]):
                    generous_payments.append(remaining_lambs)
                    total_generous += remaining_lambs

                generous_complete = True
                
            # Add another payment via the doubling method
            else:
                generous_payments.append(generous_payments[-1] * 2)
        
            
    print 'Stingy: ', stingy_payments
    print 'Total: ', total_stingy
    print 'Generous: ', generous_payments
    print 'Total: ', total_generous
    return len(stingy_payments) - len(generous_payments)


if __name__ == '__main__':
    n = raw_input('DO IT: ')
    ans = answer(n)
    print 'Answer: ', ans