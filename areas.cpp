#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int opcion;
    
    cout << "Seleccione la figura para calcular su �rea:" << endl;
    cout << "1. Tri�ngulo" << endl;
    cout << "2. C�rculo" << endl;
    cout << "3. Rect�ngulo" << endl;
    cout << "4. Cuadrada" << endl;

    cin >> opcion;

    switch (opcion) {
        case 1: {
            
            double baseTriangulo, alturaTriangulo;
            cout << "Ingrese la base del tri�ngulo: ";
            cin >> baseTriangulo;
            cout << "Ingrese la altura del tri�ngulo: ";
            cin >> alturaTriangulo;
            double areaTriangulo = (baseTriangulo * alturaTriangulo) / 2;
            cout << "El �rea del tri�ngulo es: " << areaTriangulo << endl;
            break;
        }
        case 2: {
            
            double radioCirculo;
            cout << "Ingrese el radio del c�rculo: ";
            cin >> radioCirculo;
            double areaCirculo = M_PI * pow(radioCirculo, 2);
            cout << "El �rea del c�rculo es: " << areaCirculo << endl;
            break;
        }
        case 3: {
            
            double baseRectangulo, alturaRectangulo;
            cout << "Ingrese la base del rect�ngulo: ";
            cin >> baseRectangulo;
            cout << "Ingrese la altura del rect�ngulo: ";
            cin >> alturaRectangulo;
            double areaRectangulo = baseRectangulo * alturaRectangulo;
            cout << "El �rea del rect�ngulo es: " << areaRectangulo << endl;
            break;
        }
        case 4: {
           
            double ladoCuadrada;
            cout << "Ingrese el lado de la cuadrada: ";
            cin >> ladoCuadrada;
            double areaCuadrada = pow(ladoCuadrada, 2);
            cout << "El �rea de la cuadrada es: " << areaCuadrada << endl;
            break;
        }
        default:
            cout << "Opci�n no v�lida." << endl;
            break;
    }

    return 0;
}
