var testRegx = ..

function testRegx() {
    var testRegx = /[^a-zA-Z0-9]/;
    var testString = "Hello World!";
    var result = testRegx.test(testString);
    console.log(result);
}