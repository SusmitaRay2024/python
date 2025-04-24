const socket = io();

function sendMessage() {
    const user = document.getElementById("username").value;
    const msg = document.getElementById("message").value;
    if (user && msg) {
        socket.send(user + ": " + msg);
        document.getElementById("message").value = '';
    }
}

socket.on('message', function(msg) {
    const li = document.createElement("li");
    li.textContent = msg;
    document.getElementById("messages").appendChild(li);
});