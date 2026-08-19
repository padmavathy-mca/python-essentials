import time
import random   

# USER-DEFINED (CUSTOM) EXCEPTION
# -------------------------------
class CardExpiredError(Exception):
    '''Exception raised when a user tries to pay with an expired credit card'''
    def __init__(self, expiry_date, message='The provided credit card has expired'):
        self.expiry_date = expiry_date
        self.message = message
        super().__init__(self.message)

# SIMULATED PAYMENT GATEWAY (API)
# -------------------------------
class SimulatedStripeGateway:
    
    def process_charge(self, card_number, amount, card_expiry_year):
        print(f'[Gateway] Contacting bank to charge ₹{amount}...')
        time.sleep(0.7)
        
        # Trigger Custom User-Defined Exception
        # Assuming the current year is 2026
        if card_expiry_year < 2026:
            raise CardExpiredError(expiry_date=card_expiry_year)
            
        # Trigger Built-in System Exceptions
        if card_number == 'TIMEOUT':
            raise TimeoutError('The gateway server failed to respond.')
            
        if amount > 10000:
            raise RuntimeError('Transaction Declined: Insufficient balance.')
            
        return {'status': 'SUCCESS', 'transaction_id': f'tx_{random.randint(1000, 9999)}'}

# NEW VALIDATED INPUT FUNCTIONS
# -----------------------------
def get_valid_card_number():
    while True:
        # Get input, remove leading/trailing spaces, and convert to uppercase
        card_input = input("Enter Card Number (or type 'TIMEOUT'): ").strip().upper()
        
        # 1. Allow the special gateway testing keyword to pass through
        if card_input == 'TIMEOUT':
            return card_input
            
        # 2. Check if the input consists only of numbers and is exactly 12 digits long
        if card_input.isdigit() and len(card_input) == 12:
            return card_input
            
        # 3. Show a clear error message if the input fails the rules above
        print('Validation Error: Card number must be exactly 12 digits and contain only numbers.')
        
def get_valid_amount():
    while True:
        try:
            amount = float(input('Enter Bill Amount (₹): '))
            if amount <= 0:
                print('Validation Error: Bill amount must be greater than ₹0.')
                continue
            return amount
        except ValueError:
            print('Validation Error: Please enter a valid decimal number for the amount.')

def get_valid_expiry_year():
    while True:
        try:
            year = int(input('Enter Card Expiry Year (4 digits, e.g., 2028): '))
            
            # FIXED VALIDATION: Only check if it's a realistic 4-digit calendar year format.
            # This allows years like 2023 to pass through to the gateway!
            if year < 1000 or year > 3000:
                print('Validation Error: Please enter a realistic 4-digit calendar year.')
                continue
                
            return year
            
        except ValueError:
            print('Validation Error: Please enter a valid whole number for the year.')
            
# CORE APPLICATION WITH EXCEPTION HANDLING
# ----------------------------------------
def checkout_cart(user_card, total_amount, expiry_year):
    
    gateway = SimulatedStripeGateway()   
    print('\n--- INITIATING CHECKOUT ---')
    
    try:
        # Risky payment block
        receipt = gateway.process_charge(user_card, total_amount, expiry_year)
        
    except CardExpiredError as exp_err:
        # CATCHING THE USER-DEFINED EXCEPTION
        print(f'Security Block: {exp_err.message} (Expired in: {exp_err.expiry_date})')
        print('Action: Please update your payment profile with a valid card.')
        
    except TimeoutError as net_err:
        print(f'Connection failed: {net_err}')
        print('Action: Do not refresh. Checking payment status asynchronously...')
        
    except RuntimeError as decline_err:
        print(f'Bank Response: {decline_err}')
        print('Action: Order cancelled. Please try an alternative payment method.')
        
    else:
        print(f"Success! Order processed. Transaction ID: {receipt['transaction_id']}")
        
    finally:
        print('Transaction session closed. Clearing sensitive card memory.')

if __name__ == '__main__':
    
    print('=== Welcome to the Interactive Payment Tester ===')
    print('Keys to trigger errors:')
    print(" - Type 'TIMEOUT' as the card number to test internet drops.")
    print(' - Type an amount greater than 10000 to test insufficient funds.')
    print(' - Type a year before 2026 to test the custom expired card error.\n')

    try:
        # Get data from the user dynamically
        card = get_valid_card_number()
        amount = get_valid_amount()
        year = get_valid_expiry_year()
        
        # Run the checkout logic with the user's data
        checkout_cart(user_card=card, total_amount=amount, expiry_year=year)
        
    except ValueError:
        # This catches if the user types letters instead of numbers for Amount or Year
        print('\n Please enter valid numbers for Amount and Year!')

    
