document.addEventListener('DOMContentLoaded', function () {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/ajax/example/');
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.onload = function () {
        if (xhr.status === 200) {
            var data = JSON.parse(xhr.responseText);
            console.log(data.message); // Обработка полученных данных
        }
    };
    xhr.send();
});
