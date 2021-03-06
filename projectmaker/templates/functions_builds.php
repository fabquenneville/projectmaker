<?php
function build_top($options = []){
    /*
    The function builds the top of the page

    Args:
        $options    :	An array of function options

    Returns:
        $output     :   The build module
    */
    $options = array_replace([
        'page'              =>  'index',
        'lang'              =>  'en'
    ], $options);
    
    $output = '';
    $strings = [
        'fr' => [
            'title' => 'Bonjour projectname!',
        ],
        'en' => [
            'title' => 'Hello projectname!',
        ]
    ];
    
    $output .= "
    <!DOCTYPE html>
    <html lang='$options[lang]'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link href='./Font-Awesome/css/all.css' rel='stylesheet'>";
    
    # Assembling JS server side
    $output .= '<script>';
    $output .= file_get_contents( '../library/javascript/default.js');
    $output .= '</script>';    

    # Assembling CSS server side
    $output .= '<!-- css --> <style>';
    $output .= file_get_contents( '../library/css/default.css');
    $output .= '</style>';

    $title = $strings[$options['lang']]['title'];
    $output .= "
        <!-- favicons -->
        <link rel='apple-touch-icon' sizes='180x180' href='./img/favicon_io/apple-touch-icon.png'>
        <link rel='icon' type='image/png' sizes='32x32' href='./img/favicon_io/favicon-32x32.png'>
        <link rel='icon' type='image/png' sizes='16x16' href='./img/favicon_io/favicon-16x16.png'>
        <link rel='manifest' href='./img/favicon_io/site.webmanifest'>

        <title>$title</title>
        </head><body>
        <header>
            <h1 class='hide_me'>$title</h1>
            <div>
                <nav>
                    <a href='./'><i class='fas fa-home'></i> Home</a>
                </nav>
            </div>
        </header>
    <main>";
    return $output;
}

function build_end($options = []){
    /*
    The function builds the end of the page

    Args:
        $options    :	An array of function options

    Returns:
        $output     :	The built page
    */
    $options = array_replace([
        'page'          =>  'index',
        'lang'          =>  'en'
    ], $options);

    $output = '';
    $strings = [
        'fr' => [
            'name' => 'projectowner',
        ],
        'en' => [
            'name' => 'projectowner',
        ]
    ];

    $name = $strings[$options['lang']]['name'];
    $date = date('Y');
    $output .= "
        </main>
        <footer>
            <span id='copyright_footer'>projectname by $name - ?? $date</span>
        </footer>
    </body>
    </html>";
    return $output;
}

?>