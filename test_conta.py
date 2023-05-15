import unittest 

from Conta import Conta

class TestConta(unittest.TestCase):
    def test_depositar(self):
        conta = Conta(1, "Cerquis")
        conta.depositar(100)
        self.assertEqual(conta.obter_saldo(), 100)
        
    def test_sacar(self):
        conta = Conta(2, "Lennon")
        conta.depositar(100)
        conta.sacar(50)
        self.assertEqual(conta.obter_saldo(), 50)
        with self.assertRaises(ValueError):
            conta.sacar(100)
    
    def test_erros_depositar(self):
        conta = Conta(3, "João")
        with self.assertRaises(ValueError):
            conta.depositar(-50)
            
    def test_erros_sacar(self):
        conta = Conta(4, "Fogaça")
        with self.assertRaises(ValueError):
            conta.sacar(-50)
        with self.assertRaises(ValueError):
            conta.sacar(100)
