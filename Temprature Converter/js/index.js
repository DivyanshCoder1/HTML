function calcfunc() {
    var num = parseInt(document.getElementById("val").value);
    var oper = document.getElementById("oper").value;
    var oper1 = document.getElementById("oper1").value;

    if (oper1 == "Select") {
        if (oper == "Select") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = "Select Units";
            }
        }
        if (oper == "Fa") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = "Select First Unit";
            }
        }
        if (oper == "Ke") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = "Select First Unit";
            }
        }
        if (oper == "Cel") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = "Select First Unit"
            }
        }
    }

    if (oper1 == "Fa") {
        if (oper == "Select") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = "Select Second Unit";
            }
        }
        if (oper == "Fa") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = num;
            }

        }
        if (oper == "Ke") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = (num - 32) * (5 / 9) + 273.15;
            }
        }
        if (oper == "Cel") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = (num - 32) * (5 / 9);
            }
        }
    }

    if (oper1 == "Ke") {
        if (oper == "Select") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = "Select Second Unit";
            }
        }
        if (oper == "Fa") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = (num - 273.15) * (9 / 5) + 32;
            }
        }
        if (oper == "Ke") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = num;
            }
        }
        if (oper == "Cel") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = num - 273.15;
            }

        }
    }

    if (oper1 == "Cel") {
        if (oper == "Select") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = "Select Second Unit";
            }
        }
        if (oper == "Fa") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = (num * (9 / 5)) + 32;
            }
        }
        if (oper == "Ke") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = num + 273.15;
            }
        }
        if (oper == "Cel") {
            if (isNaN(num)) {
                document.getElementById("result").innerHTML = "Please Enter a number";
            } else {
                document.getElementById("result").innerHTML = num;
            }
        }
    }
}