from fastapi import Query


class FastApiPaginator:
    def __init__(
        self,
        page_size: int = Query(
            ge=1, le=100, default=10, description="Количество записей на странице"
        ),
        page_number: int = Query(ge=1, le=100, default=1, description="Номер страницы"),
    ):
        self.page_size = page_size
        self.page_number = page_number

    def get_offset(self):
        offset = self.page_size * (self.page_number - 1)
        return offset
