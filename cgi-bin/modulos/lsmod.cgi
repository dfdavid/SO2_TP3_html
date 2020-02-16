#!/usr/bin/env perl

use CGI;
use Cwd;
my $consulta = CGI->new;

print $consulta->header( -charset=>'utf-8'), $consulta->start_html( -title=>'lsmod', -style=>{-src=>'style.css'}),$consulta->end_html;
#mensaje de cabecera de la pagina donde me va a mostrar el resultado
print $consulta->h2("LISTA DE MODULOS INSTALADOS");
#ejecuto lsmod en consola con qx
my $ls_mod = qx(lsmod); 
my @lines= split /\n/, $ls_mod; #arreglo que luego imprimo con el foreach
foreach my $line(@lines){
  print $consulta->b("$line <br>");
}
