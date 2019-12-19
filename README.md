# *ROTate* <img src="rotate.png" alt="ROTate logo" height="128px" width="128px" align="right"/>

**Table of contents**

*   [Definition](#definition)
*   [Details](#details)
*   [Components](#components)
*   [Requirements](#requirements)
*   [Documentation](#documentation)
*   [Contact](#contact)
*   [Useless facts](#useless-facts)

----

## Definition

The *ROTate* project is a collection of scripts to encrypt and decrypt files using various *ROT* cipher methods.

[Top](#rotate)

## Details

The project allows to encrypt and decrypt files using various ROT cipher methods such as *ROT13*, *ROT47*, *ROT128* as well as with enhanced variants based on each character set of these methods.

It also comes with a tool to find out which variant and value has been used to encrypt a file.

Due to the fact, that data encrypted with *ROT* methods can be cracked quite easily, they are **not** suitable for encrypting sensible data.

[Top](#rotate)

## Components

### *ROTate* variants

There are three components to encrypt and decrypt files using the *ROT13*, *ROT47* and *ROT128* cipher method.

They also allow using a user-defined rotation value (based on the character set of that cipher method) instead of the default rotation value.

### *ROTate Cracker*

As already mentioned above, data encrypted with *ROT* methods can be cracked quite easily. This brute force cracker helps to determine which *ROT* variant and rotation value has been used to encrypt a file or string by simply trying all supported variants with all rotation values available.

[Top](#rotate)

## Requirements

In order to use *ROTate*, the *Python* framework must be installed on the system.

Depending on which version of the framework you are using:

*   *Python* 2.x (version 2.7 or higher is recommended, may also work with earlier versions)
*   *Python* 3.x (version 3.2 or higher is recommended, may also work with earlier versions)

[Top](#rotate)

## Documentation

In the corresponding `docs` sub-directories, there are plain text files containing a detailed documentation for each component with further information and usage examples.

[Top](#rotate)

## Contact

Any suggestions, questions, bugs to report or feedback to give?

You can contact me by sending an email to [dev@urbanware.org](mailto:dev@urbanware.org).

Further information can be found inside the `contact.txt` file.

[Top](#rotate)

## Useless facts

*   The name *ROTate* stands for ***ROT*** *with* ***A**dditional* ***T**ools* *and* ***E**nhancements*.
*   The first version uploaded on *GitHub* was *ROTate* 3.0.6 built on March 13<sup>th</sup>, 2018.
*   Before uploading, the project has neither been changed nor even touched for more than three years.

[Top](#rotate)
