from validate_docbr import CPF, CNPJ

class ValidaCpf:
    def __init__(self, cpf):
        self.analisa_cpf(cpf)

    def analisa_cpf(self, cpf):
        if len(cpf) == 11:
            analisa_cpf = CPF()
            if analisa_cpf.validate(cpf):
                self.cpf = cpf
                print('CPF salvo')
            else:
                raise ValueError('CPF inserido não é valido')
        else:
            raise ValueError('Número de digitos incorreto')

    def formata_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)

    def __str__(self):
        return self.formata_cpf()

class ValidaCnpj:
    def __init__(self,cnpj):
        self.analisa_cnpj(cnpj)

    def analisa_cnpj(self, cnpj):
        if len(cnpj) == 14:
            analisa_cnpj = CNPJ()
            if analisa_cnpj.validate(cnpj):
                self.cnpj = cnpj
                print('CNPJ salvo')
            else:
                raise ValueError('CNPJ inserido não é valido')
        else:
            raise ValueError('Número de digitos incorreto')

    def formata_cnpj(self):
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self.cnpj)

    def __str__(self):
        return self.formata_cnpj()


# cnpj1 = '00360305000104'
# obj_cnpj1 = ValidaCnpj(cnpj1)
# print(obj_cnpj1,'\n')
#
# cpf1 = '71306554020'
# obj_cpf1 = ValidaCpf(cpf1)
# print(obj_cpf1)

