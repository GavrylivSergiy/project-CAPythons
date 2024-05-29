document.addEventListener("DOMContentLoaded", function() {
    const text = "CAPythonsBook - консольний додаток для зберігання контактів, який був розроблений мовою Python. Додаток дозволить користувачам зберігати інформацію про контакти, що можуть містити крім імен: номери телефонів, дні народження, адреса та email.   ";
    let index = 0;
    const speed = 30; // Швидкість набору тексту (в мілісекундах)
    const container = document.querySelector(".text-overlay");

    function typeText() {
        if (index < text.length) {
            container.innerHTML += text.charAt(index);
            index++;
            setTimeout(typeText, speed);
        }
    }

    typeText();
});