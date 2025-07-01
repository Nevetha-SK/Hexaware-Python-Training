// 1. Add Two Numbers using JavaScript
let a = 15;
let b = 10;
let sum = a + b;

console.log("Sum:", sum);  // Output: Sum: 25


// 2. Check if a number is even or odd
let num = 13;

if (num % 2 === 0) {
  console.log(num, "is even");
} else {
  console.log(num, "is odd");
}


// 3. Print numbers from 1 to 6
for (let i = 1; i <= 6; i++) {
  console.log(i);
}


// 4. Reverse a string
let str = "Nevetha";
let reversed = str.split('').reverse().join('');
console.log(reversed);  // Output: ahteveN


// Checking Even and Odd Numbers Using if Inside a for Loop
for (let i = 1; i <= 10; i++) {
  if (i % 2 === 0) {
    console.log(i + " is even");
  } else {
    console.log(i + " is odd");
  }
}


// Check and print whether numbers from 2 to 20 are prime or not
for (let num = 2; num <= 20; num++) {
  let isPrime = true;
  
  // Check if num is divisible by any number from 2 to num-1
  for (let i = 2; i < num; i++) {
    if (num % i === 0) {
      isPrime = false;
      break;  // No need to continue if not prime
    }
  }

  // Output result
  if (isPrime) {
    console.log(num + " is prime");
  } else {
    console.log(num + " is not prime");
  }
}


//Factorial 
function factorial(n) {
  let result = 1;  // Initialize result variable

  for (let i = 1; i <= n; i++) {
    result *= i;  // Multiply result by current number (i)
  }

  return result;  // Return the factorial value
}
// Example usage:
let number = 5;
console.log("Factorial of " + number + " is: " + factorial(number)); 


// Split the String into words
let sentence1 = "Hello My Name is Java Script";
let words = sentence1.split(" ");
console.log(words);


// Split with Limit
let sentence2 = "apple,banana,cherry,grape";
let limitedSplit = sentence2.split(",", 2);
console.log(limitedSplit); 
// Output: [ 'apple', 'banana' ]


// Split Using Regular Expression
let sentence3 = "apple123banana456cherry789";
let splitWords = sentence3.split(/\d+/); // Split by one or more digits
console.log(splitWords); 
// Output: [ 'apple', 'banana', 'cherry' ]


// Split Using an Empty String
let word = "hello";
let letters = word.split("");
console.log(letters); 
// Output: [ 'h', 'e', 'l', 'l', 'o' ]


// Split by Multiple Delimiters
let sentence = "apple,banana|cherry grape";
let fruits1 = sentence.split(/[,| ]/); // Split by comma, pipe, or space
console.log(fruits1); 
// Output: [ 'apple', 'banana', 'cherry', 'grape' ]


// Access and Length of Array
let fruits2 = ["apple", "banana", "cherry", "apple"];
console.log(fruits2[0]);       // Output: "apple"
console.log(fruits2.length);   // Output: 4


// Creating a Map to track visits
const visits = new Map();

const user = { id: 6 };  // an object as a key
visits.set(user, 13);     // map object key to value 5
visits.set("anonymous", 1); // map string key to value 1

console.log(visits.get(user));        // Output: 5
console.log(visits.has("anonymous")); // Output: true
console.log(visits.size);             // Output: 2

// Loop through all entries in the map
for (const [k, v] of visits.entries()) {
  console.log(k, v);
}

/* Output:
5
true
2
{ id: 1 } 5
anonymous 1
*/

