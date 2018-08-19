%
%Name: Hugo David Franco Avila
%Name: Jose Carlos Pacheco Sanchez
%Date: 19 - 08 - 18
%
%This program will calculate the electric force in an array of charges,
%and th eelectric field
%
%

clc
clear all
disp('Este script encontrara la fuerza electrica o el campo electrico')

%while repetir == 'y'
    numCargas = input('Cuantas cargas hay en su sistema?\n');
    disp('Desea encontrar la fuerza electrica sobre una carga o el campo electrico en un punto?')
    disp('1. Fuerza electrica')
    disp('2. Campo electrico')
    opcion = input('');
    if opcion == 1
        if numCargas < 2
            %break
        end
        qRef = input('Ingrese la magnitud de la carga sobre la que se ejerce la fuerza en micro Coulombs\n');
        qRef = qRef * 10e-6;
        qRefx = input('Ingresa el componente x de su vector de direccion\n');
        qRefy = input('Ingresa el componente y de su vector de direccion\n');
        qRefz = input('Ingresa el componente z de su vector de direccion\n');
    elseif opcion == 2
        if numCargas < 1
            %break
        end
        qRef = 1;
        qRefx = input('Ingresa el componente x del punto de referencia\n');
        qRefy = input('Ingresa el componente y del punto de referencia\n');
        qRefz = input('Ingresa el componente z del punto de referencia\n');
    else 
        disp('La opcion ingresada no es correcta')
        %break
    end
    arregloCargas = [qRef qRefx qRefy qRefz; zeros(numCargas - 1, 4)];
    %for x = 1:1:numCargas
        %qMag = ('Ingrese la magnitud de la carga ' + x+1 + ' en micro Coulombs\n');
        %qMag = qMag * 10e-6;
        %qx = input('Ingresa el componente x de su vector de direccion\n');
        %qy = input('Ingresa el componente y de su vector de direccion\n');
        %qz = input('Ingresa el componente z de su vector de direccion\n');
       % vecSec = [qMag qx qy qz];
        %arregloCargas = [arregloCargas;vecSec];
    %end   
%end
    
