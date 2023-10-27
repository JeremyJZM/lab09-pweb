#!"C:/xampp/perl/bin/perl.exe"
use strict;
use warnings;
use CGI;
my $cgi = CGI->new;

print $cgi->header("text/html");

my $pantalla = $cgi->param("screen");