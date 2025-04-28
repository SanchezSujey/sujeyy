#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int opcion;
    
    cout << "Seleccione la figura para calcular su área:" << endl;
    cout << "1. Triángulo" << endl;
    cout << "2. Círculo" << endl;
    cout << "3. Rectángulo" << endl;
    cout << "4. Cuadrada" << endl;

    cin >> opcion;

    switch (opcion) {
        case 1: {
            
            double baseTriangulo, alturaTriangulo;
            cout << "Ingrese la base del triángulo: ";
            cin >> baseTriangulo;
            cout << "Ingrese la altura del triángulo: ";
            cin >> alturaTriangulo;
            double areaTriangulo = (baseTriangulo * alturaTriangulo) / 2;
            cout << "El área del triángulo es: " << areaTriangulo << endl;
            break;
        }
        case 2: {
            
            double radioCirculo;
            cout << "Ingrese el radio del círculo: ";
            cin >> radioCirculo;
            double areaCirculo = M_PI * pow(radioCirculo, 2);
            cout << "El área del círculo es: " << areaCirculo << endl;
            break;
        }
        case 3: {
            
            double baseRectangulo, alturaRectangulo;
            cout << "Ingrese la base del rectángulo: ";
            cin >> baseRectangulo;
            cout << "Ingrese la altura del rectángulo: ";
            cin >> alturaRectangulo;
            double areaRectangulo = baseRectangulo * alturaRectangulo;
            cout << "El área del rectángulo es: " << areaRectangulo << endl;
            break;
        }
        case 4: {
           
            double ladoCuadrada;
            cout << "Ingrese el lado de la cuadrada: ";
            cin >> ladoCuadrada;
            double areaCuadrada = pow(ladoCuadrada, 2);
            cout << "El área de la cuadrada es: " << areaCuadrada << endl;
            break;
        }
        default:
            cout << "Opción no válida." << endl;
            break;
    }

    return 0;
}
