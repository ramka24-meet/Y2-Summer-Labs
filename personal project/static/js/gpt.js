function loadChat(conversationId) {
    // Send the selected conversation ID to the server
    console.log(conversationId)
    fetch('/set_conversation_id', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content')
        },
        body: JSON.stringify({ conversationId: conversationId })
    })
    .then(response => response.json())
    .then(data => {
        // Reload the page to show the selected chat
        window.location.reload();
    })
    .catch(error => console.error('Error:', error));
}
