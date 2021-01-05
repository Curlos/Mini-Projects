// Create a class called Person which will have a name, when they were born and when (and if) they died. Allow the user to create these Person classes and put them into a family tree structure. Print out the tree to the screen.

class Person {
    name: string;
    dateOfBirth: Date;
    dateOfDeath: Date;

    constructor(name: string, dateOfBirth: Date, dateOfDeath: Date) {
        this.name = name;
        this.dateOfBirth = dateOfBirth;
        this.dateOfDeath = dateOfDeath;
    }

    printPersonInfo() {
        console.log(`Name: ${this.name}, born: ${this.dateOfBirth}, died: ${this.dateOfDeath}`);
    }
}

const grandFather = new Person('Grandfather', new Date('01/01/1800'), new Date('01/26/1897'));
grandFather.printPersonInfo();

const grandMother = new Person('Grandmother', new Date('05/27/1830'), new Date('01/26/1897'));
grandMother.printPersonInfo();

const father = new Person('Father', new Date('01/01/1846'), new Date('09/02/1945'));
father.printPersonInfo();

const mother = new Person('Mother', new Date('12/12/1847'), new Date('02/14/1956'));
mother.printPersonInfo();

const son = new Person('Son', new Date('01/01/1863'), new Date('07/28/1918'));
son.printPersonInfo();

const daughter = new Person('Daughter', new Date('09/01/1872'), new Date('09/01/1939'));
daughter.printPersonInfo();