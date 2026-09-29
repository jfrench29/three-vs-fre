const rulings = [
 '“The format is fair. The vote was 3–1.”',
 '“Your request for teammates has been referred to a committee of our teammates.”',
 '“Being the best golfer is not a recognized scoring category.”',
 '“We considered making it two against one, but that seemed unfair to us.”',
 '“The trophy is regulation size. We wrote the regulations.”',
 '“Your complaint has been printed on next year’s towel.”',
 '“After careful review, we have awarded ourselves another review.”',
 '“You may be entitled to compensation. Unfortunately, we spent it on koozies.”'
];
let rulingIndex = 0;
document.querySelector('#appeal').addEventListener('click', () => {
 rulingIndex = (rulingIndex + 1) % rulings.length;
 document.querySelector('#ruling').textContent = rulings[rulingIndex];
 document.querySelector('#ruling-number').textContent = String(rulingIndex + 1).padStart(3, '0');
});
const dialog = document.querySelector('#photo-dialog');
document.querySelectorAll('[data-image]').forEach(button => button.addEventListener('click', () => {
 const image = document.querySelector('#full-photo');
 image.src = button.dataset.image;
 image.alt = button.querySelector('img').alt;
 document.querySelector('#photo-caption').textContent = button.dataset.caption;
 dialog.showModal();
}));
dialog.querySelector('.close').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => { if (event.target === dialog) { const r=dialog.getBoundingClientRect(); if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom) dialog.close(); } });
