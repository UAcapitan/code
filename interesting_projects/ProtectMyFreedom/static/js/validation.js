
const inputs = document.querySelectorAll("input");

const patterns = {
    username: /^[a-zA-Z0-9_]{1,100}$/,
    email: /^[a-zA-Z0-9.]{1,20}@[a-z]{1,10}\.[a-z]{1,5}$/,
    password: /^[a-zA-Z0-9_\-\.]{8,20}$/
}

function validate(field, regex) {
    if (regex.test(field.value)) {
        field.className = 'form-control valid';
    } else {
        field.className = 'form-control invalid';
    }
}

inputs.forEach((input) => {
    input.addEventListener("keyup", (e) => { 
        if (e.target.attributes.name.value != "re_password") {
            if (e.target.value == '') {
                e.target.className = 'form-control';
            } else {
                validate(e.target, patterns[e.target.attributes.name.value]);
            }
        }

        if (e.target.attributes.name.value == "re_password") {
            if (e.target.value == document.getElementsByName("password")[0].value) {
                e.target.className = 'form-control valid';
            } else {
                e.target.className = 'form-control invalid';
            }
        }

        if (e.target.attributes.name.value == "password") {
            if (e.target.value == document.getElementsByName("re_password")[0].value) {
                document.getElementsByName("re_password")[0].className = 'form-control valid';
            } else {
                document.getElementsByName("re_password")[0].className = 'form-control invalid';
            }
        }
    })
})