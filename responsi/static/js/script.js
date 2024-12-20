//<!-- Script Toggle Mode -->
// Script Toggle Mode
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;
const themeIcon = document.getElementById('theme-icon');

themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark');
    themeToggle.classList.toggle('dark');

    // Ganti ikon berdasarkan mode
    if (body.classList.contains('dark')) {
        themeIcon.classList.remove('fa-sun');
        themeIcon.classList.add('fa-moon'); // Ganti ikon menjadi bulan
    } else {
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun'); // Kembali ke ikon matahari
    }
});


//partikel smtr
const canvas = document.getElementById('particles');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particles = [];

for (let i = 0; i < 520; i++) {
    particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: Math.random() * 2 - 1,
        vy: Math.random() * 2 - 1,
        radius: Math.random() * 2 + 1,
        color: `hsla(${Math.random() * 360}, 100%, 50%, 0.5)`
    });
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < particles.length; i++) {
        const particle = particles[i];

        ctx.beginPath();
        ctx.arc(particle.x, particle.y, particle.radius, 0, 2 * Math.PI);
        ctx.fillStyle = particle.color;
        ctx.fill();

        particle.x += particle.vx;
        particle.y += particle.vy;

        if (particle.x + particle.radius > canvas.width || particle.x - particle.radius < 0) {
            particle.vx *= -1 ;
        }

        if (particle.y + particle.radius > canvas.height || particle.y - particle.radius < 0) {
            particle.vy *= -1;
        }
    }

    requestAnimationFrame(draw);
}

draw();

// Konfirmasi sebelum hapus produk
document.addEventListener('DOMContentLoaded', function () {
    const deleteForms = document.querySelectorAll('form[action^="/delete/"]');

    deleteForms.forEach(form => {
        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Mencegah pengiriman form langsung

            // Tampilkan SweetAlert konfirmasi
            swal({
                title: "Apakah Anda yakin?",
                text: "Produk ini akan dihapus secara permanen!",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Ya, hapus!",
                cancelButtonText: "Batal",
                closeOnConfirm: false
            }, function (isConfirm) {
                if (isConfirm) {
                    form.submit(); // Lanjutkan penghapusan jika konfirmasi
                }
            });
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    // Cek jika URL mengandung parameter success
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has("success")) {
        // Tampilkan SweetAlert jika data berhasil ditambah
        swal("Berhasil!", "Produk berhasil ditambahkan!", "success");
    }
});

