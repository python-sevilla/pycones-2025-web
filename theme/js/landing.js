(function () {
    const second = 1000,
        minute = second * 60,
        hour = minute * 60,
        day = hour * 24;

    // Definir la fecha objetivo para el 17 de octubre de este año
    let today = new Date(),
        yyyy = today.getFullYear();

    const eventDate = new Date(`${yyyy}-10-17T00:00:00`);

    // Calcular la cuenta atrás
    const countDown = eventDate.getTime(),
        x = setInterval(function() {
            const now = new Date().getTime(),
                distance = countDown - now;

            document.getElementById("days").innerText = Math.floor(distance / day);
            document.getElementById("hours").innerText = Math.floor((distance % day) / hour);
            document.getElementById("minutes").innerText = Math.floor((distance % hour) / minute);
            document.getElementById("seconds").innerText = Math.floor((distance % minute) / second);

            // Si la fecha ha llegado
            if (distance < 0) {
                document.getElementById("headline").innerText = "¡El evento ha comenzado!";
                document.getElementById("countdown").style.display = "none";
                document.getElementById("content").style.display = "block";
                clearInterval(x);
            }
        }, 1000);
}());
