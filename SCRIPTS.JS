// =========================
//      SLIDER AUTOMÁTICO
// =========================

const slides = document.querySelectorAll(".slide");

let indice = 0;

function cambiarSlide() {

    // Oculta todas las imágenes
    slides.forEach(slide => {
        slide.classList.remove("active");
    });

    // Pasa a la siguiente
    indice++;

    if(indice >= slides.length){
        indice = 0;
    }

    // Muestra la nueva imagen
    slides[indice].classList.add("active");
}

// Cambia cada 5 segundos
setInterval(cambiarSlide, 5000);


// =========================
// EFECTO HEADER AL HACER SCROLL
// =========================

const header = document.querySelector("header");

window.addEventListener("scroll", () => {

    if(window.scrollY > 50){

        header.style.background = "rgba(0,0,0,.90)";
        header.style.padding = "15px 80px";
        header.style.transition = ".4s";

    }else{

        header.style.background = "rgba(0,0,0,.35)";
        header.style.padding = "20px 80px";

    }

});


// =========================
// ANIMACIÓN DE BOTONES
// =========================

const botones = document.querySelectorAll("button");

botones.forEach(btn => {

    btn.addEventListener("mouseenter", () => {

        btn.style.transform = "scale(1.08)";

    });

    btn.addEventListener("mouseleave", () => {

        btn.style.transform = "scale(1)";

    });

});


// =========================
// SCROLL SUAVE
// =========================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function(e){

        e.preventDefault();

        const destino = document.querySelector(this.getAttribute("href"));

        if(destino){

            destino.scrollIntoView({
                behavior:"smooth"
            });

        }

    });

});