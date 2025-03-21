$(document).ready(function() {
    const messageInput = $('#messageInput');
    const sendMessageBtn = $('#sendMessageBtn');
    const messagesBox = $('#messagesBox');

    // Function to send message
    function sendMessage() {
        const message = messageInput.val();
        if (message.trim()) {
            // Send the message via an API call (AJAX or Django Channels)
            $.ajax({
                url: '/chat/send/',  // Adjust this URL based on your API endpoint
                type: 'POST',
                data: { message: message },
                success: function(response) {
                    // Display the message
                    messagesBox.append('<div class="message-item">' + response.message + '</div>');
                    messageInput.val('');  // Clear the input field
                },
                error: function(error) {
                    console.log("Error sending message: ", error);
                }
            });
        }
    }

    // Attach the send message function to the button
    sendMessageBtn.click(function() {
        sendMessage();
    });

    // Allow pressing Enter to send the message
    messageInput.keyup(function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});
