// Fungsi untuk menghapus pengguna
function deleteUser(id) {
    Swal.fire({
        title: 'Apakah Anda yakin?',
        text: "Data ini akan dihapus!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Hapus',
        cancelButtonText: 'Batal'
    }).then((result) => {
        if (result.isConfirmed) {
            fetch(`/delete_user/${id}`, {
                method: 'DELETE'
            })
            .then(response => response.json())
            .then(data => {
                Swal.fire(
                    'Terhapus!',
                    data.message,
                    'success'
                ).then(() => {
                    location.reload(); // Refresh halaman setelah menghapus
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
}

// Fungsi untuk mengedit pengguna
function editUser(id) {
    Swal.fire({
        title: 'Edit Pengguna',
        html: `
            <input type="text" id="username" class="swal2-input" placeholder="Username">
            <input type="password" id="password" class="swal2-input" placeholder="Password">
            <input type="email" id="email" class="swal2-input" placeholder="Email">
            <input type="text" id="alamat" class="swal2-input" placeholder="Alamat">
            <input type="text" id="nomor_telepon" class="swal2-input" placeholder="Nomor Telepon">`,
        focusConfirm: false,
        preConfirm: () => {
            return {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                email: document.getElementById('email').value,
                alamat: document.getElementById('alamat').value,
                nomor_telepon: document.getElementById('nomor_telepon').value
            }
        }
    }).then((result) => {
        if (result.isConfirmed) {
            fetch(`/edit_user/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(result.value)
            })
            .then(response => response.json())
            .then(data => {
                Swal.fire(
                    'Diperbarui!',
                    data.message,
                    'success'
                ).then(() => {
                    location.reload(); // Refresh halaman setelah mengedit
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
}

// Fungsi untuk menambahkan pengguna
function addUser() {
    Swal.fire({
        title: 'Tambah Pengguna',
        html: `
            <input type="text" id="username" class="swal2-input" placeholder="Username">
            <input type="password" id="password" class="swal2-input" placeholder="Password">
            <input type="email" id="email" class="swal2-input" placeholder="Email">
            <input type="text" id="alamat" class="swal2-input" placeholder="Alamat">
            <input type="text" id="nomor_telepon" class="swal2-input" placeholder="Nomor Telepon">`,
        focusConfirm: false,
        preConfirm: () => {
            return {
                username: document.getElementById('username').value,
                password: document.getElementById('password').value,
                email: document.getElementById('email').value,
                alamat: document.getElementById('alamat').value,
                nomor_telepon: document.getElementById('nomor_telepon').value
            }
        }
    }).then((result) => {
        if (result.isConfirmed) {
            fetch(`/add_user`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(result.value)
            })
            .then(response => response.json())
            .then(data => {
                Swal.fire(
                    'Berhasil!',
                    data.message,
                    'success'
                ).then(() => {
                    location.reload(); // Refresh halaman setelah menambahkan
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
}
