from fastapi import APIRouter

router = APIRouter(prefix="/locais", tags=["Locais"])


@router.get("/limgrave")

def get_limgrave():
    limgrave_info = {
  "Local": "Limgrave",
  "SubTitulo": "O início da jornada",
  "Descricao": "Limgrave é o ponto de partida da nossa jornada inesquecível em Elden Ring — uma região vasta, aparentemente pacífica, com planícies verdes, florestas escuras e ruínas cobertas de musgo. Mas por trás da beleza natural, há segredos perigosos e desafios mortais logo nos primeiros passos.\n\nAqui somos apresentados a mecânicas essenciais como coleta, criação, montaria com o cavalo Torrent, além de diversos NPCs intrigantes, como Varré (com seus comentários irônicos sobre não ter donzela), Boc, Yura e até o enigmático Alexander, o jarro guerreiro. Também encontramos o sempre memorável Patch, que continua fiel à sua reputação traiçoeira.\n\nLimgrave abriga cavernas, túneis e catacumbas espalhados por todos os cantos — como o Túnel de Limgrave e as Catacumbas Toca da Morte —, onde enfrentamos inimigos únicos e obtemos cinzas espirituais, materiais de upgrade e armas especiais. Um dos primeiros grandes sustos para os jogadores é o Dragão Voador Agheel, que desce ferozmente no Lago Agheel, bloqueando o acesso a tesouros e matando sem piedade os desavisados.\n\nAo norte, está o imponente Castelo Stormveil, uma fortaleza ancestral que serve como nosso primeiro teste real em Elden Ring. Guardado por soldados fanáticos, feras mutantes e o aterrorizante Leão enxertado, o castelo é lar de Godrick, o Enxertado — um dos portadores de Grandes Runas. Godrick é um descendente degenerado da linhagem dourada de Marika, obcecado por poder a ponto de enxertar membros de outros guerreiros em si mesmo. Sua luta é brutal e simbólica, sendo o ápice do primeiro grande arco da jornada.\n\nAntes mesmo de alcançar o castelo, somos confrontados por Margit, o Caído — um inimigo opcional nesse ponto, mas que funciona como guardião da entrada e um aviso claro de que Elden Ring não perdoa. Margit mais tarde será revelado como uma parte da complexa figura de Morgott, o Rei Prístino.\n\nFora do caminho principal, Limgrave ainda oferece regiões ricas como a Península das Lágrimas ao sul, onde fica o Castelo Morne, envolto em tragédias e revoltas de servos, e o Penhasco da Tempestade ao norte, que conduz ao desconhecido.\n\nE como esquecer o primeiro grande susto para os novatos? O Cavaleiro da Árvore, um inimigo montado com armadura dourada que patrulha a estrada logo no início do jogo. Derrotá-lo se torna um marco para quem está começando — e uma das primeiras recompensas reais de aprendizado nos padrões, tempos de ataque e persistência.\n\nLimgrave é, portanto, mais do que um tutorial expandido: é um campo de testes completo, repleto de descobertas, surpresas e momentos épicos. Um verdadeiro prólogo para a grandiosidade que está por vir no mundo das Terras Intermédias."
}
    return limgrave_info


@router.get("/liurnia")

def get_liurnia():
    liurnia_info= {
  "Local": "Liurnia",
  "SubTitulo": "A capital da magia!",
  "Descricao": "Liurnia é a região que exploramos após derrotar Godrick, o Enxertado, e sermos testados por Margit no Castelo Stormveil. Com a Grande Runa de Godrick em mãos, seguimos para o norte, rumo à capital da feitiçaria.\n\nConhecida como o reino dos magos, Liurnia dos Lagos foi, em tempos antigos, inimiga direta da Ordem Áurea. Seus cavaleiros mágicos de elite e poderosos feiticeiros se opuseram à fé dourada, defendendo a magia como fonte de poder e sabedoria. No centro da região, encontramos a imponente Academia de Raya Lucaria, um verdadeiro reflexo de sagas como Harry Potter, onde os grandes magos são formados.\n\nUm dos principais chefes da área é Rennala, Rainha da Lua Cheia — líder da academia, portadora de uma Grande Runa e mãe dos semideuses. Sua luta é marcante tanto em termos de gameplay quanto na narrativa do jogo.\n\nA paisagem de Liurnia é marcada por um imenso lago coberto por névoa, ruínas submersas, espectros sem cabeça, cavaleiros encantados e dragões que cospem gelo. É uma região misteriosa e envolvente, especialmente divertida para quem joga com magos, graças à grande quantidade de magias, catalisadores e itens voltados para builds de inteligência.\n\nA lore da região também revela conflitos internos e externos causados pela invasão da Ordem Áurea. Radagon, um dos maiores guerreiros da fé dourada, permaneceu em Liurnia, onde se casou com Rennala e teve três filhos semideuses: Rykard, Senhor da Blasfêmia; Radahn, o Flagelo Estelar; e Ranni, a bruxa. Todos são figuras centrais no universo de Elden Ring. Em Liurnia, podemos iniciar a quest de Ranni — uma missão opcional, mas extremamente rica e impactante, que pode até alterar o final do jogo. Já Radahn é encontrado em Caelid, e Rykard na Mansão Vulcânica — cenários que serão apresentados aqui futuramente com mais detalhes.\n\nEssa aliança entre fé e feitiçaria, que começou em Liurnia, colapsaria com o tempo, deixando um legado de conflito, tragédia e poder arcano. Liurnia é, sem dúvida, uma das regiões mais enigmáticas, belas e ricas em narrativa de todo o Interlúdio."
} 
    
    return liurnia_info

@router.get("/caelid")

def get_caelid():
    caelid_info = {
        "Local": "Caelid",
        "SubTitulo": "A terra da desolação",
        "Descricao": "Caelid é uma região marcada pela desolação e pela corrupção. Após deixar Liurnia, os jogadores se deparam com um ambiente árido, repleto de ruínas e criaturas mutantes. A atmosfera é pesada, refletindo a decadência que permeia a área.\n\nUm dos principais pontos de interesse em Caelid é a cidade de Caelid, que foi devastada por uma praga. Os jogadores encontrarão inimigos formidáveis, como os guerreiros da praga e as feras corrompidas, que representam os horrores que assolaram a região.\n\nA lore de Caelid está entrelaçada com a história de Radahn, o Flagelo Estelar, que se tornou uma figura central na narrativa do jogo. Sua luta contra a corrupção e a busca por poder o levaram a confrontos épicos, e sua presença ainda é sentida em toda a região.\n\nOs jogadores que exploram Caelid devem estar preparados para desafios intensos, pois a área é conhecida por suas armadilhas traiçoeiras e inimigos implacáveis. No entanto, aqueles que se aventuram com coragem podem descobrir segredos ocultos e recompensas valiosas."
    }
    return caelid_info