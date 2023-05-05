<?php
setcookie ("PHPSESSID", "", time() - 3600, '/');
session_start();
$conn = mysqli_connect("localhost", "quentin", "quentin", "db-web");

if (isset($_POST['username']) && isset($_POST['password'])) {
    $username =$_POST['username'];
    $pass=$_POST['password'];
    $password = hash('sha256', $pass);
    $select="SELECT * FROM users WHERE username = '$username'";
    $result = mysqli_query($conn, $select);
    if(mysqli_num_rows($result)>0){
        $error[]='user already exists!';
            }else{
                $insert="INSERT INTO users(username,password) VALUES('$username','$password')";
                mysqli_query($conn,$insert);
                header('location:login.php');
    }
};

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>register form</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="form-container">

    <form action="" method="post">
        <h3>register now</h3>
        <?php
        if(isset($error)) {
            foreach($error as $error){
                echo'<span class="error-msg">'.$error.'</span>';
            };
        };

        ?>
        <input type="text" name="username" required placeholder="enter your username">
        <input type="password" name="password" required placeholder="enter your password">
        <input type="submit" name="submit" value="register now" class="form-btn">
        <p> already have an account? <a href="login.php">login now</a></p>
    </form>
</div>


</body>
</html>