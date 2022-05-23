console.log("Hello");
var message = "world";
console.log(message);

let number = 10;
console.log(number);

function returnOneMore (number)
{
    var result = number;
    result++;
    return result;
}
console.log(returnOneMore(5))

var array = ["First", 43];
console.log(array)
array.push("Last")
console.log(array)

//push to append, pop to extract the last, shift to extract the first, unshift to prepend

function nextInLine(arr, item) //append item to arr and return the first element
{
    arr.push(item);
    return arr.shift();
}
var testArr = [1,2,3,4,5];
console.log("Before: " +JSON.stringify(testArr));
console.log(nextInLine(testArr, 6))
console.log("After: " + JSON.stringify(testArr));

testArr[7] = 90
console.log(testArr)

/* strictly equal
3 === 3 is true
3 === "3" is false (type conversion is not made automatically
 */
// == does type conversion automatically if needed
// === does not
function compareElements(a, b)
{
    if (a === b)
    {
        return true;
    }
    else
        return false;
}    
console.log(compareElements(5, '5'))
console.log(compareElements(5, 5))

let person =
    {
    "name": "John",
    "age": 99
    }

console.log(person.name)
console.log(person["age"])
console.log(typeof person)

let students =
    {
        12345: {
            "name": "ABC",
            "last": "DEF",
            "grade": 11
        },
        67890: {
            "name": "GHI",
            "last": "JKL",
            "grade": 12
        }
    }
console.log(students[12345])