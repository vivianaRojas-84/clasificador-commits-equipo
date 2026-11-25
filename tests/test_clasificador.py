from app.main import clasificar_eco


def test_clasificar_docs():
    assert clasificar_eco("docs: actualizar README") == "docs"


def test_clasificar_test():
    assert clasificar_eco("test: agregar pruebas") == "test"


def test_clasificar_fix():
    assert clasificar_eco("fix: corregir error") == "fix"


def test_clasificar_feat():
    assert clasificar_eco("feat: agregar usuarios") == "feat"


def test_clasificar_refactor():
    assert clasificar_eco("refactor: mejorar codigo") == "refactor"


def test_clasificar_otros():
    assert clasificar_eco("actualizar informacion") == "otros"

