// var x = 5;
    

// function setX(newValue) {
//     x = newValue;
// }
    

// console.log(x);
// // Output: 5
// setX(15);
// // x=15
// // setX(newValue)



// // setX(newValue)
// console.log(x);
// // Output: 15




// var x = 5;
    
// function addToX(amount) {

//     return x + amount;
//     // 5+ -10
//     console.log("hello there");
// }
    
// console.log(x);
// // Output 5

// var result = addToX(-10);
// // result = -5



// console.log(result);
// // Output: -5
// console.log(x);
// // Output: 5



function isPal(arr) {
    for(var left=0; left<arr.length/2; left++) {
        var right = arr.length-1-left;
        if(arr[left] != arr[right]) {
            return "Not a pal-indrome!";
        }
    }
    return "Pal-indrome!";
}
    
var result1 = isPal( [1, 1, 2, 2, 1] );
// Output = "Not a pal-indrome!"
console.log(result1);
    
var result2 = isPal( [3, 2, 1, 1, 2, 3] );
console.log(result2);
// Output "Pal-indrome!"


