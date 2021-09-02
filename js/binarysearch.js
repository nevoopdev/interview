function binary(arr, target) {
  let first = 0;
  let second = arr.length - 1;

  while (first <= second) {
    let mid = Math.floor((first + second) / 2);

    if (arr[mid] == target) {
      return mid;
    } else if (arr[mid] < target) {
      first = mid + 1;
    } else {
      second = mid - 1;
    }
  }
}

let index = binary([1, 2, 3], 5);

if (index) {
  console.log("index is at " + index);
} else {
  console.log("thers is no element");
}
