#!"C:/xampp/perl/bin/perl.exe"
use strict;
use warnings;
use CGI;
my $cgi = CGI->new;

print $cgi->header("text/html");

my $pantalla = $cgi->param("screen");

my $opcion= $cgi->param("op");

my $screen;
my $resultado;
my @operadores = (
    "(",
    ")",
    "%",
    "AC",
    "7",
    "8",
    "9",
    "/",
    "4",
    "5",
    "6",
    "*",
    "1",
    "2",
    "3",
    "-",
    "0",
    ".",
    "=",
    "+"
);
my $operador= $operadores[$opcion - 1];

if ($opcion =~ /^\d+$/ && $opcion >= 1 && $opcion <= @operadores) {
    my $operador = $operadores[$opcion - 1];

    if ($operador eq "=") {
        if ($pantalla) {
            my $resultado = eval $pantalla;
            if (defined $resultado) {
                $pantalla = $resultado;
            } else {
                $pantalla = "Error";
            }
        }
    } elsif ($operador eq "AC") {
        $pantalla = "";
    } else {
        if ($pantalla eq "Error" || $pantalla eq "") {
            $pantalla = $operador;
        } else {
            $pantalla .= $operador;
        }
    }
}

print <<HTML;
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Calculadora PW1</title>
<style>
body{
    min-height: 100vh;
    background-color:purple;
    display: grid;
    place-items: center;
}
.calculadora{
    background-color: white;
    color: black;
    display: grid;
    gap: 0.4rem;
    width: 350px;
    max-width: 100%;
    padding: 2rem;
    border-radius: 1rem;
}
.pantalla{
    border: black solid .6px;
    padding-top: 1rem;
    padding-right: 1rem;
    text-align: right;
    font-size: 2rem;
    border-radius: .5rem;
}
.botones {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr; 
    grid-gap: 5px; 
    justify-items: center; 
}
.boton{
    all: initial;
    padding: .75rem;
    border-radius: 1rem;
    border: solid 0.7px;
    display: flex;
    justify-content: center;
    cursor: pointer;
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-size: 23px;
    background-color: rgb(230, 230, 255);
    transition: 0.2s;
}
.boton.negro {  
    background-color: rgb(184, 184, 230);
    transition: 0.2s;
}
.boton.azul {
    background-color: rgb(110, 110, 255);
    transition: 0.2s;
}    
.no-mostrar{
    display: none;
}
</style>
</head>
 <body>
        <div class="calculadora">
            <div class="pantalla">
                $pantalla
            </div>

            <div class="botones">

                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">
                    <input type="text" name="op" value="1" class="no-mostrar" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="(" class="boton negro">
                </form>

                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">

                    <input type="text" name="op" value="2" class="no-mostrar" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value=")" class= "boton negro">

                </form>

                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">
                    <input type="text" name="op" value="3" class="no-mostrar" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="%" class="boton negro">
                </form>

                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">
                    <input class = "no-mostrar" type="text" name="op" value="4" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="AC" class="boton negro">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">
                    <input class = "no-mostrar" type="text" name="op" value="5" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="7" class="boton">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">
                    <input class = "no-mostrar" type="text" name="op" value="6" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="8" class="boton">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">
                    <input class = "no-mostrar" type="text" name="op" value="7" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="9" class="boton">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">
                    <input class = "no-mostrar" type="text" name="op" value="8" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="/" class="boton negro">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">

                    <input class = "no-mostrar" type="text" name="op" value="9" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="4" class="boton">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">

                    <input class = "no-mostrar" type="text" name="op" value="10" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="5" class="boton">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">

                    <input class = "no-mostrar" type="text" name="op" value="11" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="6" class="boton">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">
                    
                    <input class = "no-mostrar" type="text" name="op" value="12" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="x" class="boton negro">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">

                    <input class = "no-mostrar" type="text" name="op" value="13" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="1" class="boton">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">

                    <input class = "no-mostrar" type="text" name="op" value="14" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="2" class="boton">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">

                    <input class = "no-mostrar" type="text" name="op" value="15" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                  
                    <input type="submit" value="3" class="boton">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">

                    <input class = "no-mostrar" type="text" name="op" value="16" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="-" class="boton negro">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">

                    <input class = "no-mostrar" type="text" name="op" value="17" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="0" class="boton negro">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">

                    <input class = "no-mostrar" type="text" name="op" value="18" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="." class="boton negro">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">

                    <input class = "no-mostrar" type="text" name="op" value="19" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="=" class="boton azul">
                </form>
                <form class="no-mostrar-formulario" action="/cgi-bin/script.cgi" method="get">

                    <input class = "no-mostrar" type="text" name="op" value="20" readonly="">
                    <input type="text" name="screen" value="$pantalla" class="no-mostrar" readonly="">

                    <input type="submit" value="+" class="boton negro">
                </form>

            </div>
        </div>

    </body>
</html>