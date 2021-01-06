package BankAccountManager;

abstract class Account {
    public abstract void withdraw(int money);

    public abstract void deposit(int money);

    public abstract double getBalance();

    public abstract double getInterestRate();
}
