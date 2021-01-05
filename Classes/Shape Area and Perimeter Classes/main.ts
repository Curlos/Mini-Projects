// Create an abstract class called Shape and then inherit from it other shapes like diamond, rectangle, circle, triangle etc. Then have each class override the area and perimeter functionality to handle each shape type.

class Shape {
    area(): number {
        return 1;
    }
    perimeter(): number {
        return 1;
    }
}

class Triangle extends Shape {
    base: number;
    height: number;
    sides: Array<number>

    constructor(base: number, height: number, sides: Array<number>) {
        super()
        this.base = base
        this.height = height;
        this.sides = sides;
    }
    area(): number {
        return (this.base * this.height) / 2;
    }
    perimeter(): number {
        return this.sides.reduce((accumulator, currentValue) => accumulator + currentValue);
    }
}

class Square extends Shape {
    side: number

    constructor(side: number) {
        super()
        this.side = side
    }
    area(): number {
        return this.side ** 2
    }
    perimeter(): number {
        return this.side * 4
    }
}

class Rectangle extends Shape {
    width: number
    height: number

    constructor(width: number, height: number) {
        super()
        this.width = width;
        this.height = height;
    }
    area(): number {
        return this.width * this.height;
    }
    perimeter(): number {
        return 2 * (this.width + this.height);
    }
}

class Parallelogram extends Shape {
    base: number;
    height: number;
    sideLength: number

    constructor(base: number, height: number, sideLength: number) {
        super()
        this.base = base
        this.height = height;
        this.sideLength = sideLength;
    }
    area(): number {
        return this.base * this.height;
    }
    perimeter(): number {
        return 2 * (this.base + this.sideLength);
    }
}

class Trapezoid extends Shape {
    base: number;
    height: number;
    sides: Array<number>

    constructor(base: number, height: number, sides: Array<number>) {
        super()
        this.base = base
        this.height = height;
        this.sides = sides;
    }
    area(): number {
        return (this.base * this.height) / 2;
    }
    perimeter(): number {
        return this.sides.reduce((accumulator, currentValue) => accumulator + currentValue);
    }
}

class Circle extends Shape {
    base: number;
    height: number;
    sides: Array<number>

    constructor(base: number, height: number, sides: Array<number>) {
        super()
        this.base = base
        this.height = height;
        this.sides = sides;
    }
    area(): number {
        return (this.base * this.height) / 2;
    }
    perimeter(): number {
        return this.sides.reduce((accumulator, currentValue) => accumulator + currentValue);
    }
}

class Ellipse extends Shape {
    base: number;
    height: number;
    sides: Array<number>

    constructor(base: number, height: number, sides: Array<number>) {
        super()
        this.base = base
        this.height = height;
        this.sides = sides;
    }
    area(): number {
        return (this.base * this.height) / 2;
    }
    perimeter(): number {
        return this.sides.reduce((accumulator, currentValue) => accumulator + currentValue);
    }
}

class Sector extends Shape {
    base: number;
    height: number;
    sides: Array<number>

    constructor(base: number, height: number, sides: Array<number>) {
        super()
        this.base = base
        this.height = height;
        this.sides = sides;
    }
    area(): number {
        return (this.base * this.height) / 2;
    }
    perimeter(): number {
        return this.sides.reduce((accumulator, currentValue) => accumulator + currentValue);
    }
}

const shape = new Shape();
console.log('------------------------------------')

const triangle = new Triangle(20, 30, [10, 20, 20])
console.log(`Triangle - Area: ${triangle.area()}, Perimeter: ${triangle.perimeter()}`)
console.log('------------------------------------')

const square = new Square(20)
console.log(`Square - Area: ${square.area()}, Perimeter: ${square.perimeter()}`)
console.log('------------------------------------')

const rectangle = new Rectangle(20, 30)
console.log(`Rectangle - Area: ${rectangle.area()}, Perimeter: ${rectangle.perimeter()}`)
console.log('------------------------------------')

const parallelogram = new Parallelogram(20, 30, 40)
console.log(`Parallelogram - Area: ${parallelogram.area()}, Perimeter: ${parallelogram.perimeter()}`)
console.log('------------------------------------')

const trapezoid = new Trapezoid(20, 30, [10, 20, 20])
console.log(`Trapezoid - Area: ${trapezoid.area()}, Perimeter: ${trapezoid.perimeter()}`)
console.log('------------------------------------')

const circle = new Circle(20, 30, [10, 20, 20])
console.log(`Circle - Area: ${circle.area()}, Perimeter: ${circle.perimeter()}`)
console.log('------------------------------------')

const ellipse = new Ellipse(20, 30, [10, 20, 20])
console.log(`Ellipse - Area: ${ellipse.area()}, Perimeter: ${ellipse.perimeter()}`)
console.log('------------------------------------')

const sector = new Sector(20, 30, [10, 20, 20])
console.log(`Sector - Area: ${sector.area()}, Perimeter: ${sector.perimeter()}`)
console.log('------------------------------------')