from dataclasses import dataclass

from cats.application.common.persistence.cat import CatGateway
from cats.application.common.validators import validate_cat
from cats.entities.cat.models import Cat, CatID


@dataclass(frozen=True, slots=True)
class GetCatWithIDQuery:
    id: int


@dataclass(frozen=True, slots=True)
class CatOutput:
    cat: Cat


class GetCatWithIDQueryHandler:
    def __init__(self, cat_gateway: CatGateway) -> None:
        self._cat_gateway = cat_gateway

    async def run(self, data: GetCatWithIDQuery) -> CatOutput:
        cat = await self._cat_gateway.with_id(CatID(data.id))
        assert validate_cat(cat, data.id)
        return CatOutput(cat)
