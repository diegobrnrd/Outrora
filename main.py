# Importação de módulos (KivyMD e Kivy)
from random import choice
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager


# Classe principal do jogo
class OutroraApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Gerenciador de telas
        self.screen_manager = ScreenManager()
        self.tela_inicial = TelaInicial(name='tela_inicial')
        self.tela_historia = TelaHistoria(name='tela_historia')
        self.tela_creditos = TelaCreditos(name='tela_creditos')
        # Lista de músicas
        self.lista_de_musicas = ['musica.mp3', 'musica_2.mp3', 'musica_3.mp3', 'musica_4.mp3']
        # Escolha da musica aleatoriamente
        self.musica_aleatoria = choice(self.lista_de_musicas)
        # Carrega a música
        self.sound = SoundLoader.load(self.musica_aleatoria)

    def build(self):
        # Adiciona as telas ao gerenciador
        self.screen_manager.add_widget(self.tela_inicial)
        self.screen_manager.add_widget(self.tela_historia)
        self.screen_manager.add_widget(self.tela_creditos)
        # Loop na música
        self.sound.loop = True
        # Reproduz a música
        self.sound.play()
        # Configura o jogo para iniciar em tela cheia
        Config.set('graphics', 'fullscreen', 'auto')
        Config.write()
        return self.screen_manager

    # Para a música ao fechar o jogo
    def para_musica(self):
        if self.sound and self.sound.state == 'play':
            self.sound.stop()
            self.sound.unload()


# Define a tela inicial do jogo
class TelaInicial(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Imagem da tela inicial
        imagem = Image(source='tela_inicial.jpg',
                       allow_stretch=True,
                       keep_ratio=True)
        # Botão da tela inicial, quando pressionado chama a função troca tela
        botao_inicial = MDRaisedButton(text='Iniciar Jogo',
                                       on_release=self.troca_tela,
                                       pos_hint={'center_x': 0.5},
                                       md_bg_color=(0.5, 0, 0.1, 1))
        # Adiciona a imagem e o botão ao FloatLayout
        layout = FloatLayout()
        layout.add_widget(imagem)
        layout.add_widget(botao_inicial)
        # Adiciona o layout ao widget
        self.add_widget(layout)

    # Troca da tela inicial para a tela história
    def troca_tela(self, instance):
        self.manager.current = 'tela_historia'


# Define a tela história do jogo
class TelaHistoria(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Imagem da tela história
        imagem = Image(source='historia.jpg',
                       allow_stretch=True,
                       keep_ratio=True)
        # Adiciona a imagem ao FloatLayout
        layout = FloatLayout()
        layout.add_widget(imagem)
        # Adiciona o layout ao widget
        self.add_widget(layout)
        # História do jogo está armazenada em uma lista
        # Cada elemento da lista é um dicionário
        # Cada dicionário tem duas chaves
        # O valor associado a chave pergunta é uma string
        # O valor associado a chave escolhas é uma lista com n strings dentro
        self.estados_da_historia = [
            {'pergunta': 'Durante um acampamento com amigos, uma noite que era para ser tranquila se transforma '
                         'em um pesadelo.\nAo despertar, você percebe que seus amigos desapareceram.\nUm barulho '
                         'perturbador ecoa na escuridão.',
             'escolhas': ['Investigar Imediatamente', 'Voltar a Dormir']},
            {'pergunta': 'Saindo da barraca de acampamento com uma lanterna em punho,\nseu objetivo é alcançar uma '
                         'cabana abandonada situada no coração da floresta.\nHá uma suspeita de que seus amigos '
                         'possam ter ido investigá-la sem você.\nAo se deparar com uma bifurcação na floresta, '
                         'surge a necessidade de escolher qual caminho seguir.',
             'escolhas': ['Caminho Iluminado', 'Atalho Sombrio']},
            {'pergunta': 'Sob o manto da noite, uma presença ameaçadora se materializa nos cantos mais profundos '
                         'de seus sonhos.\nA escuridão te envolve, e risadas sussurrantes acompanham sua jornada '
                         'além da consciência.\nA confusão, silenciosa e implacável, te abraça enquanto você '
                         'descansa, te levando para além do reino da lucidez.',
             'escolhas': ['Tentar Novamente', 'Fechar Jogo']},
            {'pergunta': 'Conforme a trilha se estreita, você começa a sentir uma presença maligna ao seu redor. '
                         '\nParece que olhares invisíveis o acompanham entre as árvores.',
             'escolhas': ['Ignorar e Continuar', 'Retornar Rapidamente']},
            {'pergunta': 'Ao ignorar os sussurros, a presença invisível se intensifica.\nA escuridão, antes apenas '
                         'percebida, se materializa em sombras assustadoras que o envolvem.\nUm frio intenso '
                         'preenche o ar, enquanto a voz sussurrante se transforma em risadas macabras.\nVocê é '
                         'envolvido por uma escuridão infinita, perdendo-se na confusão que se esconde entre as '
                         'sombras.',
             'escolhas': ['Tentar Novamente', 'Fechar Jogo']},
            {'pergunta': 'Ao retornar rapidamente pelo caminho iluminado, o trajeto agora é desconhecido.\nSombras '
                         'se movem à medida que a trilha se transforma em um labirinto assustador.\nO ar fica '
                         'pesado, e a voz sussurrante se torna um lamento triste.\nVocê, incapaz de encontrar a '
                         'saída, é consumido pela confusão do labirinto,\nsua lucidez desaparece como uma vela '
                         'queimando até o fim.',
             'escolhas': ['Tentar Novamente', 'Fechar Jogo']},
            {'pergunta': 'Enquanto avança pela escuridão, a luz vacilante da sua lanterna é a única companhia. '
                         '\nDe repente, um filhote de urso-pardo emerge à sua frente, seus olhos curiosos refletem '
                         'a luz.',
             'escolhas': ['Acariciar o Filhote', 'Correr']},
            {'pergunta': 'Ao acariciar o filhote de urso-pardo, um rugido ensurdecedor rompe a noite, indicando a '
                         'presença de um urso adulto enfurecido.\nNo entanto, em vez do esperado ataque, o urso '
                         'surpreendentemente envolve você em uma dança inusitada.\nA confusão aumenta quando, de '
                         'repente, o urso se transforma em uma jarra, depois em uma idosa e por fim em um '
                         'bico-de-tamanco.\nA realidade distorcida desafia a lógica, desencadeando uma vertigem '
                         'mental insuportável.\nIncapaz de lidar com a loucura que se desenrola diante dos seus '
                         'olhos, sua mente sucumbe ao colapso,\nafundando em um abismo de confusão sem retorno.',
             'escolhas': ['Tentar Novamente', 'Fechar Jogo']},
            {'pergunta': 'Desesperado, você corre pela escuridão; a luz da sua lanterna é insuficiente para tal '
                         'ato.\nVocê tropeça em galhos, esbarra em árvores, até que um impacto abrupto interrompe '
                         'sua fuga, fazendo-o desmaiar.\nQuando seus olhos se abrem novamente, a noite ainda domina '
                         'o cenário.\nAo seu lado, você nota um estranho totem em forma de um pombo obeso.',
             'escolhas': ['Pegar o Totem', 'Ignorar o Totem', 'Tentar Quebrar o Totem']},
            {'pergunta': 'Conforme você avança pela floresta, vislumbrando a cabana ao longe, a sensação de '
                         'urgência cresce a cada passo.\nA escuridão parece se intensificar, e a distância até a '
                         'cabana parece inalterada.\nSeguindo pela trilha principal, você se aproxima da cabana, '
                         'cuja silhueta sombria se destaca contra o céu noturno.\nSeus passos ecoam na quietude da '
                         'floresta enquanto a cabana se torna mais palpável,\ne você está à beira de explorar seus '
                         'segredos sombrios.',
             'escolhas': ['Continuar']},
            {'pergunta': 'Ao se aproximar da cabana, uma calmaria intensa toma conta do ambiente.\nO murmúrio '
                         'da floresta se desvanece, e até mesmo o vento parece reter qualquer movimento.\nUma '
                         'quietude densa paira no ar, criando uma atmosfera de serenidade quase familiar.\nEssa '
                         'tranquilidade peculiar provoca uma instigação momentânea,\nconvidando-o a explorar o '
                         'interior da cabana e descobrir o que ela esconde.',
             'escolhas': ['Continuar']},
            {'pergunta': 'Num piscar de olhos, a escuridão da noite se dissipa, dando lugar a uma aurora súbita. '
                         '\nO ambiente, antes envolto em sombras, é agora banhado por uma luz diurna reconfortante. '
                         '\nO céu se transforma rapidamente de estrelado para um azul claro,\ncomo se a noite tivesse '
                         'sido apenas um breve suspiro na passagem do tempo.',
             'escolhas': ['Continuar']},
            {'pergunta': 'Ao ficar a apenas três passos da porta da cabana, você é surpreendido por um barulho sutil '
                         'vindo dos fundos.',
             'escolhas': ['Investigar', 'Ignorar']},
            {'pergunta': '',
             'escolhas': ['Abrir Porta', 'Bater na Porta', 'Investigar o Barulho']},
            {'pergunta': 'Você tenta girar a maçaneta para abrir a porta da frente. No entanto, uma resistência '
                         'inexplicável frustra seus esforços.\nA maçaneta permanece imóvel, como se algo do outro '
                         'lado estivesse se opondo à sua entrada.\nApesar de várias tentativas, a porta continua '
                         'intransponível.',
             'escolhas': ['Soltar Maçaneta']},
            {'pergunta': 'Você bate três vezes na porta da cabana, mas um silêncio denso engole as batidas.\nO som '
                         'não reverbera na quietude noturna da floresta.\nQuinze segundos se arrastam, e nenhum sinal '
                         'de resposta.\nDecidindo chamar pelos seus amigos, você se vê perplexo\nquando percebe que os '
                         'nomes deles escapam de sua mente como sombras evasivas.',
             'escolhas': ['Continuar']},
            {'pergunta': 'Ao se dirigir para o fundo da cabana, uma descoberta inesperada surge diante de seus olhos. '
                         '\nUma janela entreaberta revela uma fraca luminosidade no interior.\nA escuridão circundante '
                         'parece recuar da abertura, sugerindo uma possível entrada discreta.\nUma brisa suave carrega '
                         'murmúrios indefinidos que escapam pela janela, criando uma atmosfera de mistério.',
             'escolhas': ['Entrar Pela Janela']},
            {'pergunta': 'Ao atravessar o limiar da cabana, você é envolvido por uma luminosidade fugaz.',
             'escolhas': ['Continuar']},
            {'pergunta': 'Diante de seus olhos, surgem vislumbres de memórias há muito esquecidas: risos sob o luar, '
                         'sombras de amizades perdidas\ne o calor reconfortante de momentos que parecem pertencer a '
                         'outra vida.',
             'escolhas': ['Continuar']},
            {'pergunta': 'Uma melodia distante ressoa, despertando emoções há muito adormecidas.',
             'escolhas': ['Continuar']},
            {'pergunta': 'Nesse breve instante, o peso do desconhecido se dissipa temporariamente,\ne você se '
                         'encontra imerso em um lampejo de clareza fugaz, porém impactante.',
             'escolhas': ['Continuar']},
            {'pergunta': 'No entanto, como uma estrela cadente que se desvanece no firmamento, essa lucidez efêmera '
                         'desaparece rapidamente.',
             'escolhas': ['Continuar']},
            {'pergunta': 'A cabana, que antes estava iluminada, é agora absorvida pela penumbra da incerteza.',
             'escolhas': ['Continuar']},
            {'pergunta': 'As memórias escorrem por seus dedos como areia, deixando apenas a sensação de algo '
                         'inatingível.',
             'escolhas': ['Continuar']},
            {'pergunta': 'Um silêncio melancólico preenche o espaço, enquanto você mergulha novamente na névoa de '
                         'sua própria mente,\nenvolvido em uma atmosfera de perda e saudade.',
             'escolhas': ['Continuar']},
        ]
        # Variável para controla a obtenção do dicionário correspondente
        self.indice_do_estado_atual = 0
        # Organiza os widgtes verticalmente
        self.container = MDBoxLayout(orientation='vertical', spacing='10')
        # Chama a função estado de exibição
        self.estado_de_exibicao()
        # Adiciona o container ao widget
        self.add_widget(self.container)

    # Exibe o texto e os botões na tela
    def estado_de_exibicao(self):
        # Limpa os widgets a cada rodada
        self.container.clear_widgets()
        # Em estado é armazenado o dicionário correspondente
        # O indice de acesso será a variável indice do estado atual
        estado = self.estados_da_historia[self.indice_do_estado_atual]
        # Em texto pergunta é armazenada o valor (string) da chave pergunta
        texto_pergunta = MDLabel(text=estado['pergunta'],
                                 halign='left',
                                 font_style='H6',
                                 theme_text_color="Custom",
                                 text_color=(0.969, 0.902, 0.651, 1))
        # Espaçamento do texto da borda do widget
        texto_pergunta.padding = [50, 0, 50, 0]
        # Adiciona o texto ao widget
        self.container.add_widget(texto_pergunta)
        # Um for é passado na chave escolhas
        for escolha in estado['escolhas']:
            # Cada elemento que tiver no lista escolhas é criado com seu respectivo texto
            # Quando pressionado chama a função quando escolher
            botao = MDRaisedButton(text=escolha,
                                   on_release=self.quando_escolher,
                                   pos_hint={'center_x': 0.5},
                                   md_bg_color=(0.902, 0.627, 0.435, 1),
                                   text_color=(0.012, 0, 0.11, 1),
                                   opacity=0)
            # Adiciona os botões ao widget
            self.container.add_widget(botao)
            # Animação fade-in nos botões
            animacao = Animation(opacity=1, duration=0.5)
            animacao.start(botao)

    # Controle da história
    def quando_escolher(self, atual):
        # Guarda o texto do botão que foi pressionado na variável escolha atual
        escolha_atual = atual.text
        # Verifica qual o valor do indice do estado atual
        # Verifica qual botão foi pressionado
        # Define o novo valor do indice do estado atual
        # Fecha o jogo em alguns casos
        if self.indice_do_estado_atual == 0:  # (0) Contexto Inicial
            if escolha_atual == 'Investigar Imediatamente':
                self.indice_do_estado_atual = 1
            elif escolha_atual == 'Voltar a Dormir':
                self.indice_do_estado_atual = 2
        elif self.indice_do_estado_atual == 1:  # (1) Escolha na Bifurcação
            if escolha_atual == 'Caminho Iluminado':
                self.indice_do_estado_atual = 3
            elif escolha_atual == 'Atalho Sombrio':
                self.indice_do_estado_atual = 6
        elif self.indice_do_estado_atual == 2:  # (2)  Perdido 1
            if escolha_atual == 'Tentar Novamente':
                self.indice_do_estado_atual = 0
            elif escolha_atual == 'Fechar Jogo':
                app = MDApp.get_running_app()
                app.stop()
                return
        elif self.indice_do_estado_atual == 3:  # (3) Ponto Perdido
            if escolha_atual == 'Ignorar e Continuar':
                self.indice_do_estado_atual = 4
            elif escolha_atual == 'Retornar Rapidamente':
                self.indice_do_estado_atual = 5
        elif self.indice_do_estado_atual == 4:  # (4) Perdido 2
            if escolha_atual == 'Tentar Novamente':
                self.indice_do_estado_atual = 0
            elif escolha_atual == 'Fechar Jogo':
                app = MDApp.get_running_app()
                app.stop()
                return
        elif self.indice_do_estado_atual == 5:  # (5) Perdido 3
            if escolha_atual == 'Tentar Novamente':
                self.indice_do_estado_atual = 0
            elif escolha_atual == 'Fechar Jogo':
                app = MDApp.get_running_app()
                app.stop()
                return
        elif self.indice_do_estado_atual == 6:  # (6) Encontro Noturno
            if escolha_atual == 'Acariciar o Filhote':
                self.indice_do_estado_atual = 7
            elif escolha_atual == 'Correr':
                self.indice_do_estado_atual = 8
        elif self.indice_do_estado_atual == 7:  # (7) Perdido 4
            if escolha_atual == 'Tentar Novamente':
                self.indice_do_estado_atual = 0
            elif escolha_atual == 'Fechar Jogo':
                app = MDApp.get_running_app()
                app.stop()
                return
        elif self.indice_do_estado_atual == 8:  # (8) Desmaio
            if escolha_atual == 'Pegar o Totem':
                self.indice_do_estado_atual = 0
            elif escolha_atual == 'Ignorar o Totem':
                self.indice_do_estado_atual = 9
            elif escolha_atual == 'Tentar Quebrar o Totem':
                self.indice_do_estado_atual = 0
        elif self.indice_do_estado_atual == 9:  # (9) Ponto Vivo
            if escolha_atual == 'Continuar':
                self.indice_do_estado_atual = 10
        elif self.indice_do_estado_atual == 10:  # (10) Familiar
            if escolha_atual == 'Continuar':
                self.indice_do_estado_atual = 11
        elif self.indice_do_estado_atual == 11:  # (11) Amanhecer
            if escolha_atual == 'Continuar':
                self.indice_do_estado_atual = 12
        elif self.indice_do_estado_atual == 12:  # (12) Frente
            if escolha_atual == 'Investigar':
                self.indice_do_estado_atual = 16
            elif escolha_atual == 'Ignorar':
                self.indice_do_estado_atual = 13
        elif self.indice_do_estado_atual == 13:  # (13)
            if escolha_atual == 'Abrir Porta':
                self.indice_do_estado_atual = 14
            elif escolha_atual == 'Bater na Porta':
                self.indice_do_estado_atual = 15
            elif escolha_atual == 'Investigar o Barulho':
                self.indice_do_estado_atual = 16
        elif self.indice_do_estado_atual == 14:  # (14) Maçaneta
            if escolha_atual == 'Soltar Maçaneta':
                self.indice_do_estado_atual = 13
        elif self.indice_do_estado_atual == 15:  # (15) Nomes
            if escolha_atual == 'Continuar':
                self.indice_do_estado_atual = 13
        elif self.indice_do_estado_atual == 16:  # (16) Janela
            if escolha_atual == 'Entrar Pela Janela':
                self.indice_do_estado_atual = 17
        elif self.indice_do_estado_atual == 17:  # (17) FINAL
            if escolha_atual == 'Continuar':
                self.indice_do_estado_atual = 18
        elif self.indice_do_estado_atual == 18:  # (18) FINAL
            if escolha_atual == 'Continuar':
                self.indice_do_estado_atual = 19
        elif self.indice_do_estado_atual == 19:  # (19) FINAL
            if escolha_atual == 'Continuar':
                self.indice_do_estado_atual = 20
        elif self.indice_do_estado_atual == 20:  # (20) FINAL
            if escolha_atual == 'Continuar':
                self.indice_do_estado_atual = 21
        elif self.indice_do_estado_atual == 21:  # (21) FINAL
            if escolha_atual == 'Continuar':
                self.indice_do_estado_atual = 22
        elif self.indice_do_estado_atual == 22:  # (22) FINAL
            if escolha_atual == 'Continuar':
                self.indice_do_estado_atual = 23
        elif self.indice_do_estado_atual == 23:  # (23) FINAL
            if escolha_atual == 'Continuar':
                self.indice_do_estado_atual = 24
        elif self.indice_do_estado_atual == 24:  # (24) FINAL
            if escolha_atual == 'Continuar':
                self.troca_tela_2()
        # Verificação (loop) para chamar a função estado de exibição novamente
        if self.indice_do_estado_atual < len(self.estados_da_historia):
            self.estado_de_exibicao()

    # Para a música de tocar e troca para a tela créditos
    def troca_tela_2(self, instance=None):
        app = MDApp.get_running_app()
        if app.sound and app.sound.state == 'play':
            app.sound.stop()
            app.sound.unload()
        self.manager.current = 'tela_creditos'


# Classe responsável pela tela de créditos do jogo
class TelaCreditos(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fechar_jogo = None
        # Inicia o video pausado
        self.video_creditos = Video(source='creditos.mp4',
                                    state='pause',
                                    options={'allow_stretch': True, 'keep_ratio': True})
        # Adiciona o video ao widget
        self.add_widget(self.video_creditos)

    # Ao entrar na tela créditos
    def on_enter(self):
        super().on_enter()
        # Chama o método play video
        self.play_video()
        # Agenda a adição do botão fechar jogo na tela
        Clock.schedule_once(self.adicionar_botao_fechar_jogo, 60.7)

    # Reproduz o vídeo
    def play_video(self):
        self.video_creditos.state = 'play'

    # Ao sair da tela créditos
    def on_leave(self):
        super().on_leave()
        # Chama o método pause video
        self.pause_video()

    # Pausa o vídeo
    def pause_video(self):
        self.video_creditos.state = 'pause'

    # Adiciona o botão fechar Jogo
    def adicionar_botao_fechar_jogo(self, dt):
        self.fechar_jogo = MDRaisedButton(text='Fechar Jogo',
                                          on_release=self.fecha_jogo,
                                          pos_hint={'center_x': 0.5, 'center_y': 0.050},
                                          md_bg_color=(1, 1, 1, 1),
                                          text_color=(0, 0, 0, 1))
        # Adiciona o botão ao widget
        self.add_widget(self.fechar_jogo)

    # Função para fechar o jogo
    @staticmethod
    def fecha_jogo(instance):
        app = MDApp.get_running_app()
        app.stop()
        return


# Executa o jogo
if __name__ == '__main__':
    OutroraApp().run()
