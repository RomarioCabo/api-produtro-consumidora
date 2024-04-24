from flask_restx import fields


class ClientModel:
    @staticmethod
    def get_model(api):
        return api.model('Cliente', {
            'id': fields.String(required=True, description='Identificador único do cliente', example='123456'),
            'nome': fields.String(required=True, description='Nome completo do cliente',
                                  example='Givaldo Santos Vasconcelos'),
            'documento': fields.String(required=True, description='Documento de identificação do cliente',
                                       example='70420816097'),
            'tipoDocumento': fields.String(required=True, description='Tipo de documento de identificação',
                                           example='CPF'),
            'tipoPessoa': fields.String(required=True, description='Tipo de pessoa (Física ou Jurídica)', example='F'),
            'endereco': fields.String(required=True, description='Endereço do cliente',
                                      example='Travessa Francisco Vieira'),
            'numeroEndereco': fields.String(required=True, description='Número do endereço', example='11'),
            'complementoEndereco': fields.String(required=True, description='Complemento do endereço',
                                                 example='Apto 405'),
            'bairro': fields.String(required=True, description='Bairro do cliente', example='Trapiche da Barra'),
            'cidade': fields.String(required=True, description='Cidade do cliente', example='Maceió'),
            'estado': fields.String(required=True, description='Estado do cliente', example='AL'),
            'pais': fields.String(required=True, description='País do cliente', example='BR'),
            'cep': fields.String(required=True, description='CEP do cliente', example='57010460'),
            'codigoIbge': fields.String(required=True, description='Código IBGE da localidade do cliente',
                                        example='7162435'),
            'telefone': fields.String(required=True, description='Telefone do cliente', example='(82) 36774-7713'),
            'email': fields.String(required=True, description='E-mail do cliente',
                                   example='givaldo.santos.vasconcelos@gmail.com')
        })
