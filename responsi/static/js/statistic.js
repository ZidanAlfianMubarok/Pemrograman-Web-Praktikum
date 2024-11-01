document.addEventListener('DOMContentLoaded', function() {
    const dataContainer = document.getElementById('dataContainer');
    const labels = JSON.parse(dataContainer.getAttribute('data-labels'));
    const data = JSON.parse(dataContainer.getAttribute('data-data'));

    // Sekarang Anda bisa menggunakan labels dan data
    console.log(labels, data);
    
    // Contoh penggunaan dalam chart
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                label: 'Jumlah Barang Masuk',
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)',
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(153, 102, 255, 0.6)',
                    'rgba(255, 159, 64, 0.6)',
                    'rgba(255, 99, 71, 0.6)'
                ],
                borderColor: 'rgba(0, 0, 0, 0.1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
        }
    });
});

