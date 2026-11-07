import logging
class InsufficientFundsError(Exception):
    pass
logging.basicConfig(
    filename = 'bank_errors.log',
    level = logging.ERROR,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)
def withdraw_money(balance):
    try:
        amount_str = input("Enter amount to withdraw:")
        amount = float(amount_str)
        if amount > balance:
            raise InsufficientFundsError(f"Cannot withdraw {amount}. Balanceis only {balance}")
        balance -= amount
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        logging.error(f"ValueError: Invalid input '{amount_str}'")
    except InufficientFundsError as e:
        print(f"Error: {e}")
        logging.error(f"InsufficientFundsError: {e}")
    else:
        print(f"Withdrawal successful! New balance is: {balance}")
    finally:
        print("Goodbye! Thank you for banking with us.")
    return balance
if __name__ == "__main__":
    withdraw_money(5000)
