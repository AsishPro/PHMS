document.getElementById('symptomForm').addEventListener('submit', function(event) {

    console.log("ENTEEREDDD INTO THIS BLOCK")

    var symptom1 = document.getElementById('symptom1').value;
    var symptom2 = document.getElementById('symptom2').value;
    var symptom3 = document.getElementById('symptom3').value;
    var symptom4 = document.getElementById('symptom4').value;
    
    if (symptom1 === "" || symptom2 === ""  || symptom3 === "" ||  symptom4 === "") { // Add more conditions for other symptoms
        alert("Please select all symptoms.");
        event.preventDefault(); 
        // Prevent form submission if symptoms are null
    }
    
});


// document.addEventListener('DOMContentLoaded', function() {
//     var symptoms = {{ symptoms | tojson }}; // Fetch initial list from Flask
//     console.log(symptoms)

// });



// console.log("Asish")
// alert("please enter the symptoms")      

// document.addEventListener("DOMContentLoaded", function() {
//     console.log("Asish")
//     alert("please enter the symptoms")      
// });    