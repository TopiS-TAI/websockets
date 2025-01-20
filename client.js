const chat = document.getElementById('chat')
const message = document.getElementById('message')
let socket

fetch('./config.json')
    .then(res => res.json())
    .then(res => {
        socket = new WebSocket('ws://' + res.serverIp + ':' + res.serverPort + '/web')
        socket.addEventListener('open', function (event) {
            socket.send('Connection Established');
        });
        
        socket.addEventListener('message', function (event) {
            console.log(event.data);
            const newMsg = document.createElement('p')
            newMsg.innerHTML = event.data
            chat.appendChild(newMsg)
        });
        socket.send("Initialize");
        })
 
function send() {
    console.log('message', message)
    socket.send(message.value)
    const newMsg = document.createElement('p')
    newMsg.className = 'me'
    newMsg.innerHTML = message.value
    chat.appendChild(newMsg)
}