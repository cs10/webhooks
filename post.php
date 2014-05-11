<html>
<body>

Welcome <?php echo $_POST["name"]; ?><br>
<?php 
foreach ($_POST as $key => $value)
	echo "Field ".htmlspecialchars($key)." is ".htmlspecialchars($value)."<br>";
?>

</body>
</html>
