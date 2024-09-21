import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class Sudoku {

    // Clase para representar una celda del tablero
    public static class Celda {
        private int valor;

        public Celda() {
            this.valor = 0;
        }

        public int getValor() {
            return valor;
        }

        public void setValor(int valor) {
            this.valor = valor;
        }

        @Override
        public String toString() {
            return valor == 0 ? " . " : String.format(" %d ", valor);
        }
    }

    // Clase para representar el tablero de Sudoku
    public static class Tablero {
        private Celda[][] celdas;

        public Tablero() {
            celdas = new Celda[9][9];
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    celdas[i][j] = new Celda();
                }
            }
        }

        public Celda getCelda(int fila, int columna) {
            return celdas[fila][columna];
        }

        public void mostrar() {
            System.out.println("    1 2 3 | 4 5 6 | 7 8 9");
            System.out.println("  -----------------------");
            for (int i = 0; i < 9; i++) {
                System.out.print((i + 1) + " "); // Etiqueta de fila
                for (int j = 0; j < 9; j++) {
                    if (j % 3 == 0 && j != 0) {
                        System.out.print("|");
                    }
                    System.out.print(celdas[i][j]);
                }
                System.out.println();
                if ((i + 1) % 3 == 0 && i != 8) {
                    System.out.println("  -----------------------");
                }
            }
        }

        public void inicializarConNumerosAleatorios(int cantidad) {
            Random rand = new Random();
            int count = 0;
            while (count < cantidad) {
                int fila = rand.nextInt(9);
                int columna = rand.nextInt(9);
                int valor = rand.nextInt(9) + 1; // Números entre 1 y 9

                if (getCelda(fila, columna).getValor() == 0 && esValorValido(fila, columna, valor)) {
                    getCelda(fila, columna).setValor(valor);
                    count++;
                }
            }
        }

        public boolean esValorValido(int fila, int columna, int valor) {
            // Verificar fila
            for (int i = 0; i < 9; i++) {
                if (celdas[fila][i].getValor() == valor) {
                    return false;
                }
            }

            // Verificar columna
            for (int i = 0; i < 9; i++) {
                if (celdas[i][columna].getValor() == valor) {
                    return false;
                }
            }

            // Verificar subcuadro 3x3 
            int inicioFila = (fila / 3) * 3;
            int inicioColumna = (columna / 3) * 3;
            for (int i = inicioFila; i < inicioFila + 3; i++) {
                for (int j = inicioColumna; j < inicioColumna + 3; j++) {
                    if (celdas[i][j].getValor() == valor) {
                        return false;
                    }
                }
            }

            return true;
        }

        // Método para verificar si una fila está completa
        public boolean filaCompleta(int fila) {
            for (int i = 0; i < 9; i++) {
                if (celdas[fila][i].getValor() == 0) {
                    return false;
                }
            }
            return true;
        }

        // Método para verificar si una columna está completa
        public boolean columnaCompleta(int columna) {
            for (int i = 0; i < 9; i++) {
                if (celdas[i][columna].getValor() == 0) {
                    return false;
                }
            }
            return true;
        }

        // Método para verificar si un subcuadro 3x3 está completo
        public boolean subCuadroCompleto(int fila, int columna) {
            int inicioFila = (fila / 3) * 3;
            int inicioColumna = (columna / 3) * 3;
            for (int i = inicioFila; i < inicioFila + 3; i++) {
                for (int j = inicioColumna; j < inicioColumna + 3; j++) {
                    if (celdas[i][j].getValor() == 0) {
                        return false;
                    }
                }
            }
            return true;
        }
    }

    private Tablero tablero;
    private Scanner scanner;

    public Sudoku() {
        tablero = new Tablero();
        scanner = new Scanner(System.in);
    }

    public boolean agregarValor(int fila, int columna, int valor) {
        if (valor < 1 || valor > 9) {
            System.out.println("El valor debe estar entre 1 y 9.");
            return false;
        }

        // Si ya hay un valor en la celda, preguntar si desea sobrescribir
        Celda celda = tablero.getCelda(fila, columna);
        if (celda.getValor() != 0) {
            System.out.println("La celda ya tiene el valor " + celda.getValor() + ". ¿Desea sobrescribirlo? (S/N)");
            String respuesta = scanner.nextLine().trim().toUpperCase();
            if (!respuesta.equals("S")) {
                System.out.println("Valor no modificado.");
                return false;
            }
        }

        if (esValorValido(fila, columna, valor)) {
            tablero.getCelda(fila, columna).setValor(valor);

            // Verificar si se ha completado una fila, columna o subcuadro
            if (tablero.filaCompleta(fila)) {
                System.out.println("¡Has completado la fila " + (fila + 1) + "!");
            }

            if (tablero.columnaCompleta(columna)) {
                System.out.println("¡Has completado la columna " + (columna + 1) + "!");
            }

            if (tablero.subCuadroCompleto(fila, columna)) {
                int inicioFila = (fila / 3) * 3 + 1;
                int inicioColumna = (columna / 3) * 3 + 1;
                System.out.println("¡Has completado el subcuadro 3x3 que comienza en la fila " 
                                   + inicioFila + ", columna " + inicioColumna + "!");
            }

            return true;
        } else {
            System.out.println("Valor no válido.");
            return false;
        }
    }

    private boolean esValorValido(int fila, int columna, int valor) {
        return tablero.esValorValido(fila, columna, valor);
    }

    public void mostrarTablero() {
        tablero.mostrar();
    }

    private void leerYAgregarValores() {
        while (true) {
            try {
                System.out.println("Introduce fila (1-9) o -1 para terminar:");
                int fila = scanner.nextInt(); // Capturar fila

                if (fila == -1) break; // Terminar el ciclo si se ingresa -1

                if (fila < 1 || fila > 9) {
                    System.out.println("Fila fuera de rango. Debe estar entre 1 y 9.");
                    scanner.nextLine(); // Limpiar el buffer
                    continue;
                }

                System.out.println("Introduce columna (1-9):");
                int columna = scanner.nextInt();

                if (columna < 1 || columna > 9) {
                    System.out.println("Columna fuera de rango. Debe estar entre 1 y 9.");
                    scanner.nextLine(); // Limpiar el buffer
                    continue;
                }

                System.out.println("Introduce valor (1-9):");
                int valor = scanner.nextInt();
                scanner.nextLine(); // Limpiar el buffer

                if (agregarValor(fila - 1, columna - 1, valor)) {
                    System.out.println("Valor agregado correctamente.");
                } else {
                    System.out.println("No se pudo agregar el valor.");
                }

                mostrarTablero();
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Por favor, introduce números enteros.");
                scanner.next(); // Limpiar el buffer
            }
        }
    }

    private void mostrarMenu() {
        System.out.println("Bienvenido al Sudoku!");
        System.out.println("1. Iniciar con el tablero vacío");
        System.out.println("2. Iniciar con números aleatorios");
        System.out.print("Elige una opción (1/2): ");
    }

    private void iniciarJuego() {
        while (true) {
            mostrarMenu();
            try {
                int opcion = scanner.nextInt();
                scanner.nextLine(); // Limpiar el buffer

                switch (opcion) {
                    case 1:
                        System.out.println("Iniciando con el tablero vacío...");
                        break;
                    case 2:
                        int cantidad = elegirCantidadNumeros();
                        System.out.println("Iniciando con " + cantidad + " números aleatorios...");
                        tablero.inicializarConNumerosAleatorios(cantidad);
                        break;
                    default:
                        System.out.println("Opción no válida. Intenta de nuevo.");
                        continue;
                }
                break; // Salir del ciclo si la opción es válida
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Debes ingresar 1 o 2.");
                scanner.next(); // Limpiar el buffer
            }
        }
        mostrarTablero();
        leerYAgregarValores();
    }

    private int elegirCantidadNumeros() {
        int cantidad = 0;
        while (cantidad < 9 || cantidad > 21) {
            try {
                System.out.print("Introduce la cantidad de números aleatorios (entre 9 y 21): ");
                cantidad = scanner.nextInt();
                scanner.nextLine(); // Limpiar el buffer

                if (cantidad < 9 || cantidad > 21) {
                    System.out.println("Cantidad no válida. Debe estar entre 9 y 21.");
                }
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Por favor, introduce un número entero.");
                scanner.next(); // Limpiar el buffer
            }
        }
        return cantidad;
    }

    public static void main(String[] args) {
        Sudoku sudoku = new Sudoku();
        sudoku.iniciarJuego();
    }
}
