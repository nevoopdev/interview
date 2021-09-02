// const LinkedList = require("./linked_list");

// const ll = LinkedList.fromvalues(12, 34, 5, 464, 657);
// console.log(ll);

// console.log(ll.getbyindex(2).next);
// ll.print();

// let dd = LinkedList.fromvalues(12, 23, 34, 53, 44);
// dd.print();
// console.log("after reverse");
// dd.reverse();
// dd.print();

// REVERSE STRING WITH PRESERVE SPACES

// let str = "this is a variable";

// let str1 = str.split(" ");
// console.log(str1);

// let res = [];

// for (let i = 0; i < str1.length; i++) {
//   let x = "";
//   let y = str1[i].split("");

//   for (let j = y.length - 1; j >= 0; j--) {
//     x = x + y[j];
//   }
//   res.push(x);
// }

// console.log(res);

let str = "i am string";
let str1 = str.split("");

console.log(str1);

let arr = [];

for (let i = 0; i < str1.length; i++) {
  if (str1[i] == " ") {
    arr[i] = " ";
  }
}

let j = str1.length - 1;

for (let i = 0; i < str1.length; i++) {
  if (str1[i] != " ") {
    if (arr[j] == " ") {
      j--;
    }
    arr[j] = str1[i];
    j--;
  }
}

console.log(arr);
