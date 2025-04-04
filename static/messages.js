let input_message = $('#input-message');
let send_message_form = $('#send-message-form');
const USER_ID = $('#logged-in-user').val();

let loc = window.location;
let wsStart = 'ws://';

if (loc.protocol === 'https') {
    wsStart = 'wss://';
}

let endpoint = wsStart + loc.host + loc.pathname;
var socket = new WebSocket(endpoint);

socket.onopen = function (e) {
    console.log('Socket opened', e);
    send_message_form.on('submit', function (e) {
        e.preventDefault();
        let message = input_message.val();
        let send_to = get_active_other_user_id();
        let thread_id = get_active_thread_id();

        let data = {
            'message': message,
            'sent_by': USER_ID,
            'send_to': send_to,
            'thread_id': thread_id
        };
        data = JSON.stringify(data);
        socket.send(data);
        $(this)[0].reset();
    });
};

socket.onmessage = function (e) {
    console.log('Message received:', e);
    let data = JSON.parse(e.data);
    let message = data['message'];
    let sent_by_id = data['sent_by'];
    let thread_id = data['thread_id'];

    newMessage(message, sent_by_id, thread_id);
};

socket.onerror = function (e) {
    console.log('Socket error', e);
};

socket.onclose = function (e) {
    console.log('Socket closed', e);
};

function newMessage(message, sent_by_id, thread_id) {
    if ($.trim(message) === '') {
        return false;
    }

    // Find the correct chat_id to append the message
    let chat_id = 'chat_' + thread_id;
    let message_element;

    // Format the message depending on who sent it
    if (sent_by_id == USER_ID) {
        message_element = `
            <div class="d-flex mb-4 replied">
                <div class="msg_cotainer_send">
                    ${message}
                    <span class="msg_time_send">8:55 AM, Today</span>
                </div>
                <div class="img_cont_msg">
                    <img>
                </div>
            </div>
        `;
    } else {
        message_element = `
            <div class="d-flex mb-4 received">
                <div class="img_cont_msg">
                    <img src="https://via.placeholder.com/50" class="rounded-circle user_img_msg">
                </div>
                <div class="msg_cotainer">
                    ${message}
                    <span class="msg_time">8:40 AM, Today</span>
                </div>
            </div>
        `;
    }

    // Append the message to the correct message body of the active chat window
    let message_body = $(`.messages-wrapper[chat_structure-id="${chat_id}"] .msg_card_body`);
    if (message_body.length > 0) {
        message_body.append($(message_element));
        message_body.animate({
            scrollTop: message_body[0].scrollHeight
        }, 100);
    } else {
        console.error('Message body not found for chat_id:', chat_id);
    }

    input_message.val(null);
}

$('.contact-li').on('click', function () {
    $('.contacts .active').removeClass('active');
    $(this).addClass('active');

    // message wrappers
    let chat_id = $(this).attr('chat_structure-id');
    $('.messages-wrapper.is_active').removeClass('is_active');
    $(`.messages-wrapper[chat_structure-id="${chat_id}"]`).addClass('is_active');
});

function get_active_other_user_id() {
    let other_user_id = $('.messages-wrapper.is_active').attr('other-user-id');
    return $.trim(other_user_id);
}

function get_active_thread_id() {
    let chat_id = $('.messages-wrapper.is_active').attr('chat_structure-id');
    return chat_id.replace('chat_', '');
}

$(document).ready(function () {
    console.log("Search bar script loaded");
    $('#contacts-list').hide();

    // Search functionality for contacts
    $('#search-input').on('input', function () {
        var searchText = $(this).val().toLowerCase();

        if (searchText.trim() === '') {
            $('#contacts-list').show(); // Show all contacts if search is cleared
            return;
        }

        $('#contacts-list').show(); // Show when searching

        $('#contacts-list li').each(function () {
            var contactName = $(this).find('.user_info span').text().toLowerCase();

            if (contactName.includes(searchText)) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });

    // Simulating switching between chats
    $('#contacts-list li').on('click', function () {
        var chatId = "chat_" + $(this).data('user-id');
        $('.messages-wrapper').removeClass('is_active').addClass('hide');
        $("#" + chatId).removeClass('hide').addClass('is_active');
    });
});
