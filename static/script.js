const messageForm = document.getElementById('message-form');
const messageInput = document.getElementById('message-input');
const messagesContainer = document.getElementById('messages');

messageForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const message = messageInput.value;
  const renderedMessage = await sendMessage(message);
  messageInput.value = '';

  const messageElement = document.createElement('div');
  messageElement.innerHTML = renderedMessage;
  messagesContainer.appendChild(messageElement);
});

async function sendMessage(message) {
  const response = await fetch(`/message?text=${encodeURIComponent(message)}`);
  return await response.text();
}
