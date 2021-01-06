package BankAccountManager;

public class SavingsAccount extends Account {

    private double balance;
    private double interestRate;
    private int withdrawalCount;

    public SavingsAccount() {
        balance = 0;
        interestRate = 0.06; // Average interest rate for Checking accounts is 0.04%
        withdrawalCount = 0;
    }

    @Override
    public void withdraw(int money) {
        // For a savings account, there is a limit of six withdrawals per month
        if (balance >= money && withdrawalCount < 6) {
            balance -= money;
            withdrawalCount++;
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

    public int getWithdrawalCount() {
        return withdrawalCount;
    }
}
