function inputFields() {
    var firstName = document.getElementById("id_first_name");
    var lastName = document.getElementById("id_last_name");
    var email = document.getElementById("id_email");
    var email2 = document.getElementById("id_email2")
    var phone = document.getElementById("id_phone_number");
    var idea = document.getElementById("id_consultation_idea");


    if (firstName.value == "") {
        firstName.style.boxShadow = "1px 1px 2px black";
        firstName.style.backgroundColor = "rgba(207, 0, 15, 0.2)";
    }

    if (lastName.value == "") {
        lastName.style.boxShadow = "1px 1px 2px black";
        lastName.style.backgroundColor = "rgba(207, 0, 15, 0.2)";
    } 

    if (phone.value == "") {
        phone.style.boxShadow = "1px 1px 2px black";
        phone.style.backgroundColor = "rgba(207, 0, 15, 0.2)";
    }

    if (idea.value == "") {
        idea.style.boxShadow = "1px 1px 2px black";
        idea.style.backgroundColor = "rgba(207, 0, 15, 0.2)";
    }
}