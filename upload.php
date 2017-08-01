<?php 
$a = $_POST['rep'];
$b = $_POST['blocksize'];
$c = $_POST['locations'];
if(isset($_POST['submit'])) {
// start uploading if user submit
  if(!empty($_FILES['file']['name'])) {
  
       if ($_FILES["file"]["error"] > 0) {
       
            echo "Error: " . $_FILES["file"]["error"] . "<br />";
            
         }
        else {
        
         echo "Upload: " . $_FILES["file"]["name"] . "<br />";
         
         echo "Type: " . $_FILES["file"]["type"] . "<br />";
         
         echo "Size: " . ($_FILES["file"]["size"] / 1024) . " Kb<br />";
         
         move_uploaded_file($_FILES["file"]["tmp_name"],"/var/www/html/upload/" . $_FILES["file"]["name"]);
	$ss='/var/www/html/upload/'.$_FILES["file"]["name"];
        echo $ss;
	echo "FILE UPLOADED";
	$myfile = fopen("works.txt", "w");
	fwrite($myfile, $ss);
	fwrite($myfile, "\n");
	fwrite($myfile, $a);
	fwrite($myfile, "\n");
	fwrite($myfile, $b);
	fwrite($myfile, "\n");
	fwrite($myfile, $c);

	fclose($myfile);

	echo "done";
        header("Location:/cgi-bin/upload.py");
         
       }
 }
     
     
   else {
         echo 'plz select file'; //input filed empty return this error message;
   }
}
?>
