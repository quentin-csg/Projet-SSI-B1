<?php
setcookie ("PHPSESSID", "", time() - 3600, '/');
session_start();
$conn = mysqli_connect("localhost", "quentin", "quentin", "db-web");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

if(isset($_COOKIE['user_cookie'])) {
    $encoded_username = $_COOKIE['user_cookie'];
    $decoded_username = base64_decode($encoded_username);
    $username = str_replace("v4er9esdfve", "", $decoded_username);
    $query = "SELECT * FROM users WHERE username = '$username'";
    $result = mysqli_query($conn, $query);

    if (mysqli_num_rows($result) == true) {
        $row = mysqli_fetch_assoc($result);
        $user_id = $row['id'];
        $password = $row['password'];

    }
}
if(isset($_GET['logout'])) {
    setcookie("user_cookie", "", time() - 3600, "/");
    header("Location: login.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Information</title>
    <link rel="stylesheet" href="style2.css">
    <script>
        function showCookies() {
            var cookies = document.cookie;
            var cookieContainer = document.getElementById("cookie-container");
            cookieContainer.innerHTML = "User Cookie : " + cookies;
        }
    </script>
</head>
<body>
    <h1>User Information</h1>
    <p>Id : <?php echo $user_id; ?></p>
    <p>Username : <?php echo $username; ?></p>
    <p>Password hash : <?php echo $password; ?></p>
    <button onclick="showCookies()">Show cookies</button>
    <div id="cookie-container"></div>
    <a href="?logout=true">Logout</a>
</body>
</html>