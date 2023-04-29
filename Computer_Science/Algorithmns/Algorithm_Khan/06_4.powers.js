var isEven = function(n) {
    return n % 2 === 0;
};

var isOdd = function(n) {
    return !isEven(n);
};

var power = function(x, n) {
    println("Computing " + x + " raised to power " + n + ".");
    if (n === 0){
        return 1;   
    }
    else if (n <0){
        return 1/power(x,-n);
    }
    else if (isOdd(n) === true){
        return x*power(x,n-1);
    }
    else if (isEven(n) === true){
        var temp = power(x, n/2);
        return temp*temp; 
    }

    // base case
    // recursive case: n is negative 
    // recursive case: n is odd
    // recursive case: n is even
};

var displayPower = function(x, n) {
    println(x + " to the " + n + " is " + power(x, n));
};

displayPower(3, 0);
Program.assertEqual(power(3, 0), 1);
displayPower(3, 1);
Program.assertEqual(power(3, 1), 3);
displayPower(3, 2);
Program.assertEqual(power(3, 2), 9);
displayPower(3, -1);
Program.assertEqual(power(3, -1), 1/3);

displayPower(4, -1);
Program.assertEqual(power(4, -1), 1/4);

displayPower(5, -1);
Program.assertEqual(power(5, -1), 1/5);
