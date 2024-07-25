document.addEventListener("DOMContentLoaded", function() {
    const qrCodeSection = document.getElementById('qrcode');
    const generateQrButton = document.getElementById('generate-qr');

    generateQrButton.addEventListener('click', function() {
        const qr = new QRCode(qrCodeSection, {
            text: "https://example.com/attendance",
            width: 128,
            height: 128,
            colorDark: "#000000",
            colorLight: "#ffffff",
            correctLevel: QRCode.CorrectLevel.H
        });
    });
});
