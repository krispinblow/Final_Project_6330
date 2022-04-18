from finallib.services import unit_of_work


def evaluates_view(teacher_name: str, uow: unit_of_work.SqlAlchemyUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT teacher_name, club_name FROM evaluates WHERE teacher_name = :teacher_name
            """,
            dict(teacher_name=teacher_name),
        )
    return [dict(r) for r in results]