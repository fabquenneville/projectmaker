<?php

class projectname {

    private $id;
    private $name;

    function __construct($options = []){
        /* 
    
        Args:
            $options        :	An array of function options
            
        Returns:
        */
        $options = array_replace([
            'id'        => null,
            'name'      => null,
        ], $options);

        $this->id       = null;
        $this->name     = null;

        if ($options['id'])     $this->id   = $options['id'];
        if ($options['name'])   $this->name = $options['name'];
    }

    public function __toString() {
        /* Return the default string representation of the object
    
        Args:
    
        Returns:
            string	:	The object's string representation
        */
        return $this->name;
    }
}
?>