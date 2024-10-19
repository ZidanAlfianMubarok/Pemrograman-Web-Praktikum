$(document).ready(function() {
    // Ambil nilai success dari elemen tersembunyi
    var success = $('#success').val();

    // Jika success bernilai 'true', tampilkan modal
    if (success === 'true') {
        $('#successModal').modal('show');
    }
});
