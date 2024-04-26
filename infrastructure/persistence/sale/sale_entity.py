from datetime import datetime, timezone

from application import db


class SaleEntity(db.Model):
    __tablename__ = 'vendas'

    id = db.Column(db.Integer, primary_key=True)
    canal = db.Column(db.String(100), nullable=False)
    codigo_empresa = db.Column(db.Integer, nullable=False)
    codigo_loja = db.Column(db.Integer, nullable=False)
    numero_pdv = db.Column(db.Integer, nullable=False)
    numero_pedido = db.Column(db.String(100), nullable=False)
    numero_ordem_externo = db.Column(db.String(100), nullable=False)
    valor_total = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    quantidade_itens = db.Column(db.Integer, nullable=False)
    venda_request = db.Column(db.Text, nullable=False)
    data_atualizacao = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    data_requisicao = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    chave_nfe = db.Column(db.String(100))
    numero_nota = db.Column(db.Integer)
    data_emissao = db.Column(db.DateTime)
    pdf = db.Column(db.Text)
    situacao = db.Column(db.String(50), nullable=False)
    motivo = db.Column(db.Text)

    def __init__(self, canal, codigo_empresa, codigo_loja, numero_pdv, numero_pedido,
                 numero_ordem_externo, valor_total, quantidade_itens, venda_request,
                 data_atualizacao, data_requisicao, chave_nfe=None, numero_nota=None,
                 data_emissao=None, pdf=None, situacao=None, motivo=None):
        self.canal = canal
        self.codigo_empresa = codigo_empresa
        self.codigo_loja = codigo_loja
        self.numero_pdv = numero_pdv
        self.numero_pedido = numero_pedido
        self.numero_ordem_externo = numero_ordem_externo
        self.valor_total = valor_total
        self.quantidade_itens = quantidade_itens
        self.venda_request = venda_request
        self.data_atualizacao = data_atualizacao
        self.data_requisicao = data_requisicao
        self.chave_nfe = chave_nfe
        self.numero_nota = numero_nota
        self.data_emissao = data_emissao
        self.pdf = pdf
        self.situacao = situacao
        self.motivo = motivo
