package BankAccountManager;

public class BusinessAccount extends Account {

    private double balance;
    private double interestRate;
    private double monthlyFee;
    private String companyName;

    public BusinessAccount(String companyName) {
        balance = 0;
        interestRate = 0.04; // Average interest rate for Checking accounts is 0.04%
        monthlyFee = 17;
        this.companyName = companyName;
    }

    @Override
    public void withdraw(int money) {
        if (balance >= money) {
            balance -= money;
        } else {
            System.out.println("Not enough money in the account.");
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

    public double getMonthlyFee() {
        return monthlyFee;
    }

    public String getCompanyName() {
        return companyName;
    }

}