import unittest
from unittest.mock import MagicMock

from Banco import Banco

class TestBanco(unittest.TestCase):

    def setUp(self):
        self.banco = Banco()
        self.conta1 = MagicMock()
        self.conta1.numero_conta = 123
        self.conta2 = MagicMock()
        self.conta2.numero_conta = 456

    def test_adicionar_conta(self):
        self.banco.adicionar_conta(self.conta1)
        self.assertIn(123, self.banco.contas)

        with self.assertRaises(ValueError):
            self.banco.adicionar_conta(self.conta1)

        self.banco.adicionar_conta(self.conta2)
        self.assertIn(456, self.banco.contas)

    def test_remover_conta(self):
        with self.assertRaises(ValueError):
            self.banco.remover_conta(789)

        self.banco.adicionar_conta(self.conta1)
        self.banco.adicionar_conta(self.conta2)

        self.banco.remover_conta(123)
        self.assertNotIn(123, self.banco.contas)

        with self.assertRaises(ValueError):
            self.banco.remover_conta(123)

    def test_listar_contas(self):
        self.banco.adicionar_conta(self.conta1)
        self.banco.adicionar_conta(self.conta2)

        contas = self.banco.listar_contas()
        self.assertEqual(len(contas), 2)
        self.assertIn(self.conta1, contas)
        self.assertIn(self.conta2, contas)