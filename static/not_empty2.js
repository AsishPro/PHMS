// this code is for disabling options.
document.getElementById('symptomForm').addEventListener('submit', function(event) {
    console.log("ENTEEREDDD INTO THIS BLOCK")
    var symptom1 = document.getElementById('symptom1').value;
    var symptom2 = document.getElementById('symptom2').value;
    // Add more variables for other symptoms as needed
    
    if (symptom1 === "" || symptom2 === "") { // Add more conditions for other symptoms
        alert("Please select all symptoms.");
        event.preventDefault(); // Prevent form submission if symptoms are null
    }
});


// JavaScript code to remove previously selected options
document.addEventListener('DOMContentLoaded', function() {
    var selects = document.querySelectorAll('select');
    selects.forEach(function(select) {
        select.addEventListener('change', function() {
            var selectedValues = [];
            selects.forEach(function(sel) {
                if (sel.value) {
                    selectedValues.push(sel.value);
                }
            });
            selects.forEach(function(sel) {
                var options = sel.querySelectorAll('option');
                options.forEach(function(option) {
                    if (selectedValues.includes(option.value)) {
                        option.disabled = true;
                    } else {
                        option.disabled = false;
                    }
                });
            });
        });
    });
});

// console.log("Asish")
// alert("please enter the symptoms")      

// document.addEventListener("DOMContentLoaded", function() {
//     console.log("Asish")
//     alert("please enter the symptoms")      
// });    



// document.addEventListener('DOMContentLoaded', function() {
//     var symptoms = {{ symptoms | tojson }}; // Fetch initial list from Flask
//     console.log(symptoms)

//     var selects = document.querySelectorAll('select');
//     selects.forEach(function(select) {
//         select.addEventListener('change', function() {
//             var selectedSymptom = this.value;
//             // Remove selected symptom from the list
//             var index = symptoms.indexOf(selectedSymptom);
//             if (index !== -1) {
//                 symptoms.splice(index, 1);
//             }
//             // Update dropdown menus with modified list
//             updateDropdowns(symptoms);
//         });
//     });

//     function updateDropdowns(symptoms) {
//         selects.forEach(function(select) {
//             select.innerHTML = ''; // Clear existing options
//             var defaultOption = document.createElement('option');
//             defaultOption.value = '';
//             defaultOption.textContent = 'Select Symptom';
//             select.appendChild(defaultOption);
//             symptoms.forEach(function(symptom) {
//                 var option = document.createElement('option');
//                 option.value = symptom;
//                 option.textContent = symptom;
//                 select.appendChild(option);
//             });
//         });
//     }
// });