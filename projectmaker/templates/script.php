<?php
/********************************************************************/
/*                   common to all scripts                          */
/********************************************************************/
session_start();
$cwd = dirname(__FILE__);

//Get external stuff
require $cwd."/library/php/functions.php";

// set environment variables
$script 	= basename(__FILE__, '.php');
$output = "";

/********************************************************************/
/*                   special to $script                             */
/********************************************************************/

/********************************************************************/
/*                        output                                    */
/********************************************************************/
$output .= "Hello World!";

echo($output);
?>
