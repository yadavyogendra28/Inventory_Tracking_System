function validation() {
    var name = document.getElementById('username').value;
    var pass = document.getElementById('password').value;

    if (name == "") {
        alert("Please enter user name !!");
        document.getElementById('username').focus();
        return false;
    }
    if (pass == "") {
        alert("Please enter password !! ");
        document.getElementById('password').focus();
        return false;
    }
}

function tba_yes(that) {
    if (that.value == "Yes") {
        alert("check");
        document.getElementById("ifYes").style.display = "block";

    } else {
        document.getElementById("ifYes").style.display = "none";
    }

}

function display() {
    alert("Hello! I am an alert box!");
}