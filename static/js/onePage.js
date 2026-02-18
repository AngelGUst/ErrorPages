const titulos = [
    "Desarrollo Web",
    "Inteligencia Artificial",
    "Base de Datos",
    "Redes Cisco",
    "Seguridad Informática",
    "Diseño UX/UI",
    "Cloud Computing",
    "Internet de las Cosas",
    "Big Data",
    "DevOps"
];

const descripcion = [
    "Aprende las últimas tecnologías del mercado.",
    "El futuro de la tecnología está aquí.",
    "Gestiona grandes volúmenes de información.",
    "Conecta el mundo a través de redes seguras.",
    "Protege la integridad de la información.",
    "Mejora la experiencia del usuario final.",
    "Servicios escalables en la nube.",
    "Conectando dispositivos cotidianos a internet.",
    "Análisis de datos para toma de decisiones.",
    "Integración continua y entrega continua."
]

const imagenes = [
    "/static/img/1.jpg",
    "/static/img/2.jpg",
    "/static/img/3.jpg",
    "/static/img/4.jpg",
    "/static/img/5.jpg",
    "/static/img/6.jpg",
    "/static/img/7.jpg",
    "/static/img/8.jpg",
    "/static/img/9.jpeg",
    "/static/img/10.jpg",
]

function combinacion() {
    const cursos = [];

    const titulosSorteados = [...titulos].sort(() => Math.random() - 0.5);
    const descripcionSorteadas = [...descripcion].sort(() => Math.random() - 0.5);
    const imagenesSorteadas = [...imagenes].sort(() => Math.random() - 0.5);
    
    for (let i = 0; i < titulos.length; i++){
        cursos.push({
            titulos: titulosSorteados[i],
            descripcion: descripcionSorteadas[i],
            imagenes: imagenesSorteadas[i]
        })
    }

    return cursos; 
}

let totalCargas = 0;
let limiteCards = 100;
let mensaje = false;

function agregarCardsConScroll() {
    const cursos = combinacion();
    const contenedor = document.getElementById("cursosContainer");

    cursos.forEach(cursos => {

        if (totalCargas >= limiteCards) {
            return;
        }

        const card = document.createElement("div");
        card.className = "col-md-6 col-lg-4 mb-4";
        card.innerHTML = `
            <div class="card h-100 shadow-sm">
            <img src="${cursos.imagenes}" class="card-img-top" alt="${cursos.titulos}" style="height: 200px; object-fit: cover; width: 100%;">
            <div class="card-body">
                <h5 class="card-title">${cursos.titulos}</h5>
                <p class="card-text">${cursos.descripcion}</p>
            </div>
        </div>
        `;
        contenedor.appendChild(card);
        totalCargas ++;
    });

    if (totalCargas >= limiteCards && !mensaje) {
        mensajeMostrado = true;
        const contenedorPadre = document.getElementById("cursosContainer").parentElement;
        
        const mensaje = document.createElement("div");
        mensaje.className = "alert alert-warning alert-dismissible fade show mt-5 text-center";
        mensaje.role = "alert";
        mensaje.innerHTML = `
            <h4 class="alert-heading">¡Fin de los Cursos!</h4>
            <p>Has explorado todos los <strong>${limiteCards} cursos</strong> disponibles.</p>
            <p>Gracias por tu interés en nuestros cursos. No hay más contenido para cargar.</p>
            <hr>
        `;
        contenedorPadre.appendChild(mensaje);
    }
}

let cargado = false;

window.addEventListener('scroll', () => {

    if (totalCargas >= limiteCards) {
        return;
    }

    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight -500 && !cargado) {
        cargado = true;

        setTimeout(() => {
            agregarCardsConScroll();
            cargado = false;
        }, 1000);
    }
})
