document.querySelector('#menu-icon').addEventListener('click', () => {
    document.body.classList.toggle('sidebar-open');
});

document.querySelector('#icon-close').addEventListener('click', () => {
    document.body.classList.toggle('sidebar-open');
});

// destacar dia atual
const dataAtual = new Date();
const diasCalendario = document.querySelectorAll('.dia-calendario');

diasCalendario.forEach((dia) => {
    if (dia.textContent == dataAtual.getDate()) {
        dia.classList.add('dia-atual');
    }
});

