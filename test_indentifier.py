import pytest
from identifier import Identifier


def test_identificador_valido():
  id_checker = Identifier()
  assert id_checker.validate_identifier("abc") is True

def test_identificador_invalido_inicia_com_numero():
  id_checker = Identifier()
  assert id_checker.validate_identifier("123abc") is False

def test_identificador_invalido_muito_longo():
  id_checker = Identifier()
  assert id_checker.validate_identifier("a234567") is False

def test_identificador_vazio():
    id_checker = Identifier()
    assert id_checker.validate_identifier("") is False

def teste_identificador_valido_apenas_um_caractere():
  id_checker = Identifier()
  assert id_checker.validate_identifier("o") is True

def test_identificador_invalido_caractere_especial():
  id_checker = Identifier()
  assert id_checker.validate_identifier("a_-72") is False

def test_identificador_valido_seis_caracteres():
  id_checker = Identifier()
  assert id_checker.validate_identifier("a23456") is True





