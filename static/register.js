function validateForm() {
    var fname = document.forms["myForm"]["fname"].value;
    var lname = document.forms["myForm"]["lname"].value;
    var email = document.forms["myForm"]["email"].value;
    var phno = document.forms["myForm"]["phno"].value;
    var pass = document.forms["myForm"]["pass"].value;

    // Check if first name is empty
    if (fname == "") {
        alert("First name must be filled out");
        return false;
    }

    // Check if last name is empty
    if (lname == "") {
        alert("Last name must be filled out");
        return false;
    }

    // Check if email format is valid
    var emailRegex = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    if (!email.match(emailRegex)) {
        alert("Invalid email format");
        return false;
    }

    // Check if phone number contains only digits
    if (!(/^\d+$/.test(phno))) {
        alert("Phone number must contain only digits");
        return false;
    }

    // Check if password meets requirements (e.g., minimum length)
    if (pass.length < 6) {
        alert("Password must be at least 6 characters long");
        return false;
    }
}