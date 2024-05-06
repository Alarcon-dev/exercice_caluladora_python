"""
#ejercicio de cajero automático que tenga las siguientes funciones: 

# Retirar efectivo: Cuenta de ahorros, corriente, nequi y bancolombia a la mano (número de teléfono y/o clave correcta dependiendo el caso, tener saldo a favor, no superar el limite diario de retiro dos 2 millones de pesos)

# Realizar avances en efectivo: Tarjeta de crédito (clave correcta, tener saldo a favor, no superar el limite diario de avance de 2 millones de pesos)

# transferencias: Cuentas bancolombia, cuentas inscritas y no inscritas. (clave correcta, tener saldo a favor, no debe superar los 2 millones de pesos para las cuentas no inscritas)

# Pago de servicios: Agua, luz, gas, internet, teléfono, tv, celular, créditos, impuestos, multas, educación, salud, entretenimiento, otros (número de teléfono y/o clave correcta dependiendo el caso, tener saldo a favor)

# Cambiar clave principal (número de teléfono y/o clave correcta dependiendo el caso)
"""

class CajeroAutomatico:
    def __init__(self, saldo_total):
        self.saldo_total = saldo_total
        self.limite_retiro_diario = 2000000
        self.limite_avance_diario = 2000000

    def retirar_efectivo(self, cuenta, clave, monto):
        if cuenta == "ahorros" or cuenta == "corriente" or cuenta == "nequi" or cuenta == "bancolombia":
           
            if clave_correcta(clave) and self.saldo_total >= monto and monto <= self.limite_retiro_diario:
                self.saldo_total -= monto
                return f"Retiro exitoso. Saldo restante: {self.saldo_total}"
            else:
                return "No se puede realizar el retiro"
        else:
            return "Tipo de cuenta no válido"

    def realizar_avance_efectivo(self, tarjeta, clave, monto):
       
        if tarjeta == "credito" and clave_correcta(clave) and self.saldo_total >= monto and monto <= self.limite_avance_diario:
            self.saldo_total -= monto
            return f"Avance en efectivo realizado. Saldo restante: {self.saldo_total}"
        else:
            return "No se puede realizar el avance en efectivo"

    def transferencia(self, cuenta_destino, clave, monto):
      
        if clave_correcta(clave) and self.saldo_total >= monto and monto <= self.limite_transferencia:
            self.saldo_total -= monto
            return f"Transferencia realizada a {cuenta_destino}. Saldo restante: {self.saldo_total}"
        else:
            return "No se puede realizar la transferencia"

    def pagar_servicio(self, servicio, clave, monto):
       
        if clave_correcta(clave) and self.saldo_total >= monto:
            self.saldo_total -= monto
            return f"Pago de {servicio} realizado. Saldo restante: {self.saldo_total}"
        else:
            return "No se puede realizar el pago del servicio"

    def cambiar_clave(self, cuenta, clave_actual, nueva_clave):
       
        return "Clave cambiada exitosamente"


def clave_correcta(clave):
    
    return True



cajero = CajeroAutomatico(saldo_total=10000000)
print(cajero.retirar_efectivo("ahorros", "1234", 1500000))
print(cajero.realizar_avance_efectivo("credito", "5678", 1000000))
print(cajero.transferencia("cuenta_destino", "91011", 500000))
print(cajero.pagar_servicio("agua", "1213", 200000))
print(cajero.cambiar_clave("nequi", "1415", "1617"))
    
    







  