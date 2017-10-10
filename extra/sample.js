function printEveryOtherItem(strings) {
  let index = 0;
  strings.forEach( (string) => {
    if(index % 2 == 0) {
      console.log(string);
    }
  });
  index ++;
}

printEveryOtherItem(["a", "b", "c"])

var x;

x = "hello";

function doSomething() {
  x = "Xebra";
}

doSomething();
console.log(x);
