package BankAccountManager;

public class CheckingAccount extends Account {

    private double balance;
    private double interestRate;

    public CheckingAccount() {
        balance = 0;
        interestRate = 0.04; // Average interest rate for Checking accounts is 0.04%
    }

    @Override
    public void withdraw(int money) {
        if (balance >= money) {
            balance -= money;
        }
    }

    @Override
    public void deposit(int money) {
        if (money > 0) {
            balance += money;
        }

    }

    @Override
    public double getBalance() {
        return balance;

    }

    @Override
    public double getInterestRate() {
        return interestRate;
    }

}
