<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>Document</title>
</head>

<body>
    <div class="container">
        <div class="row justify-content-md-center">
            <div class="col-sm-6">
                <div class="card bg-light m-5" style="max-width: 33rem;">
                    <div class="card-header" style="justify-content: center; display: flex;">
                        <h1>Resultados</h1>
                    </div>
                    <div class="card-body">
                        <fieldset>
                            <div class="row" style="margin-top: 10px;">
                                <div class="col-sm-4">
                                    <label for="folio">Folio:</label>
                                </div>
                                <div class="col-sm">
                                    <input type="text" id="folio" class="form-control" value="{{ $constancia->folio }}" readonly>
                                </div>
                            </div>
                            <div class="row" style="margin-top: 10px;">
                                <div class="col-sm-4">
                                    <label for="rfc">RFC:</label>
                                </div>
                                <div class="col-sm">
                                    <input type="text" id="rfc" class="form-control" value="{{ $constancia->rfc }}" readonly>
                                </div>
                            </div>
                            <div class="row" style="margin-top: 10px;">
                                <div class="col-sm-4">
                                    <label for="curp">CURP:</label>
                                </div>
                                <div class="col-sm">
                                    <input type="text" id="curp" class="form-control" value="{{ $constancia->curp }}" readonly>
                                </div>
                            </div>
                            <div class="row" style="margin-top: 10px;">
                                <div class="col-sm-4">
                                    <label for="nombre">Nombre:</label>
                                </div>
                                <div class="col-sm">
                                    <input type="text" id="nombre" class="form-control" value="{{ $constancia->nombre }}" readonly>
                                </div>
                            </div>
                            <div class="row" style="margin-top: 10px;">
                                <div class="col-sm-4">
                                    <label for="apellidos">Apellidos:</label>
                                </div>
                                <div class="col-sm">
                                    <input type="text" id="apellidos" class="form-control" value="{{ $constancia->apellidos }}" readonly>
                                </div>
                            </div>
                            <div class="row" style="margin-top: 10px;">
                                <div class="col-sm-4">
                                    <label for="expedicion">Expedición:</label>
                                </div>
                                <div class="col-sm">
                                    <input type="text" id="expedicion" class="form-control" value="{{ $constancia->expedicion }}" readonly>
                                </div>
                            </div>
                            <div class="row" style="margin-top: 10px;">
                                <div class="col-sm-4">
                                    <label for="vencimiento">Vencimiento:</label>
                                </div>
                                <div class="col-sm">
                                    <input type="text" id="vencimiento" class="form-control" value="{{ $constancia->vencimiento }}" readonly>
                                </div>
                            </div>
                            <div class="row" style="margin-top: 10px;">
                                <div class="col-sm-4">
                                    <label for="duracion">Duración:</label>
                                </div>
                                <div class="col-sm">
                                    <input type="text" id="duracion" class="form-control" value="{{ $constancia->duracion }} Horas" readonly>
                                </div>
                            </div>
                            <div class="row" style="margin-top: 10px;">
                                <div class="col-sm-4">
                                    <label for="curso">Curso:</label>
                                </div>
                                <div class="col-sm">
                                    <input type="text" id="curso" class="form-control" value="{{ $constancia->categoriaCurso->curso }}" readonly>
                                </div>
                            </div>
                        </fieldset>
                    </div>
                </div>
            </div>
        </div>

        <div class="row justify-content-md-center">
            <div class="col-md-auto">
                <a href="{{ url()->previous() }}" class="btn btn-primary" role="button" style="background: #21ADB5; margin-top: 5px;">Ir al Buscador</a>
            </div>
        </div>
    </div>

</body>

</html>

