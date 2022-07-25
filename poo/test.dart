abstract class Vehiculo {
  late String _tipo;
  late int _anio;
  late String _combustible;
  late double _velocidad;

  void moverse();
}

class Carro implements Vehiculo {
  @override
  int _anio;

  @override
  String _combustible;

  @override
  String _tipo;

  @override
  double _velocidad;

  Carro(this._tipo, this._anio, this._combustible, this._velocidad);

  @override
  void moverse() {
    print('Este vehiculo se mueve a $_velocidad');
  }
}

class Nave implements Vehiculo {
  @override
  int _anio;

  @override
  String _combustible;

  @override
  String _tipo;

  @override
  double _velocidad;

  Nave(this._tipo, this._anio, this._combustible, this._velocidad);

  @override
  void moverse() {
    print('Este vehiculo se mueve a $_velocidad');
  }
}

class Main {
  void run() {
    Carro carro = new Carro('terrestre', 2018, 'Gasolina', 85);
    moverVehiculo(carro);
    Nave nave = new Nave('valodor', 2010, 'Oxigenor Liquido', 2000);
    moverVehiculo(nave);
  }

  void moverVehiculo(Vehiculo vehiculo) {
    vehiculo.moverse();
  }
}

void main(List<String> args) {
  Main().run();
}
