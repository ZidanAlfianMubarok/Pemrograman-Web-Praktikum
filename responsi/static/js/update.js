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
                    particle.vx *= -1;
                }

                if (particle.y + particle.radius > canvas.height || particle.y - particle.radius < 0) {
                    particle.vy *= -1;
                }
            }

            requestAnimationFrame(draw);
        }

        draw();