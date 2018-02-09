from politica import Politicos, Partidos

joao = Politicos(
	"João de Souza Oliveira",
	"111.222.333-44",

)

maria = Politicos(
	"Maria Pereira Albuquerque",
	"555.666.777-88",

)

jose = Politicos(
	"José Bonifácio da Silva",
	"444.333.222-11",
	"Jota"

)

pr = Partidos(
	"Partido da República",
	"PR",
	22,
	1000
)

pt = Partidos(
	"Partido dos Trabalhadores",
	"PT",
	13,
	5000
)

pr.adicionar_politico(joao)
pr.adicionar_politico(maria)

pr.adicionar_politicos(joao, maria)

pt.adicionar_politicos(jose, joao)

pt.realizar_doacao_politicos()

jose.receber_dinheiro(1000)
jose.receber_dinheiro(200)
jose.exibir_dinheiro()



