var video = document.createElement('video');
video.setAttribute('id', 'videoElement');
document.getElementById('cameraFeed').appendChild(video);

function openCamera() {
    fetch('/open_camera')
        .then(response => response.text())
        .then(data => console.log(data));

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            document.getElementById('videoElement').srcObject = stream;
        })
        .catch(function (error) {
            console.error("Error accessing camera: ", error);
        });
}

function closeCamera() {
    fetch('/close_camera')
        .then(response => response.text())
        .then(data => console.log(data));

    var stream = document.getElementById('videoElement').srcObject;
    var tracks = stream.getTracks();

    tracks.forEach(track => track.stop());
    document.getElementById('videoElement').srcObject = null;
}
