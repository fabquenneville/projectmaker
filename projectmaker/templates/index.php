<?php
/********************************************************************/
/*                   common to all public pages                     */
/********************************************************************/
session_start();

//Get external stuff
require "../library/php/functions.php";
require "../library/php/functions_builds.php";

// set environment variables
$page 	= basename(__FILE__, '.php');
$output = "";
$lang = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'], 0, 2);
$acceptLang = ['fr', 'en']; 
$lang = in_array($lang, $acceptLang) ? $lang : 'en';

/********************************************************************/
/*                   special to $page                               */
/********************************************************************/

/********************************************************************/
/*                        output
/********************************************************************/

$output .= build_top([
    "page" 				=> 	$page,
    "lang" 				=> 	$lang,
]);

$output .= "
<section>
    <p>Hello projectname</p>
</section>
";

$output .= build_end([
    "page" 				=> 	$page,
    "lang" 				=> 	$lang,
]);

echo($output);
?>

