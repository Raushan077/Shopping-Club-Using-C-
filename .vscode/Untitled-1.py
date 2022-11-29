def caught_spending(speed, is_birthday):
    
    if is_birthday:
        speeding = speed -5
    else:
        speeding = speed
        
    if speeding > 80:
        return 'Big Ticket'
    elif speeding >60:
        return 'Small Ticket'
    else:
        return 'No Ticket'  