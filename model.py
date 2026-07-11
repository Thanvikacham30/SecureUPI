import os

def predictor(arr):
    try:
        amount = arr[1]
        old_balance = arr[2]
        new_balance = arr[3]

        # Fraud if new balance is less than expected
        if new_balance < abs(amount - old_balance):
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False 
    

        
    

    
