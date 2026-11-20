from abc import ABC
from datetime import datetime

class Base(ABC):
    _contadores: dict[type, int] = {}

    def __init__(self, id_personalizado: int | None = None) -> None:
        if id_personalizado is not None:
            self._id: int = id_personalizado
        else:
            self._id: int = self._generar_siguiente_id()

        self._eliminado: bool = False
        self._creado_en: datetime = datetime.now()

    def _generar_siguiente_id(self) -> int:
        tipo_actual = type(self)
        if tipo_actual not in Base._contadores:
            Base._contadores[tipo_actual] = 0
        Base._contadores[tipo_actual] += 1
        return Base._contadores[tipo_actual]

    @property
    def id(self) -> int:
        return self._id

    @property
    def eliminado(self) -> bool:
        return self._eliminado

    @eliminado.setter
    def eliminado(self, valor: bool) -> None:
        self._eliminado = bool(valor)

    @property
    def creado_en(self) -> datetime:
        return self._creado_en

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Base):
            return False
        return self.id == otro.id and type(self) is type(otro)