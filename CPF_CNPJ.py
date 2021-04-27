from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def analisa_doc(doc):
        if len(doc) == 11:
            return Cpf(doc)
        elif len(doc) == 14:
            return Cnpj(doc)
        else:
            raise ValueError("Número de digitos incorreto!!")

class Cpf:

    def __init__(self, doc):
        if self.analisa_cpf(doc):
            self.cpf = doc
        else:
            raise ValueError('CPF inserido não é valido!')

    def analisa_cpf(self, doc):
        analisa_cpf = CPF()
        return analisa_cpf.validate(doc)

    def formata_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)

    def __str__(self):
        print("CPF salvo!")
        return self.formata_cpf()

class Cnpj:

    def __init__(self, doc):
        if self.analisa_cnpj(doc):
            self.cnpj = doc
        else:
            raise ValueError('CNPJ inserido não é valido!')

    def analisa_cnpj(self, doc):
        analisa_cnpj = CNPJ()
        return analisa_cnpj.validate(doc)

    def formata_cnpj(self):
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self.cnpj)

    def __str__(self):
        print("CNPJ salvo!")
        return self.formata_cnpj()


cnpj1 = '00360305000104'
obj_cnpj1 = Cnpj(cnpj1)
print(obj_cnpj1,'\n')

cpf1 = '71306554020'
obj_cpf1 = Cpf(cpf1)
print(obj_cpf1)

