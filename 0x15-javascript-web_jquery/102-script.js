//  script that fetches and prints how to say “Hello” depending on the language
$(document).ready(function() {
    $('#btn_translate').click(function() {
        const langCode = $('#language_code').val();
        const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

        $.get(url, function(data) {
            $('#hello').text(data.hello);
        });
    });
});

