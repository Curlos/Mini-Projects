package BankAccountManager;

public class MainTester {
    public static void main(String[] args) {
        BusinessAccount tesla = new BusinessAccount("Tesla");
        System.out.println(tesla.getCompanyName());
        System.out.println(tesla.getBalance());
        tesla.withdraw(17);
        tesla.deposit(3000);
        tesla.withdraw(17);

        System.out.println(tesla.getBalance());

        CheckingAccount c = new CheckingAccount();
        System.out.println(c.getBalance());
        c.withdraw(17);
        c.deposit(3000);
        c.withdraw(17);
        System.out.println(tesla.getBalance());

        SavingsAccount s = new SavingsAccount();
        System.out.println(s.getBalance());
        s.withdraw(17);
        s.deposit(3000);
        s.withdraw(17);
        System.out.println(s.getBalance());
    }
}
