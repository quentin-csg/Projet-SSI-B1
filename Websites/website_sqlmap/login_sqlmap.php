<?php
$conn = mysqli_connect("localhost", "quentin", "quentin", "nom-user-db");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $pass = $_POST['password'];
    $query = "SELECT * FROM users WHERE username = '$username' AND password = '$pass'";
    $result = mysqli_query($conn, $query);


    if (mysqli_num_rows($result) == true) {
        header('Location: userpage_sqlmap.php');
        exit;
    } else {
        $error_message = "Nom d'utilisateur ou mot de passe incorrect";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
        <title>Formulaire de connexion</title>
</head>
<body>
        <h2>Connexion</h2>
        <form action="" method="post">
            <h3>Login</h3>
            <?php
            if (isset($error_message)) {
            echo "<p style='color:red;'>$error_message</p>";
            }
            ?>
            <label for="username">Nom d'utilisateur :</label>
            <input type="text" id="username" name="username" required><br><br>
            <label for="password">Mot de passe :</label>
            <input type="password" id="password" name="password" required><br><br>
            <input type="submit" value="Connexion">
        </form>
</body>
</html>

<?php
mysqli_close($conn);
?>