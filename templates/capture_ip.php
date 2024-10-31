<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $ip = $_SERVER['REMOTE_ADDR'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $acceptPolicy = isset($_POST['accept-policy']) ? 'Sí' : 'No';
    $subscribe = isset($_POST['subscribe']) ? 'Sí' : 'No';

    $data = [
        'email' => $email,
        'password' => $password,
        'ip' => $ip,
        'accept_policy' => $acceptPolicy,
        'subscribe' => $subscribe,
    ];

    $json_data = json_encode($data, JSON_PRETTY_PRINT);

    // Guardar los datos en un archivo JSON
    file_put_contents('users.json', $json_data, FILE_APPEND);

    echo "Datos guardados correctamente.";
}
?>
